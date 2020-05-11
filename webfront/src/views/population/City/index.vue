<template>
  <div class="population-container">
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :xs="24" :sm="24" :lg="24">
        <div class="chart-wrapper1">
          <population_-map :chart-data="DensityData"></population_-map>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    const population_data = {
        density: [
            { name: '虹口区', value: 34058 },
            { name: '黄浦区', value: 32004 },
            { name: '静安区', value: 28910 },
            { name: '普陀区', value: 23431 },
            { name: '杨浦区', value: 21627 },
            { name: '徐汇区', value: 19874 },
            { name: '长宁区', value: 18112 },
            { name: '宝山区', value: 7479 },
            { name: '闵行区', value: 6836 },
            { name: '浦东新区', value: 4567 },
            { name: '嘉定区', value: 3408 },
            { name: '松江区', value: 2892 },
            { name: '青浦区', value: 1799 },
            { name: '奉贤区', value: 1681 },
            { name: '金山区', value: 1367 },
            { name: '崇明县', value: 586}
        ]
    }
    import Population_Map from "./components/Population_Map";
    export default {
        name: "index",
        components: {
            Population_Map
        },
        data(){
            return{
                DensityData: population_data.density
            }
        }
    }
</script>

<style scoped>
  .population-container{
    width: 95%;
    margin: 0 auto;
  }
  .chart-wrapper1{
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
    height: 100%;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
  .chart-wrapper{
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
</style>
