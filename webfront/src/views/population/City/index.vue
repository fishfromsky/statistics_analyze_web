<template>
  <div class="population-container">
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper1">
          <population_-map :chart-data="population_data.density"></population_-map>
        </div>
        <div class="chart-wrapper">
          <perhousehold :chart-data="population_data.perhousehold"></perhousehold>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <el-row>
          <el-col :xs="24" :sm="24" :lg="24">
            <div class="chart-wrapper">
              <population :chart-data="population_data.population"></population>
            </div>
            <div class="chart-wrapper">
              <household :chart-data="population_data.household"></household>
            </div>
            <div class="chart-wrapper">
              <density :chart-data="population_data.population_density"></density>
            </div>
            <div class="chart-wrapper">
              <populationrate :chart-data="population_data.population_rate"></populationrate>
            </div>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex'
    import Population_Map from "./components/Population_Map";
    import population from './components/population'
    import household from './components/household'
    import perhousehold from './components/per_household'
    import density from './components/density'
    import populationrate from './components/population_rate'
    import { getcitypopulationdata } from '@/api/model'
    export default {
        name: "index",
        components: {
            Population_Map,
            population,
            household,
            perhousehold,
            density,
            populationrate
        },
        data(){
            return{
                population_data: {
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
                    { name: '崇明区', value: 586}
                  ],
                  population: {
                    data: [],
                    year: []
                  },
                  household: {
                    households: [],
                    year: []
                  },
                  perhousehold: {
                    year: [],
                    per_data: []
                  },
                  population_density: {
                    data: [],
                    year: []
                  },
                  population_rate: {
                    data: [],
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
          var that = this
          getcitypopulationdata().then(res=>{
            if (res.code === 20000){
              let result = res.data
              print(result)
              for (let i=0; i<result.length; i++){
                that.population_data.population.data.push(parseFloat(result[i]['population']))
                that.population_data.population.year.push(result[i]['year'])
                that.population_data.household.households.push(parseFloat(result[i]['households']))
                that.population_data.household.year.push(result[i]['year'])
                that.population_data.perhousehold.year.push(result[i]['year'])
                that.population_data.perhousehold.per_data.push(parseFloat(result[i]['average_person_per_household']))
                that.population_data.population_density.year.push(result[i]['year'])
                that.population_data.population_density.data.push(parseFloat(result[i]['population_density']))
                that.population_data.population_rate.data.push(parseFloat(result[i]['population_rate']))
                that.population_data.population_rate.year.push(result[i]['year'])
              }
            }
          })
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
    height: 250px;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
</style>
