<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <gdp-chart :chart-data="BasicInfo.GDPData"/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <capita_-gdp :chart-data="BasicInfo.CapitaGDP"/>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="24">
        <div class="chart-wrapper">
          <local_-gdp :chart-data="BasicInfo.Rate"></local_-gdp>
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
    export default {
        name: "index",
        components:{
            GdpChart,
            capita_Gdp,
            local_Gdp
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
                  unemployment_rate: [],
                  economy_rate: [],
                  year: []
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
              for (let i=0; i<result.length; i++){
                that.BasicInfo.GDPData.total.push(parseFloat(result[i]['gdp']))
                that.BasicInfo.GDPData.rate.push(result[i]['gdp_growth_rate'])
                that.BasicInfo.GDPData.year.push(result[i]['year'])
                that.BasicInfo.CapitaGDP.capita_gdp.push(parseFloat(result[i]['gdp_per_capita']))
                that.BasicInfo.CapitaGDP.year.push(result[i]['year'])
                that.BasicInfo.Rate.unemployment_rate.push(parseFloat(result[i]['unemployment_rate']))
                that.BasicInfo.Rate.economy_rate.push(parseFloat(result[i]['gdp_growth_rate']))
                that.BasicInfo.Rate.year.push(result[i]['year'])
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
