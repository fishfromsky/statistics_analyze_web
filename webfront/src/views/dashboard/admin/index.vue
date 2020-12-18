<template>
  <div class="inner index_tabs">
    <!--header-->
    <div class="header">
      <!-- <div class="school-badge"></div>
      <div class="college-badge"></div> -->
      <div class="bg_header">
        <img class="school-badge" src="../../image/badge.png" />
        <img class="college-badge" src="../../image/college.png" />
        <div class="fl t_title">
          <div class="header-title-text">上海市固废智慧管理与仿真决策平台</div>
        </div>
      </div>
    </div>
    <div>
      <div class="left_cage">
        <div
          class="dataAllBorder01 cage_cl"
          style="margin-top: 12% !important; height: 24%"
        >
          <!-- 空间分布 -->
          <el-row>
            <div class="main_title">
              <img src="../../image/t_1.png" alt="" />
              中转站可视化
            </div>
            <el-col :xs="48" :sm="48" :lg="24">
              <visit-chart :chart-data="lineChartData" style="height: 30vh" />
            </el-col>
          </el-row>
        </div>
        <div
          class="dataAllBorder01 cage_cl"
          style="margin-top: 12% !important; height: 24%"
        >
          <!-- 生活垃圾产量预测 -->
          <el-row>
            <div class="main_title">
              <img src="../../image/t_1.png" alt="" />
              生活垃圾产量预测
            </div>
            <el-col :xs="48" :sm="48" :lg="24">
              <model-visit style="height: 30vh" />
            </el-col>
          </el-row>
        </div>
      </div>
      <div class="center_cage">
        <div
          class="dataAllBorder02"
          style="
            position: relative;
            overflow: hidden;
            height: 70vh;
            margin-top: 3% !important;
          "
        >
          <!--标题栏-->
          <div class="map_title_box" style="height: 6%">
            <div class="map_title_innerbox">
              <div class="map_title">集散厂优化动图</div>
            </div>
            <div
              id="map"
              v-loading="map_loading"
              element-loading-background="rgba(0, 0, 0, 0.5)"
              element-loading-text="加载中，请稍后"
              style="width: 100%; height: 70vh"
            ></div>
          </div>

          <div class="select-box">
            <el-input
              type="number"
              placeholder="输入p值"
              v-model="selectP"
            ></el-input>
            <el-button class="confirm-btn" @click="selectConfirm"
              >确定</el-button
            >
          </div>
        </div>
      </div>

      <div class="left_cage">
        <div
          class="dataAllBorder01 cage_cl"
          style="margin-top: 12% !important; height: 24%"
        >
          <!-- 人口网格图-->
          <el-row>
            <div class="main_title">
              <img src="../../image/t_1.png" alt="" />
              无害化处理厂可视化
            </div>
            <el-col :xs="48" :sm="48" :lg="24">
              <bar-chart style="height: 30vh"/>
            </el-col>
          </el-row>
        </div>
        <div
          class="dataAllBorder01 cage_cl"
          style="margin-top: 12% !important; height: 24%"
        >
          <!-- 固废产量网格图 -->
          <el-row>
            <div class="main_title">
              <img src="../../image/t_1.png" alt="" />
              人口网格图
            </div>
            <el-col :xs="48" :sm="48" :lg="24">
              <model-kind style="height: 30vh" />
            </el-col>
          </el-row>
        </div>
      </div>
    </div>

    <div
      style="
        width: calc(100% - 20px);
        height: 35vh;
        margin: 10px;
        display: flex;
        flex-direction: row;
      "
    >
      <div
        class="dataAllBorder01 cage_cl"
        style="height: 100%; position: relative; margin: 5px; overflow: hidden"
      >
        <div class="message_scroll_box">
          <div class="message_scroll">
            <div class="scroll_top">
              <span class="scroll_title">空气污染爬虫数据</span>
              <span class="scroll_level">一级</span>
              <a class="localize"></a>
              <span class="scroll_timer">20-10-20/9:52</span>
            </div>
            <div style="height: 25vh; width: 100%">
              <el-scrollbar style="height: 100%">
                <div v-for="item in spiderlist" :key="item.id" class="scroll-item-box">
                  <div class="scroll-item-innerbox" v-if="item.index%2==0">
                    <span>{{item.date}}</span>
                    <span style="margin-left: 10px">{{item.time}}</span>
                    <span class="crawldata-download">下载</span>
                  </div>
                  <div class="scroll-item-innerbox newText" v-else>
                    <span>{{item.date}}</span>
                    <span style="margin-left: 10px">{{item.time}}</span>
                    <span class="crawldata-download">下载</span>
                  </div>
                </div>
              </el-scrollbar>
            </div>
            <!-- <div class="msg_cage">
              <a class="localize_title">下载大量数据</a>
            </div>
            <div class="msg_cage">
              <a class="localize_msg">xxx资源网站</a>
            </div> -->
          </div>
        </div>
      </div>

      <div
        class="dataAllBorder01 cage_cl"
        style="height: 100%; position: relative; margin: 5px"
      >
        <!--标题栏-->
        <div style="height: 30px">
          <span class="scroll_title">政策新闻</span>
        </div>

        <div style="min-height: 190px; width: 100%; font-size: 13px; color: white">
          <div class="newText news-title">
            <a
              href="http://lhsr.sh.gov.cn/srgl/20180515/0039-C94EEFE3-34F0-4450-B0AB-1107E0AF9D87.html"
            >
              上海市生活垃圾全程分类体系建设行动计划（2018-2020年）
            </a>
          </div>
          <div style="margin-bottom: 5px" class="news-title">
            <a
              href="http://lhsr.sh.gov.cn/gggs/20190219/0039-E2825314-7F1A-4D9D-9FA5-5C70894C2776.html"
            >
              上海市生活垃圾管理条例
            </a>
          </div>
          <div class="newText news-title">
            <a href="http://www.sh.xinhuanet.com/2020-07/02/c_139183140.html">
              上海：九成居民区垃圾分类已达标 年底基本实现原生生活垃圾零填埋
            </a>
          </div>
          <div style="margin-bottom: 5px" class="news-title">
            <a href="http://www.sh.xinhuanet.com/2020-07/02/c_139183140.html">
              上海：九成居民区垃圾分类已达标 年底基本实现原生生活垃圾零填埋
            </a>
          </div>
          <div class="newText news-title">
            <a href="http://www.chinanews.com/sh/2020/10-11/9309877.shtml">
              新闻调查丨上海垃圾分类，前端的努力如何不被浪费？后端怎么处理？
            </a>
          </div>
          <div style="margin-bottom: 5px" class="news-title">
            <a href="https://news.sjtu.edu.cn/mtjj/20190713/107281.html">
              上海市生活垃圾分类立法实施现状解读及建议
            </a>
          </div>
          <div class="newText news-title">
            <a href="https://www.thepaper.cn/newsDetail_forward_9681877">
              上海虹口垃圾分类大数据接入一网统管，无人清扫机有望上路
            </a>
          </div>
        </div>
      </div>

      <div
        class="dataAllBorder01 cage_cl"
        style="height: 100%; position: relative; margin: 5px"
      >
        <!-- 天气 -->
        <div id="weather-v2-plugin-standard"></div>
        <!-- 访问人数 -->
        <div>
          <el-col :xs="36" :sm="36" :lg="18" class="card-panel-card">
            <div class="card-panel">
              <div class="card-panel-icon-wrapper icon-people">
                <svg-icon icon-class="peoples" class-name="card-panel-icon" />
              </div>
              <div class="card-panel-description">
                <div class="card-panel-text">今日访问数量 534</div>
                <count-to
                  :start-val="0"
                  :end-val="632"
                  :duration="2600"
                  class="card-panel-num"
                />
              </div>
            </div>
          </el-col>
        </div>
        <!-- 友情链接 -->
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
import { mapGetters } from "vuex";
import CountTo from 'vue-count-to'
import { getCrawlDataRecord } from '@/api/model'
import PanelGroup from "./components/PanelGroup";
import VisitChart from "./components/VisitChart";
import ModelVisit from "./components/ModelVisit";
import ModelKind from "./components/ModelKind";
import Student from "./components/Student";
import BarChart from "./components/BarChart";

