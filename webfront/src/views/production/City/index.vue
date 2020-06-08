<template>
    <div class="dashboard-container">
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <garbage :chart-data="garbageData.production"></garbage>
                </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <deal :chart-data="garbageData.deal"></deal>
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20" style="margin-top: 40px">
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper">
                    <handle :chart-data="garbageData.handle"></handle>
                </div>
            </el-col>
            <el-col :xs="24" :sm=24 :lg="12">
                <div class="chart-wrapper">
                    <compare :chart-data="garbageData.compare"></compare>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import { getcitygarbage } from '@/api/model'
    import garbage from './components/garbage'
    import deal from './components/deal'
    import handle from './components/handle'
    import compare from './components/compare'
    export default {
        name: "index",
        components: {
            garbage,
            deal,
            handle,
            compare
        },
        data(){
            return {
                garbageData: {
                    production: {
                        year: [],
                        data: []
                    },
                    deal: {
                        year: [],
                        data: []
                    },
                    handle: {
                        year: [],
                        data: []
                    },
                    compare: {
                        year: [],
                        deal: [],
                        handle: []
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
                        for (let i=0; i<result.length; i++){
                            that.garbageData.production.year.push(result[i]['year'])
                            that.garbageData.production.data.push(parseFloat(result[i]['total_garbage']))
                            that.garbageData.deal.year.push(result[i]['year'])
                            that.garbageData.deal.data.push(parseFloat(result[i]['collect_transport_garbage']))
                            that.garbageData.handle.year.push(result[i]['year'])
                            that.garbageData.handle.data.push(parseFloat(result[i]['volume_of_treated']))
                            that.garbageData.compare.year.push(result[i]['year'])
                            that.garbageData.compare.deal.push(parseFloat(result[i]['collect_transport_garbage']))
                            that.garbageData.compare.handle.push(parseFloat(result[i]['volume_of_treated']))
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
