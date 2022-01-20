<template>
  <div ref="map" class="map-container"></div>
</template>


<script>
import echarts from 'echarts'
import resize from './mixins/resize'
import data from './mapdata/medal.json'
import shanghai from './mapdata/shanghai.json'

echarts.registerMap('shanghai', shanghai)

var lngExtent = [30.6503888542, 31.8030482032]
var latExtent = [120.893603906, 122.351009468]
// 方格图的行边界和列边界
var cellCount = [134, 155]
var cellSizeCoord = [
  (lngExtent[1] - lngExtent[0]) / cellCount[0],
  (latExtent[1] - latExtent[0]) / cellCount[1]
]

export default {
  name: 'GDP',
  data() {
    return {
      chart: echarts.ECharts
    }
  },
  watch: {},
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },

  methods: {
    getCoord(params, api, lngIndex, latIndex) {
      var coords = params.context.coords || (params.context.coords = [])
      var key = lngIndex + '-' + latIndex
      // bmap returns point in integer, which makes cell width unstable.
      // So we have to use right bottom point.
      return coords[key] || (coords[key] = api.coord([
        +(latExtent[0] + lngIndex * cellSizeCoord[0]).toFixed(6),
        +(lngExtent[0] + latIndex * cellSizeCoord[1]).toFixed(6)
      ]))
    },

    renderItem(params, api) {
      var lngIndex = api.value(0)
      var latIndex = api.value(1)
      var pointLeftTop = this.getCoord(params, api, lngIndex, latIndex)
      var pointRightBottom = this.getCoord(params, api, lngIndex + 1, latIndex + 1)

      return {
        type: 'rect',
        shape: {
          x: pointLeftTop[0],
          y: pointLeftTop[1],
          width: pointRightBottom[0] - pointLeftTop[0],
          height: pointRightBottom[1] - pointLeftTop[1]
        },
        style: api.style({
          stroke: 'rgba(0,0,0,0)'
        }),
        styleEmphasis: api.styleEmphasis()
      }
    },
    initChart() {
      this.chart = echarts.init(this.$refs.map)
      this.chart.setOption({
        tooltip: {},
        visualMap: {
          type: 'continuous',
          itemWidth: 40,
          itemHeight: 200,
          textStyle: {
            color: 'rgba(255, 255, 255, 1)',
            fontWeight: 'normal',
            fontSize: 24
          },
          min: 0,
          max: 500,
          top: 10,
          left: 10,
          range: [1, 500],
          inRange: {
            color: ['#AFEEEE', '#FAE900', '#F6AE00', '#C41A1A'],
            colorAlpha: [0.8, 0.9]
          },
          outOfRange: {
            color: ['rgba(0,0,0,0)'],
            opacity: 0
          }
        },
        series: [
          {
            type: 'custom',
            coordinateSystem: 'geo',
            renderItem: this.renderItem,
            animation: false,
            emphasis: {
              itemStyle: {
                color: 'yellow'
              }
            },
            encode: {
              tooltip: 2
            },
            data: data
          }
        ],
        geo: {
          map: 'shanghai',
          zoom: 1.2,
          center: [121.477665, 31.226048],
          label: {
            emphasis: {
              show: true,
              textStyle: {
                color: '#fff'
              }
            }
          },
          roam: true, //是否允许缩放
          itemStyle: {
            normal: {
              color: '#101f32', //地图背景色
              borderColor: '#43d0d6', //省市边界线
              borderWidth: 1.1
            },
            emphasis: {
              color: '#43d0d6' //悬浮背景
            }
          }
        }
      })
    }
  }
}
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 100%;
  background: url("../../../image/factory_bg.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}
</style>
