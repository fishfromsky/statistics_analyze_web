<template>

  <div class="dashboard-container">
        <div class="header">
    <h1 class="header-title">固废智慧管理</h1>
     </div>
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
.header {position:relative;height:40px;box-sizing:border-box;}
.header-title {
    margin:0;
    padding:0;
    text-align:center;
    font-size:20px;
    font-weight:400;
    color:	#00FFFF;
}
  .dashboard {
    &-container {
        
        width: 100%;
    min-height: calc(100vh - 50px);
    background-color: #080f3e;
    padding: 20px;

    top:36px;
    bottom:10px;
    left:10px;
    right:10px;
    padding:10px 10px 0 10px;
    min-height:500px;
    background:url("./wrapper-bg.png") no-repeat;
     background-color:#0b0f34;
    background-size:100% 100%;
    box-sizing:border-box;

    }
    &-text {
      font-size: 30px;
      line-height: 46px;
    }
  }
  .chart-wrapper{//子组件框
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
    padding: 16px 16px 0;
    margin-bottom: 32px;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
   
    border: 2px solid #00a1ff;
    border-radius: 8px;

    
  }
  .wrapper {
    position:absolute;
    top:36px;
    bottom:10px;
    left:10px;
    right:10px;
    padding:10px 10px 0 10px;
    min-height:500px;
  
    background-size:100% 100%;
    box-sizing:border-box;
}
</style>