const lineChartData = {
  newVisitis: {
    expectedData: [519, 387, 489, 598, 578, 409, 632],
    actualData: [120, 82, 91, 154, 162, 140, 128],
  },
  modelVisits: {
    expectedData: [12, 43, 23, 65, 34, 24, 34],
    actualData: [4, 3, 2, 6, 4, 5, 9],
  },
  modelkind: [
    { value: 3, name: "微粒扬尘模型" },
    { value: 2, name: "海洋洋流模型" },
    { value: 1, name: "大气环流模型" },
    { value: 2, name: "冷空气锋面模型" },
    { value: 1, name: "热流传导模型" },
  ],
  student: [
    { value: 34, name: "2018级" },
    { value: 62, name: "2017级" },
    { value: 24, name: "2016级" },
    { value: 8, name: "2015级" },
  ],
  barchart: {
    model1: [12, 7, 3, 5, 10, 12, 10],
    model2: [10, 8, 6, 3, 8, 12, 11],
    model3: [9, 4, 6, 13, 4, 5, 12],
  },
};

//地图
import echarts from "echarts";
import shanghai from "../../repository/p_median/test/mapdata/shanghai.json";
echarts.registerMap("shanghai", shanghai);
import { fetchall_list } from "@/api/app01/utputallocation";

