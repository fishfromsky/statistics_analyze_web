<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/roma') // echarts theme
    import resize from './mixins/resize'
    export default {
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
                this.chart.setOption({
                    title: {
                        text: '多元回归模型运行结果'
                    },
                    legend: {
                        data: ['实际值', '预测值']
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
                        data: val.year
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '实际值',
                            type: 'scatter',
                            stack: '实际值',
                            emphasis: {
                                label: {
                                    show: true,
                                    position: 'left',
                                    color: 'red',
                                    fontSize: 16
                                }
                            },
                            data: val.real
                        },
                        {
                            name: '预测值',
                            type: 'line',
                            stack: '预测值',
                            emphasis: {
                                label: {
                                    show: true,
                                    position: 'left',
                                    color: 'blue',
                                    fontSize: 16
                                }
                            },
                            data: val.pred
                        },
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
