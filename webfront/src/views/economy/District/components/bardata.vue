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
                this.chart.setOption({
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    legend: {
                        data: ['GDP', '第一产业GDP', '第二产业GDP', '第三产业GDP']
                    },
                   toolbox:{
            show:true, //是否显示
            feature: { //要显示的具体功能
              saveAsImage:{ //保存图片
                    show:true
                },
            }
          },
                    xAxis: [
                        {
                            type: 'category',
                            axisTick: {show: false},
                            data: val.district,
                            axisLabel : {   //坐标轴刻度标签的相关设置。
                                interval:0,
                                rotate:"45"
                            },
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: 'GDP',
                            type: 'bar',
                            barGap: 0,
                            // label: labelOption,
                            data: val.gdp
                        },
                        {
                            name: '第一产业GDP',
                            type: 'bar',
                            // label: labelOption,
                            data: val.gdp_first_industry
                        },
                        {
                            name: '第二产业GDP',
                            type: 'bar',
                            // label: labelOption,
                            data: val.gdp_second_industry
                        },
                        {
                            name: '第三产业GDP',
                            type: 'bar',
                            // label: labelOption,
                            data: val.gdp_third_industry
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
