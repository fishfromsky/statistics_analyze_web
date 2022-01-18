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
                let total = val.total
                let landfill = val.landfill
                let incineration = val.incineration
                let compost = val.compost
                let else_num = val.else_num
                this.chart.setOption({
                    title: {
                        text: '上海市生活垃圾无害化处理能力'
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
                            name: '处理总量',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: total
                        },
                        {
                            name: '垃圾填埋',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: landfill
                        },
                        {
                            name: '焚烧',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: incineration
                        },
                        {
                            name: '堆肥',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: compost
                        },
                        {
                            name: '其他',
                            type: 'line',
                            stack: '总量',
                            areaStyle: {},
                            data: else_num
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
