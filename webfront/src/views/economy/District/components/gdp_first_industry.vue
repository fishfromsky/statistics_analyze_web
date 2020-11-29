<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "GDP",
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
                let gdp = val.gdp
                let year = val.year
                this.chart.setOption({
                    title:{
                        text: val.district+'第一产业生产总值(GDP)'
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
                    xAxis: [
                        {
                            type: 'category',
                            data: year,
                            axisPointer: {
                                type: 'shadow'
                            },
                            axisLabel : {   //坐标轴刻度标签的相关设置。
                                interval:0,
                                rotate:"45"
                            },
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            name: '亿元',
                            axisLabel: {
                                formatter: '{value}'
                            }
                        }
                    ],
                    series: [
                        {
                            name: '生产总值',
                            type: 'line',
                            data: gdp
                        }
                    ]

                })
            }
        }
    }
</script>

<style scoped>
</style>
