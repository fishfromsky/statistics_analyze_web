<template>
    <div class="dashboard-container">
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <compare :chart-data="garbageData.compare"></compare>
                </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <rate :chart-data="garbageData.rate"></rate>
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" style="margin-top: 40px">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <collect :chart-data="garbageData.collect"></collect>
                </div>
            </el-col>
            <el-col :xs="24" :sm=24 :lg="12">
                <div class="chart-wrapper">
                    <dealelement :chart-data="garbageData.deal_element"></dealelement>
                </div>   
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import { getcitygarbage, getcitygarbagedealdata } from '@/api/model'
    import compare from './components/compare'
    import rate from './components/rate'
    import collect from './components/collect'
    import dealelement from './components/deal_element'
    import { parse } from 'path-to-regexp'
    export default {
        name: "index",
        components: {
            compare,
            rate,
            collect,
            dealelement
        },
        data(){
            return {
                garbageData: {
                    compare: {
                        year: [],
                        deal: [],
                        handle: []
                    },
                    rate: {
                        year: [],
                        rate: []
                    },
                    collect: {
                        year: [],
                        collect_num: []
                    },
                    deal_element: {
                        year: [],
                        total: [],
                        landfill: [],
                        incineration: [],
                        compost: [],
                        else_num: []
                    }
                }
            }
        },
        methods: {
            getData(){
                let that = this
                getcitygarbage().then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        result.sort(function(a, b){
                            return parseInt(a.year) > parseInt(b.year) ? 1:-1
                        })
                        for (let i=0; i<result.length; i++){
                            that.garbageData.compare.year.push(result[i]['year'])
                            that.garbageData.compare.deal.push(parseFloat(result[i]['collect_transport_garbage']))
                            that.garbageData.compare.handle.push(parseFloat(result[i]['volume_of_treated']))
                            that.garbageData.rate.year.push(parseFloat(result[i]['year']))
                            that.garbageData.rate.rate.push(parseFloat(result[i]['rate_of_treated']))
                        }
                    }
                })
                getcitygarbagedealdata().then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        console.log(result)
                        result.sort(function(a, b){
                            return parseInt(a.year) > parseInt(b.year) ? 1:-1
                        })
                        for (let i=0; i<result.length; i++){
                            that.garbageData.collect.year.push(parseFloat(result[i]['year']))
                            that.garbageData.collect.collect_num.push(parseFloat(result[i]['collect_factory_num']))
                            that.garbageData.deal_element.year.push(parseFloat(result[i]['year']))
                            that.garbageData.deal_element.total.push(parseFloat(result[i]['factory_num_total']))
                            that.garbageData.deal_element.landfill.push(parseFloat(result[i]['landFill']))
                            that.garbageData.deal_element.incineration.push(parseFloat(result[i]['incineration']))
                            that.garbageData.deal_element.compost.push(parseFloat(result[i]['compost']))
                            that.garbageData.deal_element.else_num.push(parseFloat(result[i]['else_num']))
                        }
                    }
                })
            }
        },
        mounted(){
            this.getData()
        }
    }
</script>

<style scoped lang="scss">
    .dashboard {
        &-container {
        margin: 30px;
        }
        &-text {
        font-size: 30px;
        line-height: 46px;
        }
    }
    .chart-wrapper{
        background: #fff;
        padding: 16px 16px 0;
        margin-bottom: 32px;
        min-height: 300px;
        box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    }
</style>
