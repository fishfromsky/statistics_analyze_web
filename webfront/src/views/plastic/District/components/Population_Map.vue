<template>
  <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import shanghai from './mapdata/shanghai.json'
    import echarts from 'echarts'
    require('echarts/theme/macarons') // echarts theme
    import resize from './mixins/resize'
    export default {
        name: "Population_Map",
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
                default: '800px'
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
        mounted() {
            this.$nextTick(() => {
                this.initChart()
            })
        },
        beforeDestroy() {
            if (!this.chart) {
                return
            }
            this.chart.dispose()
            this.chart = null
        },
        methods: {
            initChart(){
                this.chart = echarts.init(this.$el, 'macarons');
                this.setOptions(this.chartData)
            },
            setOptions(data) {
                echarts.registerMap('shanghai', shanghai)
                this.chart.setOption({
                    title: {
                        text: '上海市各区橡塑类垃圾产量'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{b}<br/>{c} (万吨)'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'right',
                        top: 'center',
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    visualMap: {
                        min: 800,
                        max: 25000,
                        text: ['High', 'Low'],
                        realtime: false,
                        calculable: true,
                        inRange: {
                            color: ['lightskyblue', 'yellow', 'orangered']
                        }
                    },
                    series: [
                        {
                            name: '上海市各区橡塑类垃圾产量',
                            type: 'map',
                            mapType: 'shanghai', // 自定义扩展图表类型
                            data: data
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>

</style>
