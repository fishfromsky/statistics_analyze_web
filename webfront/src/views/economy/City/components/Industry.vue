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
            let first = val.first
            let second = val.second
            let third = val.third
            let year = val.year
            this.chart.setOption({
                title: {
                    text: '上海市生产总值结构'
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
                        name: '第一产业',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: first
                    },
                    {
                        name: '第二产业',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: second
                    },
                    {
                        name: '第三产业',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: third
                    }
                ]
            })
        }
    }
}
</script>