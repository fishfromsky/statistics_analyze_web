<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/macarons') // echarts theme
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
                this.chart = echarts.init(this.$el, 'macarons');
                this.setOptions(this.chartData)
            },
            setOptions(val){
                let deal = val.deal
                let handle = val.handle
                let year = val.year
                this.chart.setOption({
                    title: {
                        text: '上海市垃圾清运量与处理量对比'
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
                    legend: {
                        data: ['垃圾清运量', '垃圾处理量']
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
                            name: '垃圾清运量',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: deal
                        },
                        {
                            name: '垃圾处理量',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: handle
                        },

                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
