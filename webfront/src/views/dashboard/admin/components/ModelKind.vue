<template>
    <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "ModelKind",
        mixins:[resize],
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
            default: '300px'
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
            initChart() {
                this.chart = echarts.init(this.$el, 'westeros');
                let pieData = [];
                let nameData = [];
                for (let i=0; i<this.chartData.length; i++){
                  let dict = {};
                  dict['name'] = this.chartData[i].name;
                  dict['value'] = this.chartData[i].value;
                  pieData.push(dict);
                  nameData.push(this.chartData[i].name);
                }
                this.setOptions(pieData, nameData)
            },
            setOptions(pieData, nameData){
              this.chart.setOption({
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  legend: {
                      left: 'center',
                      bottom: '10',
                      data: nameData
                  },
                  series: [
                  {
                      name: '模型类型',
                      type: 'pie',
                      roseType: 'radius',
                      radius: [15, 95],
                      center: ['50%', '38%'],
                      data: pieData,
                      animationEasing: 'cubicInOut',
                      animationDuration: 2600
                  }
                ]
              })
            }
        }
    }
</script>

<style scoped>

</style>
