<template>
    <div :class="className" :style="{width:width,height:height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros') // echarts theme
    import resize from './mixins/resize'

    const animationDuration = 6000;

    export default {
        name: "BarChart",
        mixins: [resize],
        props:{
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
         data(){
          return {
            chart: null
          }
        },
        watch:{
          chartData:{
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
        methods:{
          initChart(){
             this.chart = echarts.init(this.$el, 'westeros');
             this.setOptions(this.chartData)
          },
          setOptions({model1,model2,p} = {}){
            this.chart.setOption({
              tooltip:{
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                }
              },
               grid: {
                top: 10,
                left: '2%',
                right: '2%',
                bottom: '3%',
                containLabel: true
              },
              xAxis: [{
                name: '集散厂数量',
                type: 'category',
                data: p,
                axisTick: {
                  alignWithLabel: true
                },
                axisLabel:{
                  interval: 0,
                  rotate: 0
                }
              }],
              yAxis: [{
                name: '万元',
                type: 'value',
                axisTick: {
                  show: false
                }
              }],
              series:[
                {
                  name: '交通成本',
                  type: 'bar',
                  stack: 'vistors',
                  barWidth: '60%',
                  data: model1,
                  color: '#59C4E6',
                  animationDuration
                }, {
                  name: '规模成本',
                  type: 'bar',
                  stack: 'vistors',
                  barWidth: '60%',
                  data: model2,
                  color: '#EDAFDA',
                  animationDuration
                }
              ]
            })
          }
        }
    }
</script>

<style scoped>

</style>
