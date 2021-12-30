<template>
    <div class="dashboard-container">
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <compare :chart-data="garbageData.compare" style="height: 35vh"></compare>
                </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <rate :chart-data="garbageData.rate" style="height: 35vh"></rate>
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" style="margin-top: 20px">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <collect :chart-data="garbageData.collect" style="height: 35vh"></collect>
                </div>
            </el-col>
            <el-col :xs="24" :sm=24 :lg="12">
                <div class="chart-wrapper">
                    <dealelement :chart-data="garbageData.deal_element" style="height: 35vh"></dealelement>
                </div>   
            </el-col>
        </el-row>
        <el-row :gutter="20" style="margin-top: 20px">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <dealcapacity :chart-data="garbageData.deal_capacity" style="height: 35vh"></dealcapacity>
                </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <danger :chart-data="garbageData.dangerous" style="height: 35vh"></danger>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import { getcitygarbage, getcitygarbagedealdata, getcitygarbagecapacitydata, getcitygarbagevolumdata, getdangerousgarbage } from '@/api/model'
    import compare from './components/compare'
    import rate from './components/rate'
    import collect from './components/collect'
    import dealelement from './components/deal_element'
    import dealcapacity from './components/deal_capacity'
    import danger from './components/danger'
    import { parse } from 'path-to-regexp'
    export default {
        name: "index",
        components: {
            compare,
            rate,
            collect,
            dealelement,
            dealcapacity,
            danger
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
                    },
                    deal_capacity: {
                        year: [],
                        total: [],
                        landfill: [],
                        incineration: [],
                        compost: [],
                        else_num: []
                    },
                    dangerous: {
                        year: [],
                        production: [],
                        deal: [],
                        use: [],
                        store: []
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
                        result.sort(function(a, b){
                            return parseInt(a.year) > parseInt(b.year) ? 1:-1
                        })
                        for (let i=0; i<result.length; i++){
                            that.garbageData.collect.year.push(parseFloat(result[i]['year']))
                            that.garbageData.collect.collect_num.push(parseFloat(result[i]['collect_factory_num']))
                        }
                    }
                })
                getcitygarbagecapacitydata().then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        result.sort(function(a, b){
                            return parseInt(a.year) > parseInt(b.year) ? 1:-1
                        })
                        for (let i=0; i<result.length; i++){
                            that.garbageData.deal_element.year.push(result[i]['year'])
                            that.garbageData.deal_element.total.push(parseFloat(result[i]['deal_num_total']))
                            that.garbageData.deal_element.landfill.push(parseFloat(result[i]['landfill']))
                            that.garbageData.deal_element.incineration.push(parseFloat(result[i]['incineration']))
                            that.garbageData.deal_element.compost.push(parseFloat(result[i]['compost']))
                            that.garbageData.deal_element.else_num.push(parseFloat(result[i]['else_num']))
                        }
                    }
                })
                getcitygarbagevolumdata().then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        result.sort(function(a, b){
                            return parseInt(a.year) > parseInt(b.year) ? 1:-1
                        })
                        for (let i=0; i<result.length; i++){
                            that.garbageData.deal_capacity.year.push(result[i]['year'])
                            that.garbageData.deal_capacity.total.push(result[i]['deal_volume_total'])
                            that.garbageData.deal_capacity.landfill.push(result[i]['landfill'])
                            that.garbageData.deal_capacity.incineration.push(result[i]['incineration'])
                            that.garbageData.deal_capacity.compost.push(result[i]['compost'])
                            that.garbageData.deal_capacity.else_num.push(result[i]['else_num'])
                        }
                    }
                })
                getdangerousgarbage().then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        result.sort(function(a, b){
                            return parseInt(a.year) > parseInt(b.year) ? 1:-1
                        })
                        for (let i=0; i<result.length; i++){
                            that.garbageData.dangerous.year.push(result[i]['year'])
                            that.garbageData.dangerous.production.push(parseFloat(result[i]['production']))
                            that.garbageData.dangerous.deal.push(parseFloat(result[i]['deal']))
                            that.garbageData.dangerous.use.push(parseFloat(result[i]['use']))
                            that.garbageData.dangerous.store.push(parseFloat(result[i]['store']))
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
