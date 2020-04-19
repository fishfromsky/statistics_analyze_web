<template>
  <div class="model-container">
    <model-header @event1="HandleChange($event)"></model-header>
    <div v-if="hasModel">
      <el-row :gutter="32" class="test-container">
        <el-col :xs="24" :sm="24" :lg="8">
          <div class="chart-wrapper">
            <model-params @event1="handleParams($event)" :model-index="ModelIndex"/>
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="16">
          <div class="chart-wrapper1">
            <model-detail :chart-data="ChartData" :model-index="ModelIndex"/>
          </div>
        </el-col>
      </el-row>
    </div>
    <div v-else>
      <div class="picture">
        <img class="gif" src="../../../src/assets/404_images/box.png">
      </div>
      <div class="title">请输入要进行模拟实验的模型编号~</div>
    </div>
  </div>
</template>

<script>
  import ModelHeader from './components/ModelHeader'
  import ModelParams from './components/ModelParams'
  import ModelDetail from './components/ModelDetail'
  export default {
    data() {
      return {
        ModelIndex:'',
        ChartData:[],
        hasModel: false,
        emptySrc:'../../../src/assets/404_images/404.png'
      }
    },
    components:{
      ModelHeader,
      ModelParams,
      ModelDetail
    },
    methods: {
      HandleChange:function (data) {
        this.ModelIndex = data;
        this.hasModel = true
      },
      handleParams:function (data) {
        this.ChartData = data
      }
    }
  }
</script>
<style scoped>
  .test-container{
    margin-top: 20px;
    margin-bottom: 32px;
  }
  .chart-wrapper{
   background: #fff;
   padding: 16px 16px 0;
   margin-bottom: 32px;
   box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
  .chart-wrapper1{
   background: #ddd;
   padding: 16px 16px 0;
   margin-bottom: 32px;
   box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
  }
  .picture{
    margin: 0 auto;
    margin-top: 100px;
    width: 400px;
    height: 300px;
  }
  .gif{
    width: 100%;
    height: 100%;
  }
  .title{
    width: 500px;
    text-align: center;
    margin: 0 auto;
    margin-top: 30px;
    font-size: 20px;
    color: #5a5e66;
  }
</style>

