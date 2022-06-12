<template>
  <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
import echarts from 'echarts'

require('echarts/theme/westeros') // echarts theme
import resize from './mixins/resize'

export default {
  name: "production",
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
      default: '500px'
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
    this.chart.dispose();
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'westeros');
      this.setOptions(this.chartData)
    },
    setOptions(val) {
      let population_data = val.data
      let year = val.year
      this.chart.setOption({
        title: {
          text: '上海橡塑类垃圾产量',
          textStyle: {
            fontSize: 30
          }
        },
        grid: {
          top: '20%'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            },
            label: {
              fontSize: 20
            }
          }
        },
         toolbox:{
            show:true, //是否显示
            feature: { //要显示的具体功能
              saveAsImage:{ //保存图片
                    show:true
                },
            }
          },
        xAxis: [
          {
            type: 'category',
            data: year,
            axisPointer: {
              type: 'shadow'
            },
            axisLabel: {
              fontSize: 25
            },
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: '万吨',
            axisLabel: {
              formatter: '{value}',
              fontSize: 25
            },
            nameTextStyle:{
              fontSize: 30
            }
          },
        ],
        series: [
          {
            name: '垃圾产量',
            type: 'bar',
            data: population_data
          },
        ]
      })
    }
  }
}
</script>

<style scoped>
</style>
