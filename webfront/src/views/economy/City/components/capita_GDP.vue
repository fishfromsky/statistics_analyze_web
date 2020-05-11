<template>
  <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/macarons') // echarts
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
                type: Array,
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
                this.chart.setOption({
                    title:{
                        text: '上海市近20年人均GDP'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            crossStyle: {
                                color: '#999'
                            }
                        }
                    },
                    xAxis: {
                        type: 'category',
                        data: ['2000', '2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012',
                        '2013','2014','2015','2016','2017','2018','2019']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: val,
                        type: 'bar'
                    }]
                })
            }
        }
    }
</script>

<style scoped>
</style>
