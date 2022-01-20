<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/walden') // echarts theme
import resize from './mixins/resize'

export default {
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
      default: '350px'
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
    initChart() {
      this.chart = echarts.init(this.$el, 'walden')
      this.setOptions(this.chartData)
    },
    setOptions(val) {
        this.chart.setOption({
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: val.year,
                splitLine:{
                    show: false
                }
            },
            yAxis: {
                type: 'value',
                splitLine:{
                    show: false
                }
            },
            series: [
                {
                    name: '湿垃圾',
                    type: 'line',
                    data: val.wet
                },
                {
                    name: '干垃圾',
                    type: 'line',
                    data: val.dry
                },
                {
                    name: '可回收物',
                    type: 'line',
                    data: val.recycle
                },
                {
                    name: '有害垃圾',
                    type: 'line',
                    data: val.harm
                },
                {
                    name: '清运总量',
                    type: 'line',
                    data: val.total
                },
            ]
      })
    }
  }
}
</script>
