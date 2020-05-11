<template>
  <div class="dashboard-container">
    <el-row>
      <el-col :xs="24" :sm="24" :lg="24">
        <div class="chart-wrapper">
          <gdp-chart :chart-data="economyData"/>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="16">
        <div class="chart-wrapper">
          <capita_-gdp :chart-data="capitaData"/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <local_-gdp :chart-data="localGdp"></local_-gdp>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    const BasicInfo = {
        GDPData: {
            total: [4812.15, 5257.66, 5795.02, 6762.38, 8165.38, 9365.54, 10718.04, 12668.89, 14276.79, 15287.56, 17436.85,
                 19539.07, 20558.98, 22264.06, 24068.20, 25659.18, 28183.51, 30632.99, 32679.87, 38155.32],
            rate: [11,10.5,10.9,11.8,13.64,11.1,12,14.3,9.7,8.24,10.34,8.2,7.5,7.04,7,6.9,6.9,6.9,6.6,6]
        },
        CapitaGDP: [30307,32089,34277,38878,45353,50282,55615,62909,67916,70273,77275,84037,86969,92852,99438,106009,116582,126634,134982,157300],
        LocalGDP: [
            { name: '浦东新区', value: 10460.1},
            { name: '嘉定区', value: 2362.7},
            { name: '黄浦区', value: 2270.3},
            { name: '闵行区', value: 2013.7},
            { name: '杨浦区', value: 1847.8},
            { name: '静安区', value: 1840.0},
            { name: '徐汇区', value: 1670.7},
            { name: '长宁区', value: 1418.8},
            { name: '宝山区', value: 1392.1},
            { name: '松江区', value: 1279.7},
            { name: '青浦区', value: 1074.3},
            { name: '普陀区', value: 1001.8},
            { name: '奉贤区', value: 841.5},
            { name: '虹口区', value: 838.0},
            { name: '金山区', value: 759.9},
            { name: '崇明区', value: 351.1}
        ]
    }
    import { mapGetters } from 'vuex'
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
                economyData: BasicInfo.GDPData,
                capitaData: BasicInfo.CapitaGDP,
                localGdp: BasicInfo.LocalGDP
            }
        },
        computed: {
            ...mapGetters([
                'name'
            ])
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
