<template>
  <div class="dashboard-container">
    <panel-group/>
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="12" style="margin-top: 50px;">
        <div class="chart-wrapper">
          <visit-chart :chart-data="lineChartData"/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12" style="margin-top: 50px;">
        <div class="chart-wrapper">
          <model-visit :chart-data="modelChartData"/>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <model-kind :chart-data="modelKindData"/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <student :chart-data="studentData"/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <bar-chart :chart-data="barchart"/>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import PanelGroup from './components/PanelGroup'
  import VisitChart from './components/VisitChart'
  import ModelVisit from './components/ModelVisit'
  import ModelKind from './components/ModelKind'
  import Student from './components/Student'
  import BarChart from './components/BarChart'

  const lineChartData = {
      newVisitis: {
          expectedData: [519, 387, 489, 598, 578, 409, 632],
          actualData: [120, 82, 91, 154, 162, 140, 128]
      },
      modelVisits:{
          expectedData:[12,43,23,65,34,24,34],
          actualData: [4,3,2,6,4,5,9]
      },
      modelkind:[
          {value:3, name:'微粒扬尘模型'},
          {value:2, name:'海洋洋流模型'},
          {value:1, name:'大气环流模型'},
          {value:2, name:'冷空气锋面模型'},
          {value:1, name:'热流传导模型'}
      ],
      student:[
          {value:34, name:'2018级'},
          {value:62, name:'2017级'},
          {value:24, name:'2016级'},
          {value:8, name:'2015级'}
      ],
      barchart:{
          model1:[12,7,3,5,10,12,10],
          model2:[10,8,6,3,8,12,11],
          model3:[9,4,6,13,4,5,12]
      }
  };

  export default {
      name: 'Dashboard',
      data(){
          return {
              lineChartData: lineChartData.newVisitis,
              modelChartData: lineChartData.modelVisits,
              modelKindData: lineChartData.modelkind,
              studentData: lineChartData.student,
              barchart: lineChartData.barchart
          }
      },
      components: {
          ModelKind,
          PanelGroup,
          VisitChart,
          ModelVisit,
          Student,
          BarChart
      },
      computed: {
          ...mapGetters([
              'name'
          ])
      }
  }
</script>

<style lang="scss" scoped>
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
