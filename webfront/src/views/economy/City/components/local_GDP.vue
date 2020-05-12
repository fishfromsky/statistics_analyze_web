<template>
  <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/westeros')// echarts theme
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
                this.chart = echarts.init(this.$el, 'westeros');
                this.setOptions(this.chartData)
            },
            setOptions(val){
                this.chart.setOption({
                    title:{
                      text:'2018年各区GDP占比'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b} : {c} ({d}%)'
                    },
                    // legend: {
                    //     left: 'center',
                    //     bottom: '10',
                    //     data: ['浦东新区','嘉定区','黄浦区','闵行区','杨浦区','静安区','徐汇区','长宁区','宝山区','松江区','青浦区','普陀区','奉贤区','虹口区','金山区','崇明区']
                    // },
                    series: [
                        {
                            name: '实验学生来源',
                            type: 'pie',
                            roseType: 'radius',
                            radius: [15, 95],
                            center: ['50%', '50%'],
                            data: val,
                            animationEasing: 'cubicInOut',
                            animationDuration: 2600
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>
</style>
