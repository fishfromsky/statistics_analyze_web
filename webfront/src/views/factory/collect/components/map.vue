<template>
  <div>
    <div ref="map" class="map-container" />
    <div class="control-panel">
      <div class="button-list">
        <span>是否显示标签：</span>
        <el-switch v-model="labelstatus" @change="labelchange" />
      </div>
    </div>
  </div>
</template>
<script>
import echarts from 'echarts'
import 'echarts/extension/bmap/bmap'
import { gettransferfactory } from '@/api/model'
import da from 'element-ui/src/locale/lang/da'
var option = {
  title: {
    text: '上海市垃圾中转站信息表',
    subtext: '截至2019年数据',
    left: 'center',
    textStyle: {
      color: '#fff'
    },
    top: 20
  },
  tooltip: {
    trigger: 'item'
  },
  bmap: {
    center: [121.478423, 31.222243],
    zoom: 11,
    roam: true,
    mapStyle: {
      styleJson: [
        {
          'featureType': 'water',
          'elementType': 'all',
          'stylers': {
            'color': '#044161'
          }
        },
        {
          'featureType': 'land',
          'elementType': 'all',
          'stylers': {
            'color': '#004981'
          }
        },
        {
          'featureType': 'boundary',
          'elementType': 'geometry',
          'stylers': {
            'color': '#064f85'
          }
        },
        {
          'featureType': 'district',
          'elementType': 'labels',
          'stylers': {
            'visibility': 'on'
          }
        },
        {
          'featureType': 'railway',
          'elementType': 'all',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'highway',
          'elementType': 'geometry',
          'stylers': {
            'color': '#004981'
          }
        },
        {
          'featureType': 'highway',
          'elementType': 'geometry.fill',
          'stylers': {
            'color': '#005b96',
            'lightness': 1
          }
        },
        {
          'featureType': 'highway',
          'elementType': 'labels',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'arterial',
          'elementType': 'geometry',
          'stylers': {
            'color': '#004981'
          }
        },
        {
          'featureType': 'arterial',
          'elementType': 'geometry.fill',
          'stylers': {
            'color': '#00508b'
          }
        },
        {
          'featureType': 'poi',
          'elementType': 'all',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'green',
          'elementType': 'all',
          'stylers': {
            'color': '#056197',
            'visibility': 'off'
          }
        },
        {
          'featureType': 'subway',
          'elementType': 'all',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'manmade',
          'elementType': 'all',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'local',
          'elementType': 'all',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'arterial',
          'elementType': 'labels',
          'stylers': {
            'visibility': 'off'
          }
        },
        {
          'featureType': 'boundary',
          'elementType': 'geometry.fill',
          'stylers': {
            'color': '#029fd4'
          }
        },
        {
          'featureType': 'building',
          'elementType': 'all',
          'stylers': {
            'color': '#1a5787'
          }
        },
        {
          'featureType': 'label',
          'elementType': 'all',
          'stylers': {
            'visibility': 'off'
          }
        }
      ]
    }
  },
  series: [
    {
      name: '垃圾中转站',
      type: 'effectScatter',
      coordinateSystem: 'bmap',
      // data: this.convertData(this.data),
      data: [],
      encode: {
        value: 2
      },
      symbolSize: function(val) {
        return val[2] / 15
      },
      showEffectOn: 'emphasis',
      rippleEffect: {
        brushType: 'stroke'
      },
      hoverAnimation: true,
      label: {
        formatter: '{b}',
        position: 'right',
        show: false
      },
      itemStyle: {
        color: '#f4e925',
        shadowBlur: 10,
        shadowColor: '#333'
      },
      zlevel: 1
    }
  ]
}
export default {
  data() {
    return {
      chart: echarts.ECharts,
      data: [],
      geoCoordMap: {},
      labelstatus: false
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      var that = this
      gettransferfactory().then(res => {
        if (res.code === 20000) {
          const data = res.data
          for (let i = 0; i < data.length; i++) {
            const name = data[i]['name']
            const value = data[i]['capacity']
            const longitude = data[i]['longitude']
            const latitude = data[i]['latitude']
            that.data.push({ name: name, value: value })
            that.geoCoordMap[name] = [longitude, latitude]
          }
          that.initChart()
        }
      })
    },
    labelchange: function() {
      option.series[0].label.show = this.labelstatus
      this.chart.setOption(option)
    },
    convertData(data) {
      var res = []
      for (var i = 0; i < data.length; i++) {
        var geoCoord = this.geoCoordMap[data[i].name]
        if (geoCoord) {
          res.push({
            name: data[i].name,
            value: geoCoord.concat(data[i].value)
          })
        }
      }
      return res
    },
    initChart() {
      this.chart = echarts.init(this.$refs.map)
      option.series[0].data = this.convertData(this.data)
      option.series[0].label.show = this.labelstatus
      this.chart.setOption(option)
    }
  }
}
</script>

<style lang="less" scoped>
    .map-container{
        position: relative;
        z-index: 10;
        width: 100%;
        height: 95vh;
    }
    .control-panel{
        width: 250px;
        height: 60px;
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 100
    }
    .button-list{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    .button-list span{
        font-size: 15px;
        color: #fff;
    }
</style>