export default {
  name: "Dashboard",

  components: {
    ModelKind,
    PanelGroup,
    VisitChart,
    ModelVisit,
    Student,
    BarChart
  },
  data() {
    return {
      lineChartData: lineChartData.newVisitis,
      modelChartData: lineChartData.modelVisits,
      modelKindData: lineChartData.modelkind,
      studentData: lineChartData.student,
      barchart: lineChartData.barchart,
      map_loading: false,
      project_id: "p001",
      chinaGeoCoordMap: {},
      chinaDatas: [],
      series: [],
      centrl_geo: [121.477665, 31.226048],
      zoom: 1.2,
      selectP: 6,
      chart: null,
      max_deal: null,
      min_deal: null,
      spiderlist: []
    };
  },
  computed: {
    ...mapGetters(["name"]),
    option: function () {
      return {
        tooltip: {
          trigger: "item",
          backgroundColor: " rgba(0, 161, 255, 0.4)",
          borderColor: "#00faff",
          showDelay: 0,
          hideDelay: 0,
          enterable: true,
          transitionDuration: 0,
          extraCssText: "z-index:100",
          formatter: function (params, ticket, callback) {
            //根据业务自己拓展要显示的内容
            var res = "";
            if (params.componentSubType === "effectScatter") {
              var name = params.data.name;
              var value = params.data.value[2];
              res =
                "<span style='color:#fff;'>" +
                name +
                "</span><br/>数据：" +
                value;
            } else {
              var value = params.data.value;
              res = "<span style='color:#fff;'>p值" + value + "</span>";
            }
            return res;
          },
        },
        backgroundColor: "",
        geo: {
          map: "shanghai",
          zoom: this.zoom,
          center: this.centrl_geo,
          label: {
            emphasis: {
              show: false,
            },
          },
          roam: true, //是否允许缩放
          itemStyle: {
            normal: {
              color: "rgba(51, 69, 89, .2)", //地图背景色

              shadowColor: "#00FFFF",
              shadowBlur: 10,

              borderColor: "#00FFFF", //省市边界线00fcff 516a89
              borderWidth: 1,
            },
            emphasis: {
              color: "rgba(17,204,204,.5)", //悬浮背景
            },
          },
        },
        series: this.series,
      };
    },
  },
  methods: {
    getCrawlData:function(){
      let that = this
      let datatype = '国内空气污染数据'
      getCrawlDataRecord(datatype).then(res=>{
        if (res.code === 20000){
          let result = res.data
          for (let i=0; i<result.length; i++){
            let dict = {}
            dict['time'] = result[i].time
            dict['date'] = result[i].date
            dict['index'] = i
            that.spiderlist.push(dict)
          }
        }
      })
    },
    controlSeries: function (centrl, centrl_geo) {
      let that = this;
      [[centrl.name, that.chinaDatas]].forEach(function (item, i) {
        that.series.push(
          {
            type: "lines",
            zlevel: 2,
            effect: {
              show: true,
              period: 2, //箭头指向速度，值越小速度越快
              trailLength: 0.01, //特效尾迹长度[0,1]值越大，尾迹越长重
              symbol: "arrow", //箭头图标
              symbolSize: 4, //图标大小
            },
            lineStyle: {
              normal: {
                width: 0.5, //尾迹线条宽度
                opacity: 1, //尾迹线条透明度
                curveness: 0.2, //尾迹线条曲直度
                color: "#33ffff", // 飞线颜色
              },
            },
            data: that.convertData(item[1], centrl_geo),
          },
          {
            type: "effectScatter",
            coordinateSystem: "geo",
            zlevel: 2,
            rippleEffect: {
              //涟漪特效
              period: 4, //动画时间，值越小速度越快
              brushType: "stroke", //波纹绘制方式 stroke, fill
              scale: 4, //波纹圆环最大限制，值越大波纹越大
            },
            label: {
              normal: {
                show: false,
                position: "right", //显示位置
                offset: [5, 0], //偏移设置
                formatter: function (params) {
                  //圆环显示文字
                  return params.data.name;
                },
                fontSize: 13,
              },
              emphasis: {
                show: true,
              },
            },
            symbol: "circle",
            symbolSize: function (val) {
              return 1; //圆环大小
            },
            itemStyle: {
              normal: {
                show: false,
                color: "#FF8C00",
              },
            },
            data: item[1].map(function (dataItem) {
              return {
                //在这里定义你所要展示的数据
                name: dataItem[0].name,
                value: that.chinaGeoCoordMap[dataItem[0].name].concat([
                  dataItem[0].value,
                ]),
              };
            }),
          },
          {
            type: "effectScatter",
            coordinateSystem: "geo",
            zlevel: 3,
            symbolSize: function (val) {
              return 5 + (val[2] * 10) / that.max_deal;
            },
            rippleEffect: {
              brushType: "stroke",
            },
            hoverAnimation: true,
            rippleEffect: {
              //涟漪特效
              period: 4,
              brushType: "stroke",
              scale: 4,
            },
            label: {
              formatter: "{b}",
              position: "right",
              show: true,
            },
            itemStyle: {
              color: "#ff3300",
              shadowBlur: 10,
              shadowColor: "#333",
            },
            data: [
              {
                name: item[0],
                value: that.chinaGeoCoordMap[item[0]].concat([centrl.value]),
              },
            ],
          }
        );
      });
    },
    isInArray: function (arr, value) {
      for (var i = 0; i < arr.length; i++) {
        if (value === arr[i]) {
          return true;
        }
      }
      return false;
    },
    selectConfirm: function () {
      this.map_loading = true;
      this.chinaGeoCoordMap = {};
      this.chinaDatas = [];
      this.series = [];
      let that = this;
      let data = {};
      data["project_id"] = this.project_id;
      data["p_value"] = this.selectP;
      fetchall_list(data).then((res) => {
        if (res.code === 20000) {
          let data = res.data;
          let rrc_list = [];
          let rrc_detail = [];
          that.max_deal = data[0].rrc_deal;
          that.min_deal = data[0].rrc_deal;
          for (let i = 0; i < data.length; i++) {
            if (!that.isInArray(rrc_list, data[i].rrc)) {
              rrc_list.push(data[i].rrc);
              rrc_detail.push(data[i]);
            }
            that.chinaGeoCoordMap[data[i].ts] = [
              data[i].ts_lng,
              data[i].ts_lat,
            ];
            if (data[i].rrc_deal > that.max_deal) {
              that.max_deal = data[i].rrc_deal;
            }
            if (data[i].rrc_deal < that.min_deal) {
              that.min_deal = data[i].rrc_deal;
            }
          }
          for (let i = 0; i < rrc_list.length; i++) {
            that.chinaDatas = [];
            for (let j = 0; j < data.length; j++) {
              if (data[j].rrc === rrc_list[i]) {
                that.chinaDatas.push([
                  { name: data[j].ts, value: data[j].p_value },
                ]);
              }
            }
            that.chinaGeoCoordMap[rrc_detail[i].rrc] = [
              rrc_detail[i].rrc_lng,
              rrc_detail[i].rrc_lat,
            ];
            that.chinaDatas.push([
              { name: rrc_detail[i].rrc, value: rrc_detail[i].p_value },
            ]);
            that.controlSeries(
              { name: rrc_detail[i].rrc, value: rrc_detail[i].rrc_deal },
              [rrc_detail[i].rrc_lng, rrc_detail[i].rrc_lat]
            );
          }
          that.chart.setOption(that.option);
          that.map_loading = false;
        } else if (res.code === 50000) {
          this.$message.error(res.message);
        }
      });
    },
    getList: function () {
      let data = {};
      data["project_id"] = this.project_id;
      fetchall_list(data).then((res) => {
        console.log(res);
      });
    },
    convertData: function (data, center) {
      var res = [];
      for (var i = 0; i < data.length; i++) {
        var dataItem = data[i];
        var fromCoord = this.chinaGeoCoordMap[dataItem[0].name];
        var toCoord = center; //中心点地理坐标
        if (fromCoord && toCoord) {
          res.push([
            {
              coord: fromCoord,
              value: dataItem[0].value,
            },
            {
              coord: toCoord,
            },
          ]);
        }
      }
      return res;
    },
  },
  mounted() {
    this.getCrawlData()
    // this.getList()
    this.chart = echarts.init(document.getElementById("map"));
    this.selectConfirm()
    window.WIDGET = {
      CONFIG: {
        layout: 1,
        width: "300",
        height: "90",
        background: 5,
        dataColor: "FFFFFF",
        borderRadius: 5,
        city: "CN101020100",
        key: "iqKbqsmVEE",
      },
    };
    (function (d) {
      var c = d.createElement("link");
      c.rel = "stylesheet";
      c.href =
        "https://apip.weatherdt.com/standard/static/css/weather-standard.css?v=2.0";
      var s = d.createElement("script");
      s.src =
        "https://apip.weatherdt.com/standard/static/js/weather-standard.js?v=2.0";
      var sn = d.getElementsByTagName("script")[0];
      sn.parentNode.insertBefore(c, sn);
      sn.parentNode.insertBefore(s, sn);
    })(document);
  },
};
</script>

