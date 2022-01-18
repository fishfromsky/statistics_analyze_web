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
                        text: '灰色关联度分析矩阵',
                        left: 'center'
                    },
                    tooltip: {
                        position: 'top',
                    },
                    animation: false,
                    grid: {
                        height: '50%',
                        top: '10%',
                        left: '70'
                    },
                    xAxis: {
                        type: 'category',
                        data: val.label,
                        axisLabel : {   //坐标轴刻度标签的相关设置。
                            interval:0,
                            rotate:"45"
                        },
                        splitArea: {
                            show: true
                        }
                    },
                    yAxis: {
                        type: 'category',
                        data: val.label,
                        axisLabel: {
                            interval: 0,
                            rotate: "60"
                        },
                        splitArea: {
                            show: true
                        }
                    },
                    visualMap: {
                        min: 0,
                        max: 1,
                        calculable: true,
                        orient: 'horizontal',
                        left: 'center',
                        bottom: '15%'
                    },
                    series: [{
                        name: '相关系数',
                        type: 'heatmap',
                        data: val.result,
                        label: {
                            show: true
                        },
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }]
                })
            }
        }
    }
</script>

<style scoped>
</style>
