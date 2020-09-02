<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros') // echarts theme
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
            chartData: function(a, _) {
                console.log(a)
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
                this.chart.setOption({
                    title: {
                        text: 'LSTM模型运行结果'
                    },
                    tooltip: {
                        trigger: 'axis'
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
                    // xAxis: {
                    //     type: 'category',
                    //     boundaryGap: false,
                    //     data: val.year
                    // },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '实际值',
                            type: 'line',
                            stack: '实际值',
                            data: val.real
                        },
                        {
                            name: '预测值',
                            type: 'line',
                            stack: '预测值',
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
