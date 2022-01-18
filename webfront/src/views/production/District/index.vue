<template>
    <div class="chart-wrapper">
        <el-select v-model="choose_year" style="margin-top: 20px; margin-left: 20px">
            <el-option v-for="item in year_option" :key="item" :label="item" :value="item"></el-option>
        </el-select>
        <garbagedistrict :chartData="chartdata" style="height: 80vh; margin-top: 20px"></garbagedistrict>
    </div>
</template>

<script>
import { getgarbagedistrict, filtergarbagedistrictbyyear } from '@/api/model'
import garbagedistrict from './components/productionbar.vue'
    export default {
        name: "index",
        components: {
            garbagedistrict
        },
        data(){
            return{
                choose_year: '2020',
                year_option: [],
                chartdata:{
                    district: [],
                    garbage: [],
                    choose_year: '  '
                }
            }
        },
        watch:{
            choose_year(val){
                let data = {}
                data['year'] = val
                filtergarbagedistrictbyyear(data).then(res=>{
                    if (res.code === 20000){
                        console.log(res)
                    }
                })
            }
        },
        methods: {
            isInArray: function (arr, value) {
                for (var i = 0; i < arr.length; i++) {
                    if (value === arr[i]) {
                        return true;
                    }
                }
                return false;
            },
            filterData:function(){
                let that = this
                let data = {}
                data['year'] = this.choose_year
                filtergarbagedistrictbyyear(data).then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        for (let i=0; i<result.length; i++){
                            that.chartdata.district.push(result[i].district)
                            that.chartdata.garbage.push(parseFloat(result[i].garbage).toFixed(2))
                        }
                        that.chartdata.choose_year = that.choose_year
                    }
                })
            },
            getData:function(){
                let that = this
                getgarbagedistrict().then(res=>{
                    if (res.code === 20000){
                        let result = res.data
                        for (let i=0; i<result.length; i++){
                            if (!that.isInArray(that.year_option, result[i].year)){
                                that.year_option.push(result[i].year)
                            }
                        }
                    }
                })
            }
        },
        mounted(){
            this.getData()
            this.filterData()
        }
    }
</script>

<style scoped>
.chart-wrapper{
    width: 100%;
    height: 100vh;
    background: rgb(16, 12, 42);
}
</style>
