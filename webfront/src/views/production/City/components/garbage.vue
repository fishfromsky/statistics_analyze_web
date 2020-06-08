<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/roma') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "garbage",
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
                this.chart = echarts.init(this.$el, 'roma');
                this.setOptions(this.chartData)
            },
            setOptions(val){
                let data = val.data
                let year = val.year
                this.chart.setOption({
                    title: {
                        text: '上海市生活垃圾产量'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['垃圾产量']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: year
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '垃圾产量',
                            type: 'line',
                            stack: '总量',
                            data: data
                        },
                      
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
