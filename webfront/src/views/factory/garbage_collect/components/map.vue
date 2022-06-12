<template>
  <div :class="className" :style="{ width: width, height: height }" />
</template>

<script>
// import data from "./mapdata/location_data.json"
import echarts from 'echarts'
import shanghai from './mapdata/shanghai.json'
require('echarts/theme/westeros') // echarts
import resize from './mixins/resize'

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
      type: Array,
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
    initChart() {
      this.chart = echarts.init(this.$el)
      this.setOptions(this.chartData)
    },
    setOptions(val) {
      echarts.registerMap('shanghai', shanghai) // 绑定地图数据
      this.chart.setOption({
        title: {
          text: '垃圾收集点'
        },
        tooltip: {
          trigger: 'item',
          triggerOn: 'mousemove|click',
          axisPointer: {
            type: 'line'
          },
          formatter: '{b}: {c}',
          textStyle: {
            fontSize: 14
          },
          backgroundColor: 'rgba(50,50,50,0.7)',
          borderColor: '#333',
          borderWidth: 0
        },
         toolbox:{
            show:true, //是否显示
            feature: { //要显示的具体功能
              saveAsImage:{ //保存图片
                    show:true
                },
            }
          },
        series: [
          {
            symbolSize: 5,
            data: val,
            type: 'scatter',
            coordinateSystem: 'geo'
          }
        ],
        geo: {
          map: 'shanghai',
          roam: true,
          label: {}
        }
      })
    }
  }
}
</script>

<style scoped>
</style>
