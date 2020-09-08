<template>
   <div :class="className" :style="{width: width,height: height}"></div>
</template>

<script>
    import echarts from 'echarts'
    require('echarts/theme/infographic') // echarts theme
    import resize from './mixins/resize'
    let option = {
        title: {
            text: 'bi-kmeans聚类分析结果',
            left: 'center'
        },
        xAxis: {
            type: 'value'
        },
        yAxis: {
            type: 'value'
        },
        tooltip: {
            axisPointer: {
                type: 'cross'
            }
        },
        series: []
    }
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
            getdataoption:function(result, k) {
                var series = [];
                for (let i = 0; i < k; i++) {
                    option.series.push({
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
                this.chart.setOption(option)
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
