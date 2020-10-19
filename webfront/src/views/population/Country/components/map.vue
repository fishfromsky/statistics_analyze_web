<template>
  <div :class="className" :style="{ width: width, height: height }" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/westeros') // echarts
import resize from './mixins/resize'
import 'echarts/extension/bmap/bmap'

import data from './mapdata/heat_data.json'

var lngExtent = [30.6882888542, 31.8830482032]
var latExtent = [120.863603906, 122.247009468]
var cellCount = [134, 155]
var cellSizeCoord = [
  (lngExtent[1] - lngExtent[0]) / cellCount[0],
  (latExtent[1] - latExtent[0]) / cellCount[1]
]
var gapSize = 0

export default {
  name: 'GDP',
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '700px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
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
      this.chart = echarts.init(this.$el)
      this.setOptions(this.chartData)
    },
    setOptions(val) {

      this.chart.setOption({
        tooltip: {},
        visualMap: {
          type: 'continuous',
          min: 0,
          max: 60000,
          top: 10,
          left: 10,
          range: [1, 60000],
          inRange: {
            color: ['#AFEEEE', '#4169E1', '#8B0000'],
            colorAlpha: [0.6, 0.9]
          },
          outOfRange: {
            color: ['rgba(0,0,0,0)'],
            opacity: 0
          }
        },
        series: [
          {
            type: 'custom',
            coordinateSystem: 'bmap',
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
        bmap: {
          center: [116.46, 39.92],
          zoom: 11.8,
          roam: true,
          mapStyle: {
            styleJson: [{
              'featureType': 'water',
              'elementType': 'all',
              'stylers': {
                'color': '#d1d1d1'
              }
            }, {
              'featureType': 'land',
              'elementType': 'all',
              'stylers': {
                'color': '#f3f3f3'
              }
            }, {
              'featureType': 'railway',
              'elementType': 'all',
              'stylers': {
                'visibility': 'off'
              }
            }, {
              'featureType': 'highway',
              'elementType': 'all',
              'stylers': {
                'color': '#999999'
              }
            }, {
              'featureType': 'highway',
              'elementType': 'labels',
              'stylers': {
                'visibility': 'off'
              }
            }, {
              'featureType': 'arterial',
              'elementType': 'geometry',
              'stylers': {
                'color': '#fefefe'
              }
            }, {
              'featureType': 'arterial',
              'elementType': 'geometry.fill',
              'stylers': {
                'color': '#fefefe'
              }
            }, {
              'featureType': 'poi',
              'elementType': 'all',
              'stylers': {
                'visibility': 'off'
              }
            }, {
              'featureType': 'green',
              'elementType': 'all',
              'stylers': {
                'visibility': 'off'
              }
            }, {
              'featureType': 'subway',
              'elementType': 'all',
              'stylers': {
                'visibility': 'off'
              }
            }, {
              'featureType': 'manmade',
              'elementType': 'all',
              'stylers': {
                'color': '#d1d1d1'
              }
            }, {
              'featureType': 'local',
              'elementType': 'all',
              'stylers': {
                'color': '#d1d1d1'
              }
            }, {
              'featureType': 'arterial',
              'elementType': 'labels',
              'stylers': {
                'visibility': 'off'
              }
            }, {
              'featureType': 'boundary',
              'elementType': 'all',
              'stylers': {
                'color': '#fefefe'
              }
            }, {
              'featureType': 'building',
              'elementType': 'all',
              'stylers': {
                'color': '#d1d1d1'
              }
            }, {
              'featureType': 'label',
              'elementType': 'labels.text.fill',
              'stylers': {
                'color': 'rgba(0,0,0,0)'
              }
            }]
          }
        }
      })
    }
  }
}
</script>

<style scoped>
</style>
