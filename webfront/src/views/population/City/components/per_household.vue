<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/macarons') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "per_household",
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
                let per_data = val.per_data
                let year = val.year
                this.chart.setOption({
                    title: {
                        text: '上海市每户平均人口数据'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    grid: {
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
                        type: 'value',
                        anme: '人'
                    },
                    series: [
                        {
                            name: '每户平均人口',
                            type: 'line',
                            stack: '总量',
                            data: per_data
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
