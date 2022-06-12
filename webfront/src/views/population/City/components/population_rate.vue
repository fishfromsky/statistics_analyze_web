<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "population_rate",
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
                default: '250px'
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
            initChart(){
                this.chart = echarts.init(this.$el, 'westeros');
                this.setOptions(this.chartData)
            },
            setOptions(val){
                let population_rate = val.data
                let year = val.year
                this.chart.setOption({
                    title:{
                        text: '上海市人口自然增长率'
                    },
                    grid:{

                    },
                     tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            crossStyle: {
                                color: '#999'
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
                            }
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            name: '%',
                            axisLabel: {
                                formatter: '{value}'
                            }
                        },
                    ],
                    series: [
                        {
                            name: '人口自然增长率',
                            type: 'bar',
                            data: population_rate
                        },
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
