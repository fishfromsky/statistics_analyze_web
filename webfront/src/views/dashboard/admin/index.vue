<template>
 
   <div class="inner index_tabs" style="height: 100%;">
        <div class="header">
            <img src="../../image/badge.png"  class="school-badge"/>
            <img src="../../image/college.png"  class="school-badge"/>
            <span class="header-title">上海市固废智慧管理与仿真决策平台</span>
        </div>
    <div class="left_cage">
         <div class="dataAllBorder01 cage_cl" style="margin-top: 9% !important; height: 24%;">
                   <!-- 空间分布 -->
            <el-row>
               <el-col :xs="48" :sm="48" :lg="24" >
              <visit-chart :chart-data="lineChartData"/>
              </el-col>
           </el-row>
          </div>
          <div class="dataAllBorder01 cage_cl" style="margin-top: 1.5% !important; height: 38%;">
               <div class="dataAllBorder02 "> <!-- 生活垃圾产量预测 -->
                <el-row>
                <el-col :xs="50" :sm="50" :lg="24">
                  <model-visit :chart-data="modelChartData"/> 
           </el-col>
           </el-row>
               </div>
          </div>
           <div class="dataAllBorder01 cage_cl" style="margin-top: 1.5% !important; height: 32%; position: relative;">
               <div class="dataAllBorder02" style="padding: 1.2%; overflow: hidden">
                        <div class="message_scroll_box">
                            <div class="message_scroll">
                            <div class="scroll_top">
                                <span class="scroll_title">爬虫数据</span>
                                <span class="scroll_level ">一级</span>
                                <a class="localize"></a>
                                <span class="scroll_timer">20-10-20/9:52</span>
                            </div>
                            <div class="msg_cage">
                                <a class="localize_title">下载大量数据</a>
                            </div>
                            <div class="msg_cage">
                                <a class="localize_msg">xxx资源网站</a>
                            </div>
                        </div>
                             <div class="message_scroll">
                            <div class="scroll_top">
                                <span class="scroll_title">爬虫数据</span>
                                <span class="scroll_level ">一级</span>
                                <a class="localize"></a>
                                <span class="scroll_timer">20-10-20/9:52</span>
                            </div>
                            <div class="msg_cage">
                                <a class="localize_title">下载大量数据</a>
                            </div>
                            <div class="msg_cage">
                                <a class="localize_msg">xxx资源网站</a>
                            </div>
                        </div>
                        </div>

                    </div>
                </div>
     </div>
         <div class="center_cage">
        <div class="dataAllBorder01 cage_cl" style="margin-top: 3.5% !important; height: 62.7%; position: relative;">
                    <div class="dataAllBorder02" style="position: relative; overflow: hidden;">
                        <!--标题栏-->
                        <div class="map_title_box" style="height: 6%">
                            <div class="map_title_innerbox">
                                <div class="map_title">实时地图</div>
                            </div>
                        </div>
                        <div style="height:710px ;width:100px"></div>
                    </div>
                      <div class="dataAllBorder02" style="position: relative; overflow: hidden;">
                        <!--标题栏-->
                        <div class="map_title_box" style="height: 6%">
                            <div class="map_title_innerbox">
                                <div class="map_title">政策新闻</div>
                                
                            </div>
                        </div>
                        <div style="height:200px ;width:100px"></div>
                    </div>
                        
                    </div>
        </div>

           <div class="left_cage">
         <div class="dataAllBorder01 cage_cl" style="margin-top: 9% !important; height: 24%;">
                   <!-- 空间分布 -->
            <el-row>
               <el-col :xs="48" :sm="48" :lg="24" >
              <visit-chart :chart-data="lineChartData"/>
              </el-col>
           </el-row>
          </div>
          <div class="dataAllBorder01 cage_cl" style="margin-top: 1.5% !important; height: 38%;">
               <div class="dataAllBorder02 "> <!-- 生活垃圾产量预测 -->
                <el-row>
                <el-col :xs="50" :sm="50" :lg="24">
                  <model-visit :chart-data="modelChartData"/> 
           </el-col>
           </el-row>
               </div>
          </div>
           <div class="dataAllBorder01 cage_cl" style="margin-top: 1.5% !important; height: 32%; position: relative;">
               <div class="dataAllBorder02" style="padding: 1.2%; overflow: hidden">
                   <!-- 天气 -->
                   <panel-group/>
                    </div>
                </div>
     </div>
     
     </div>
   
    <!-- <el-row :gutter="20">
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
    </el-row> -->

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
.header {
  position:relative;
  height:75px;
  display: flex;
  flex-direction: row;
  align-items: center;
  
}
.school-badge{
 width:100px;
 height:75px;

}
.header-title {
  margin-left: 30px;
    font-size:20px;
    font-weight:400;
    color:	#00FFFF;
}
  .dashboard {
    &-container {
      width: 100%;
      height: 100%;
      min-height: calc(100vh - 50px);
      background-color: #080f3e;
      padding: 20px;

    top:36px;
    bottom:10px;
    left:10px;
    right:10px;
    padding:10px 10px 0 10px;
    min-height:500px;
    //background:url("../../image/wrapper-bg.png") no-repeat;
    background-color:#0b0f34;
    background-size:100% 100%;
    box-sizing:border-box;

    }
    &-text {
      font-size: 30px;
      line-height: 46px;
    }
  }.inner{
    height: 100%;
}
.index_tabs{float: left;width: 100%;height: 24px; background-color: #080f3e;border-top-left-radius: 9px;border-top-right-radius: 9px}
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
.dataAllBorder01{
    width: 100%;
    height: 100%;
    border-radius: 10px;
    border: 1px #0174f5 solid;
    padding: 1px;
    box-sizing: border-box;
}
.dataAllBorder02{
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border:2px solid #016ae0;
    border-radius: 10px;
}
.cage_cl{
    background-color: rgba(2,8,23,0.1);
}
.left_cage{
    width: 22%;
    height: 100%;
    margin-left: 0.3%;
    float: left;
}
.center_cage{
    width: 55.1%;
    height: 100%;
    margin-left: 0.3%;
    float: left;
}
.right_cage{
    width: 22%;
    height: 100%;
    margin-left: 0.3%;
    float: right;
}
.message_scroll{
    border: rgba(12,122,200,0.5) 1px solid;
    background-color: rgba(20,66,125,0.12);
    height: 90px;
    cursor: pointer;
    margin-bottom: 6px;
}
.scroll_top{
    height: 25px;
}
.scroll_title{
    float: left;
    background-image: url("../../image/pushmessage_class.png");
    background-repeat: no-repeat;
    width: 150px;
    line-height: 25px;
    color: white;
    font-size: 14px;
    text-align: center;
}
.scroll_level{
    float: left;
    background-repeat: no-repeat;
    line-height: 25px;
    width: 56px;
    background-position-y:3px;
    color: white;
    font-size: 12px;
    text-align: center;
    margin-left: 8px;
}

.localize{
    display: block;
    line-height: 25px;
    margin-left: 8px;
    background-image: url("../../image/pushmessage_localize_01.png");
    background-repeat: no-repeat;
    background-position-y:3px;
    width: 14px;
    height: 25px;
    float: left;
}
.localize:hover{
    background-image: url("../../image/pushmessage_localize_02.png");
}
.scroll_timer{
    color: #4a97da;
    font-size: 12px;
    line-height: 25px;
    text-align: right;
    display: block;
    float: right;
    margin-right: 5px;
}
.msg_cage{
    padding-left: 10px;
    padding-right: 6px;
    height: 18px;
    overflow: hidden;
    margin-top: 8px;
}
.localize_title{
    color: #2c85d2;
}
.localize_msg{
    font-size: 14px;
    color: white;
}
.scroll_box{
    height: 30px;
    width: 100%;
    position: absolute;
    bottom: 0;
    padding-left: 3px;
    padding-right: 3px;
    padding-bottom: 2px;
    border-radius:0px 0px 15px 15px;
    overflow: hidden;
    opacity: 0;
}
.scroll_tool_box{
    height: 100%;
    width: 100%;
    background-color: rgba(6,10,19,0.9);
}
.scroll_tool{
    color: #28cfa2;
    border: #28cfa2 1px solid;
    line-height: 20px;
    width: 90px;
    text-align: center;
    display: block;
    float: right;
    border-radius: 3px;
    font-size: 12px;
    margin-top: 3px;
    margin-right: 8px;
    text-decoration: none;
}

.map_title_box{
    height: 11%;
    width: 100%;
    top: 0px;
    left: 0px;
    background-color: rgba(17,25,69,0.1);
    border-radius: 11px 11px 0px 0px;
    position: relative;
}
.map_title_innerbox{
    position: absolute;
    top: -4px;
    width: 100%;
}
.map_title{
    width: 358px;
    background-image: url("../../image/first_title.png");
    background-repeat: no-repeat;
    margin:auto;
    height: 28px;
    text-align: center;
    color: white;
    font-size: 14px;
    font-family: "Microsoft YaHei";
    font-weight: bold;
}
</style>
