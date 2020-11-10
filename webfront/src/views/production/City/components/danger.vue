<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "compare",
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
                let year = val.year
                let production = val.production
                let deal = val.deal
                let use = val.use
                let store = val.store
                this.chart.setOption({
                    title: {
                        text: '上海危险废弃物产生数据'
                    },
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
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: year
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: '产生量',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: production
                        },
                        {
                            name: '处置量',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: deal
                        },
                        {
                            name: '综合利用',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: use
                        },
                        {
                            name: '储存量',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: store
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
