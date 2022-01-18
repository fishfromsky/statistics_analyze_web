<template>
  <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros')// echarts theme
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
                let year = val.year
                let unemployment_rate = val.unemployment_rate
                let economy_rate = val.economy_rate
                this.chart.setOption({
                    title: {
                        text: '上海市GDP增长率'
                    },
                    xAxis: {
                    data: year,
                    boundaryGap: false,
                    axisTick: {
                        show: false
                    },
                    axisLabel:{
                        interval: 0,
                        rotate: 60
                    }
                    },
                    grid: {
                    left: 10,
                    right: 10,
                    bottom: 20,
                    top: 50,
                    containLabel: true
                    },
                    tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross'
                    },
                    padding: [5, 10]
                    },
                    yAxis: {
                        type: 'value',
                        name: '%'
                    },
                    series: [{
                        name: 'GDP增长率',
                        itemStyle: {
                                normal: {
                                color: '#FF005A',
                                lineStyle: {
                                    color: '#FF005A',
                                    width: 2
                                }
                            }
                        },
                        smooth: true,
                        type: 'line',
                        data: economy_rate,
                        animationDuration: 2800,
                        animationEasing: 'quadraticOut'
                    }]
                })
            }
        }
    }
</script>

<style scoped>
</style>
