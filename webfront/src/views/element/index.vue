<template>
    <div>
        <div class="main-box">
            <div class="header">
                <div class="header-text">上海市固废垃圾成分</div>
            </div>
            <el-row :gutter="20" style="margin-top: 20px">
                <el-col :xs="24" :sm="24" :lg="12">
                    <el-row>
                        <el-col :xs="24" :sm="24" :lg="24">
                            <div class="chart-wrapper">
                                <div class="titlebox">主要垃圾生产量变化</div>
                                <biggarbage :chartData="data1"></biggarbage>
                            </div> 
                        </el-col>
                        <el-col :xs="24" :sm="24" :lg="24">
                            <div class="chart-wrapper">
                                <div class="titlebox">次要垃圾生产量变化</div>
                                <smallgarbage :chartData="data3"></smallgarbage>                               
                            </div>
                        </el-col>
                    </el-row>
                </el-col>
                <el-col :xs="24" :sm="24" :lg="12">
                    <div class="chart-wrapper">
                        <div class="titlebox">{{graphyear}}年固废成分信息</div>
                        <el-select v-model="graphyear" class="choosebox">
                            <el-option v-for="item in chooseyear" :key="item.value" :label="item.label" :value="item.value"></el-option>
                        </el-select>
                        <graphchart :chartData="data2" style="height:80vh"></graphchart>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import { getgarbageelement } from '@/api/model'
    import biggarbage from './components/biggarbage.vue'
    import graphchart from './components/graphchart.vue'
    import smallgarbage from './components/smallgarbage.vue'
    export default {
        name: "index",
        components: {
            biggarbage,
            graphchart,
            smallgarbage
        },
        data(){
            return{
                data: null,
                data1: {
                    year: [],
                    cook: [],
                    paper: [],
                    plastic: [],
                    recycle: [],
                    fire: []
                },
                data3: {
                    year: [],
                    clothe: [],
                    wood: [],
                    ash: [],
                    china: [],
                    glass: [],
                    metal: [],
                    other: [],
                    mix: []
                },
                data2:[],
                graphyear: '2016',
                chooseyear: []
            }
        },
        watch:{
            graphyear(val){
                this.getGraphData(val)
            }
        },
        methods:{
            getGraphData(year){
                for (let i=0; i<this.data.length; i++){
                    if (this.data[i].year === year){
                        let list = []
                        list.push({value: this.data[i].cook.toFixed(2), name: '厨余类'})
                        list.push({value: this.data[i].paper.toFixed(2), name: '纸类'})
                        list.push({value: this.data[i].plastic.toFixed(2), name: '橡塑类'})
                        list.push({value: this.data[i].clothe.toFixed(2), name: '纺织类'})
                        list.push({value: this.data[i].wood.toFixed(2), name: '木竹类'})
                        list.push({value: this.data[i].ash.toFixed(2), name: '灰土类'})
                        list.push({value: this.data[i].china.toFixed(2), name: '砖瓦陶瓷类'})
                        list.push({value: this.data[i].glass.toFixed(2), name: '玻璃类'})
                        list.push({value: this.data[i].metal.toFixed(2), name: '金属类'})
                        list.push({value: this.data[i].other.toFixed(2), name: '其他类'})
                        list.push({value: this.data[i].mix.toFixed(2), name: '混合类'})
                        list.push({value: this.data[i].recycle.toFixed(2), name: '可回收类'})
                        list.push({value: this.data[i].fire.toFixed(2), name: '可燃类'})
                        this.data2 = list
                        break
                    }
                }
            },
            getData:function(){
                getgarbageelement().then(res=>{
                    if (res.code === 20000){
                        this.data = res.data
                        for (let i=0; i<this.data.length; i++){
                            this.data1.year.push(this.data[i].year)
                            this.chooseyear.push({value: this.data[i].year, label: this.data[i].year})
                            this.data1.cook.push(this.data[i].cook.toFixed(2))
                            this.data1.paper.push(this.data[i].paper.toFixed(2))
                            this.data1.plastic.push(this.data[i].plastic.toFixed(2))
                            this.data1.recycle.push(this.data[i].recycle.toFixed(2))
                            this.data1.fire.push(this.data[i].fire.toFixed(2))
                            this.data3.year.push(this.data[i].year)
                            this.data3.clothe.push(this.data[i].clothe.toFixed(2))
                            this.data3.wood.push(this.data[i].wood.toFixed(2))
                            this.data3.ash.push(this.data[i].ash.toFixed(2))
                            this.data3.china.push(this.data[i].china.toFixed(2))
                            this.data3.glass.push(this.data[i].glass.toFixed(2))
                            this.data3.metal.push(this.data[i].metal.toFixed(2))
                            this.data3.other.push(this.data[i].other.toFixed(2))
                            this.data3.mix.push(this.data[i].mix.toFixed(2))
                        }
                        this.getGraphData(this.data[this.data.length-1].year)
                    }
                })
            }
        },
        mounted(){
            this.getData()
        }
    }
</script>

<style lang="less">
    .titlebox{
        width: 35%;
        height: 35px;
        background: rgba(0,161,255,0.7);
        text-align: center;
        color: #fff;
        line-height: 35px;
        margin: 0 auto;
        margin-top: -35px;
        border-radius: 10px;
    }
    .main-box{
        width: 100%;
        min-height: calc(100vh - 50px);
        background-color: rgb(8, 15, 62);
        padding: 20px;
    }
    .header{
        width: 100%;
        height: 45px;
        padding-top: 10px;
    }
    .header-text{
        color: #fff;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
    }
    .chart-wrapper{
        padding: 16px 16px 0;
        margin-bottom: 32px;
        box-shadow: 0 0 10px 10px rgba(0,161,255,0.1);
        border: 1px solid #00a1ff;
        background: linear-gradient(#00faff, #00faff) left top,
		linear-gradient(#00faff, #00faff) left top,
		linear-gradient(#00faff, #00faff) right top,
		linear-gradient(#00faff, #00faff) right top,
		linear-gradient(#00faff, #00faff) left bottom,
		linear-gradient(#00faff, #00faff) left bottom,
		linear-gradient(#00faff, #00faff) right bottom,
		linear-gradient(#00faff, #00faff) right bottom;
        background-repeat: no-repeat;
        background-size: 5px 20px, 20px 5px;
        background-color: rgba(0,161,255,0.1);
    }
    .choosebox{
        width: 28%;
        height: 40px;
        margin-left: 70%;
        /deep/ .el-select,
        /deep/ .el-input,
        /deep/ .el-input__inner{
            background: rgba(0,161,255,0.2);
            color:#00faff;
            font-size: 16px;
            border:0px;
            border-radius:0px;
            text-align: center;
            border: #00a1ff 1px solid;
        }
        /deep/ .el-select-dropdown__list{
            background: #08164d;
            margin: 0px;
            border:0px;
            border-radius: 0px;
        }

        //修改单个的选项的样式
        /deep/ .el-select-dropdown__item{
            background-color: transparent;
        }

        //item选项的hover样式
        /deep/ .el-select-dropdown__item.hover, 
        /deep/ .el-select-dropdown__item:hover{
            color:#409eff;
        }
    }
</style>