<style lang="scss" scoped>
// 浏览人数
/deep/ .el-scrollbar__wrap{
  overflow-x: hidden;
}
.card-panel-col {
  margin-bottom: 32px;
}
.card-panel {
  height: 108px;
  cursor: pointer;
  font-size: 12px;
  position: relative;
  overflow: hidden;

  color: #666;
  // background: #fff;
  box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
  border-color: rgba(0, 0, 0, 0.05);
  &:hover {
    .card-panel-icon-wrapper {
      color: #fff;
    }
    .card-panel-num {
      font-size: 20px;
      color: #fff;
    }
    .icon-people {
      background: #40c9c6;
    }
    .card-panel-text {
      line-height: 18px;
      color: rgb(72, 202, 46);
      font-size: 16px;
      margin-bottom: 12px;
    }
  }
  .icon-people {
    color: #40c9c6;
  }
  .card-panel-icon-wrapper {
    float: left;
    margin: 14px 0 0 14px;
    padding: 16px;
    transition: all 0.38s ease-out;
    width: 60px;
    height: 60px;
    border: 1px solid #2b92d4;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    overflow: hidden;
    animation-timing-function: ease-in-out;
    animation-name: breathe;
    animation-duration: 1500ms;
    animation-iteration-count: infinite;
    animation-direction: alternate;
  }
  @keyframes breathe {
    0% {
      opacity: 0.4;
      box-shadow: 0 1px 2px rgba(0, 147, 223, 0.4),
        0 1px 1px rgba(0, 147, 223, 0.1) inset;
    }

    100% {
      opacity: 1;
      border: 1px solid rgba(59, 235, 235, 0.7);
      box-shadow: 0 1px 15px #0093df, 0 1px 10px #0093df inset;
    }
  }
  .card-panel-icon {
    float: left;
    font-size: 30px;
  }
  .card-panel-description {
    float: right;
    font-weight: bold;
    margin: 26px;
    margin-left: 0px;

    .card-panel-text {
      cursor: pointer;
      line-height: 18px;
      color: #1e90ff;
      font-size: 16px;
      margin-bottom: 12px;
    }

    .card-panel-num {
      font-size: 20px;
    }
  }
}
.newText {
  margin-bottom: 5px;
  background-color: #072951;
  box-shadow: -10px 0px 15px #2c58a6 inset,
    /*å·¦è¾¹é˜´å½±*/ 10px 0px 15px #2c58a6 inset;
  border-radius: 5%;
}
.news-title{
  display: flex;
  flex-direction: row;
  align-items: center;
  min-height: 3vh;
  font-size: 0.8vw;
}
.main_title {
  width: 200px;
  height: 30px;
  line-height: 33px;
  background-color: #2c58a6;
  border-radius: 18px;
  position: absolute;
  top: -30px;
  left: 50%;
  margin-left: -100px;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  box-sizing: border-box;
  text-align: center;
}
.main_title img {
  display: inline-block;
  vertical-align: middle;
  margin-left: -10px;
}
.t_title {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
/*header开始*/
.header {
  width: 100%;
  height: 10vh;
}
.header-title-text{
  color: #fff;
  font-size: 1.5vw;

}
.bg_header {
  position: relative;
  width: 100%;
  height: 10vh;
  background: url(../../image/title.png) no-repeat;
  background-size: 100% 100%;
  display: flex;
  flex-direction: row;
}

.school-badge {
  width: 11%;
  height: 9%;
  position: absolute;
  z-index: 100;
  margin-top: 5px;
  margin-left: 1%;
  background: url("../../image/badge.png");
  background-size: 100% 100%;
  background-position: center center;
  background-repeat: no-repeat;
}
.college-badge {
  width: 10%;
  height: 8%;
  position: absolute;
  z-index: 100;
  margin-top: 5px;
  margin-left: 12%;
  background: url("../../image/college.png");
  background-size: 100% 100%;
  background-position: center center;
  background-repeat: no-repeat;
}

.dashboard {
  &-container {
    width: 100%;
    height: 100%;
    min-height: calc(100vh - 50px);
    background-color: #080f3e;
    padding: 20px;

    top: 36px;
    bottom: 10px;
    left: 10px;
    right: 10px;
    padding: 10px 10px 0 10px;
    min-height: 500px;
    //background:url("../../image/wrapper-bg.png") no-repeat;
    background-color: #0b0f34;
    background-size: 100% 100%;
    box-sizing: border-box;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.inner {
  height: 100%;
}
.index_tabs {
  float: left;
  width: 100%;
  background-color: #080f3e;
  background: url("../../image/true.png");
  background-size: 100% 100%;
  background-position: center center;
  background-repeat: no-repeat;
}
.chart-wrapper {
  //子组件框
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
  background-color: rgba(0, 161, 255, 0.1);
  padding: 16px 16px 0;
  margin-bottom: 32px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);

  border: 2px solid #00a1ff;
  border-radius: 8px;
}
.wrapper {
  position: absolute;
  top: 36px;
  bottom: 10px;
  left: 10px;
  right: 10px;
  padding: 10px 10px 0 10px;
  min-height: 500px;

  background-size: 100% 100%;
  box-sizing: border-box;
}
.dataAllBorder01 {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  border: 1px #0174f5 solid;
  padding: 1px;
  box-sizing: border-box;
}
.dataAllBorder02 {
  width: 100%;
  height: 40%;
  box-sizing: border-box;
  border-radius: 10px;
  border: 1px solid #2c58a6;
  position: relative;
  box-shadow: 0 0 10px #2c58a6;
}
.cage_cl {
  background-color: rgba(2, 8, 23, 0.1);
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
  background-color: rgba(0, 161, 255, 0.1);
  padding: 16px 16px 0;
  margin-bottom: 32px;
  box-shadow: 0px 0px 10px #4788fb;

  border: 2px solid #00a1ff;
  border-radius: 8px;
}
.left_cage {
  width: 22%;
  height: 100%;
  margin-left: 0.3%;
  float: left;
}
.center_cage {
  width: 55.1%;
  height: 100%;
  margin-left: 0.3%;
  float: left;
}
.right_cage {
  width: 22%;
  height: 100%;
  margin-left: 0.3%;
  float: right;
}
.message_scroll {
  border: rgba(12, 122, 200, 0.5) 1px solid;
  background-color: rgba(20, 66, 125, 0.12);
  min-height: 10vh;
  cursor: pointer;
  margin-bottom: 6px;
  padding-left: 10px;
  padding-right: 10px;
}
.scroll_top {
  height: 5vh;
}
.scroll_title {
  float: left;
  background-image: url("../../image/pushmessage_class.png");
  background-repeat: no-repeat;
  width: 150px;
  line-height: 25px;
  color: white;
  font-size: 14px;
  text-align: center;
}
.scroll_level {
  float: left;
  background-repeat: no-repeat;
  line-height: 25px;
  width: 56px;
  background-position-y: 3px;
  color: white;
  font-size: 12px;
  text-align: center;
  margin-left: 8px;
}

.localize {
  display: block;
  line-height: 25px;
  margin-left: 8px;
  background-image: url("../../image/pushmessage_localize_01.png");
  background-repeat: no-repeat;
  background-position-y: 3px;
  width: 14px;
  height: 25px;
  float: left;
}
.localize:hover {
  background-image: url("../../image/pushmessage_localize_02.png");
}
.scroll_timer {
  color: #4a97da;
  font-size: 12px;
  line-height: 25px;
  text-align: right;
  display: block;
  float: right;
  margin-right: 5px;
}
.msg_cage {
  padding-left: 10px;
  padding-right: 6px;
  height: 18px;
  overflow: hidden;
  margin-top: 8px;
}
.localize_title {
  color: #2c85d2;
}
.localize_msg {
  font-size: 14px;
  color: white;
}
.scroll_box {
  height: 4vh;
  width: 100%;
  position: absolute;
  bottom: 0;
  padding-left: 3px;
  padding-right: 3px;
  padding-bottom: 2px;
  border-radius: 0px 0px 15px 15px;
  overflow: hidden;
  opacity: 0;
}
.scroll_tool_box {
  height: 100%;
  width: 100%;
  background-color: rgba(6, 10, 19, 0.9);
}
.scroll_tool {
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

.map_title_box {
  height: 11%;
  width: 100%;
  top: 0px;
  left: 0px;
  background-color: rgba(17, 25, 69, 0.1);
  border-radius: 11px 11px 0px 0px;
  position: relative;
}
.map_title_innerbox {
  position: absolute;
  top: 0px;
  width: 100%;
}
.map_title {
  width: 358px;
  background-image: url("../../image/first_title.png");
  background-repeat: no-repeat;
  margin: auto;
  height: 28px;
  text-align: center;
  color: white;
  font-size: 14px;
  font-family: "Microsoft YaHei";
  font-weight: bold;
}
//地图的css
.select-box {
  position: absolute;
  z-index: 100;
  width: 200px;
  height: 150px;
  border: #00faff solid 1px;
  margin-left: 20px;
  margin-top: 20px;
  padding: 10px;
}
/deep/ .el-input__inner {
  background-color: rgba(0, 161, 255, 0.2);
  border: #00a1ff 1px solid;
  color: #00faff;
  height: 25px;
}
.confirm-btn {
  height: 35px;
  margin-top: 20px;
  background: rgba(0, 161, 255, 0.2);
  color: #00faff;
  border: #00a1ff 1px solid;
}
.scroll-item{
  width: 100%;
  height: 30vh;
}
.scroll-item-box{
  width: 100%;
  height: 30px;
}
.scroll-item-box span{
  color: #fff;
  font-size: 0.8vw;
}
.scroll-item-innerbox{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.crawldata-download{
  position: absolute;
  right: 20px
}
</style>
