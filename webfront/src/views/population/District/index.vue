<template>
    <div class="dashboard-container">
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="12">
                <el-select v-model="district_choose">
                    <el-option v-for="item in district_options" :key="item.label" :label="item.label" :value="item.value"></el-option>
                </el-select>
                <div class="chart-wrapper">
                    <district :chartData="DistrictInfo" style="height: 35vh"></district>
                </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper" style="margin-top: 60px">
                    <districtdensity :chartData="DistrictInfo" style="height: 35vh"></districtdensity>
                </div>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="12">
                <el-select v-model="choose_year">
                    <el-option v-for="item in year_option" :key="item" :label="item" :value="item"></el-option>
                </el-select>
                <div class="chart-wrapper">
                    <timepopulation :chartData="TimeInfo" style="height: 35vh"></timepopulation>
                </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <div class="chart-wrapper" style="margin-top: 60px">
                    <timedensity :chartData="TimeInfo" style="height: 35vh"></timedensity>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { filterlinepopulationdistrict, getdistrictpopulation, filterbarpopulationdistrict } from '@/api/model'
import district from './components/disitrict'
import districtdensity from './components/districtdensity'
import timepopulation from './components/timepopulation'
import timedensity from './components/timedensity'
export default {
  name: "index",
  components:{
      district,
      districtdensity,
      timepopulation,
      timedensity
  },
  data(){
      return{
          DistrictInfo: {
              district: '',
              year: [],
              population: [],
              population_density: []
          },
          TimeInfo:{
              district: [],
              population: [],
              population_density: []
          },
          year_option: [],
          choose_year: '2017',
          district_choose: '浦东新区',
          district_options: [
            { label: "黄浦区", value: "黄浦区" },
            { label: "普陀区", value: "普陀区" },
            { label: "静安区", value: "静安区" },
            { label: "长宁区", value: "长宁区" },
            { label: "徐汇区", value: "徐汇区" },
            { label: "虹口区", value: "虹口区" },
            { label: "杨浦区", value: "杨浦区" },
            { label: "宝山区", value: "宝山区" },
            { label: "嘉定区", value: "嘉定区" },
            { label: "闵行区", value: "闵行区" },
            { label: "浦东新区", value: "浦东新区" },
            { label: "金山区", value: "金山区" },
            { label: "松江区", value: "松江区" },
            { label: "青浦区", value: "青浦区" },
            { label: "崇明区", value: "崇明区" },
            { label: "奉贤区", value: "奉贤区" },
        ],
      }
  },
  watch:{
      district_choose(val){
          this.getLineData()
      },
      choose_year(val){
          this.getBarData()
      }
  },
  methods:{
      isInArray: function (arr, value) {
      for (var i = 0; i < arr.length; i++) {
        if (value === arr[i]) {
          return true;
        }
      }
      return false;
    },
      getLineData(){
          let that = this
          let data = {}
          data['district'] = this.district_choose
          if (this.DistrictInfo.year.length!=0){
              this.DistrictInfo.year = []
          }
          if (this.DistrictInfo.population.length!=0){
              this.DistrictInfo.population = []
          }
          if (this.DistrictInfo.population_density.length!=0){
              this.DistrictInfo.population_density = []
          }
          filterlinepopulationdistrict(data).then(res=>{
              if (res.code === 20000){
                  let result = res.data
                  result.sort(function(a, b){
                     return parseInt(a.year) > parseInt(b.year) ? 1:-1
                  })
                  for (let i=0; i<result.length; i++){
                      that.DistrictInfo.year.push(result[i]['year'])
                      that.DistrictInfo.population.push(parseFloat(result[i]['population']).toFixed(0))
                      that.DistrictInfo.population_density.push(parseFloat(result[i]['population_density']).toFixed(2))
                  }
                  that.DistrictInfo.district = that.district_choose
              }
          })
      },
      getYearData:function(){
          let that = this
          getdistrictpopulation().then(res=>{
              if (res.code === 20000){
                  let result = res.data
                  for (let i=0; i<result.length; i++){
                      if (!that.isInArray(that.year_option, result[i]['year'])){
                          that.year_option.push(result[i]['year'])
                      }
                  }
              }
          })
      },
      getBarData(){
          let that = this
          let data = {}
          data['year'] = this.choose_year
          if (this.TimeInfo.district.length!=0){
              this.TimeInfo.district = []
          }
          if (this.TimeInfo.population.length!=0){
              this.TimeInfo.population = []
          }
          if (this.TimeInfo.population_density.length!=0){
              this.TimeInfo.population_density = []
          }
          filterbarpopulationdistrict(data).then(res=>{
              if (res.code === 20000){
                  let result = res.data
                  for (let i=0; i<result.length; i++){
                      that.TimeInfo.district.push(result[i]['district'])
                      that.TimeInfo.population.push(parseFloat(result[i]['population']).toFixed(2))
                      that.TimeInfo.population_density.push(parseFloat(result[i]['population_density']).toFixed(2))
                  }
              }
          })
      }
  },
  mounted(){
      this.getLineData()
      this.getYearData()
      this.getBarData()
  }
};
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
.chart-wrapper {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
  margin-top: 20px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
</style>
