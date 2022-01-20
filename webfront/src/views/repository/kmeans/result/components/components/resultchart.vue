<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/infographic') // echarts theme
    import resize from './mixins/resize'
    import { param } from '@/utils'
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
                chart: null,
                xlabel: '',
                ylabel: ''
            }
        },
        computed:{
            option: function(){
                let that = this
                return {
                    title: {
                        text: 'bi-kmeans聚类分析结果',
                        left: 'center'
                    },
                    xAxis: {
                        type: 'value',
                        name: that.xlabel
                    },
                    yAxis: {
                        type: 'value',
                        name: that.ylabel
                    },
                    tooltip: {
                        axisPointer: {
                            type: 'cross'
                        },
                    },
                    series: []
                }
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
            getdataoption:function(result, k) {
                var series = [];
                for (let i = 0; i < k; i++) {
                    this.option.series.push({
                        name: 'scatter' + i,
                        type: 'scatter',
                        animation: false,
                        data: result[i],
                        markPoint: {
                            symbolSize: 29,
                            label: {
                                show: false
                            },
                            itemStyle: {
                                opacity: 0.7
                            }
                        }
                    });
                }
            },
            initChart(){
                this.chart = echarts.init(this.$el, 'infographic');
                this.setOptions(this.chartData)
            },
            setOptions(val){
                this.xlabel = val.xlabel
                this.ylabel = val.ylabel
                let label_num = this.judgesortnum(val.label)
                let dataset = []
                for (let i=0; i<label_num; i++){
                    dataset.push([])
                }
                for (let i=0; i<val.label.length; i++){
                    let index = val.label[i]
                    dataset[index].push([val.xaxis[i], val.yaxis[i]])
                }
                this.getdataoption(dataset, label_num)
                this.chart.setOption(this.option)
            },
            judgesortnum:function(list){
                let tmp_sort = []
                for (let i=0; i<list.length; i++){
                    if (!this.isInArray(tmp_sort, list[i])){
                        tmp_sort.push(list[i])
                    }
                }
                return tmp_sort.length
            },
            isInArray:function(arr,value){
                for(var i = 0; i < arr.length; i++){
                    if(value === arr[i]){
                        return true;
                    }
                }
                return false;
            },
        }
    }
</script>

<style scoped>
</style>
