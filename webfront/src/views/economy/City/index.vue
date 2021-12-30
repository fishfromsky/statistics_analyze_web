<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <gdp-chart :chart-data="BasicInfo.GDPData" style="height: 35vh"/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <capita_-gdp :chart-data="BasicInfo.CapitaGDP" style="height: 35vh"/>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <local_-gdp :chart-data="BasicInfo.Rate" style="height: 35vh"></local_-gdp>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <industry :chart-data="BasicInfo.Industry" style="height: 35vh"></industry>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex'
    import { getcityeconomydata } from '@/api/model'
    import GdpChart from './components/GDP'
    import capita_Gdp from './components/capita_GDP'
    import local_Gdp from './components/local_GDP'
    import Industry from './components/Industry'
import { parse } from 'path-to-regexp'
    export default {
        name: "index",
        components:{
            GdpChart,
            capita_Gdp,
            local_Gdp,
            Industry
        },
        data(){
            return {
              BasicInfo: {
                GDPData: {
                    total: [],
                    rate: [],
                    year: []
                },
                CapitaGDP: {
                  capita_gdp: [],
                  year: []
                },
                Rate: {
                  economy_rate: [],
                  year: []
                },
                Industry: {
                  year: [],
                  first: [],
                  second: [],
                  third: []
                }
              }
            }
        },
        computed: {
            ...mapGetters([
                'name'
            ])
        },
        mounted(){
          let that = this;
          getcityeconomydata().then(res=>{
            if (res.code === 20000){
              let result = res.data
              result.sort(function(a, b){
                return parseInt(a.year) > parseInt(b.year) ? 1:-1
              })
              for (let i=0; i<result.length; i++){
                that.BasicInfo.GDPData.total.push(parseFloat(result[i]['gdp']))
                that.BasicInfo.GDPData.rate.push(result[i]['gdp_growth_rate'])
                that.BasicInfo.GDPData.year.push(result[i]['year'])
                that.BasicInfo.CapitaGDP.capita_gdp.push(parseFloat(result[i]['gdp_per_capita']))
                that.BasicInfo.CapitaGDP.year.push(result[i]['year'])
                that.BasicInfo.Rate.economy_rate.push(parseFloat(result[i]['gdp_growth_rate']))
                that.BasicInfo.Rate.year.push(result[i]['year'])
                that.BasicInfo.Industry.year.push(result[i]['year'])
                let sum = result[i]['gdp_first_industry']+result[i]['gdp_second_industry']+result[i]['gdp_third_industry']
                that.BasicInfo.Industry.first.push((result[i]['gdp_first_industry']/sum).toFixed(2))
                that.BasicInfo.Industry.second.push((result[i]['gdp_second_industry']/sum).toFixed(2))
                that.BasicInfo.Industry.third.push((result[i]['gdp_third_industry']/sum).toFixed(2))
              }
            }
          })
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
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
</style>
