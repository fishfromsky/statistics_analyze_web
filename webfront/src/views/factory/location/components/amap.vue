<template>
  <div>
    <div ref="map" class="map-container"></div>
    <div class="control-panel">
      <div class="button-list">
        <span>是否显示标签：</span>
        <el-switch v-model="labelstatus" @change="labelchange"></el-switch>
      </div>
    </div>
  </div>
</template>

<script>
import { getfactorylist } from "@/api/model";
import echarts from "echarts";
import shanghai from "./mapdata/shanghai.json";
echarts.registerMap("shanghai", shanghai);
export default {
  name: "amap",
  components: {},
  data() {
    return {
      bmap: {},
      mapZoom: 10,
      chart: echarts.ECharts,
      data0: [], // 其他
      data1: [], //焚烧厂
      data2: [], //填埋场
      data3: [], 
      data4: [],
      geoCoordMap: {},
      labelstatus: false,
      centrl_geo: [121.477665, 31.226048],
      zoom: 1.2,
    };
  },
  methods: {
    labelchange: function () {
      this.initChart();
    },
    convertData(data) {
      var res = [];
      for (var i = 0; i < data.length; i++) {
        var geoCoord = this.geoCoordMap[data[i].name];
        if (geoCoord) {
          res.push({
            name: data[i].name,
            value: geoCoord.concat(data[i].value),
          });
        }
      }
      return res;
    },
    getData() {
      var that = this;
      getfactorylist().then((res) => {
        if (res.code === 20000) {
          let fac_data = res.data;
          for (let i = 0; i < fac_data.length; i++) {
            let f_name = fac_data[i]["name"];
            let f_value = fac_data[i]["deal"];
            let f_longitude = fac_data[i]["longitude"];
            let f_latitude = fac_data[i]["latitude"];
            if (fac_data[i]["typeId"] === 0) {
              that.data0.push({ name: f_name, value: f_value });
            } else if (fac_data[i]["typeId"] === 1) {
              that.data1.push({ name: f_name, value: f_value });
            } else if (fac_data[i]["typeId"] === 2) {
              that.data2.push({ name: f_name, value: f_value });
            } else if (fac_data[i]["typeId"] === 3){
              that.data3.push({ name: f_name, value: f_value });
            } else if (fac_data[i]["typeId"] === 4){
              that.data4.push({ name: f_name, value: f_value });
            } 
            that.geoCoordMap[f_name] = [f_longitude, f_latitude];
          }
          that.initChart();
        }
      });
    },
    initChart() {
      let img = new Image();
      img.src = "@/views/image/factory_bg.jpg";
      img.width = "100%";
      img.height = "100%";
      this.chart = echarts.init(this.$refs.map);
      this.chart.setOption({
        title: {
          text: "上海市无害化固废垃圾处理厂信息",
          subtext: "截至2019年数据",
          textStyle: {
            color: "#fff",
          },
          left: "20",
          top: "20",
        },
        legend:{
            data: ['其他(万吨)', '填埋厂', '焚烧场', '预处理+厌氧处理', '预处理+好氧处理'],
            top: '100',
            right: '20',
            textStyle: {
                color: '#fff'
            },
            orient: 'vertical'
        },
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
        // backgroundColor: "#013954",
        geo: {
          map: "shanghai",
          zoom: this.zoom,
          center: this.centrl_geo,
          label: {
            emphasis: {
              show: true,
              textStyle: {
                color: "#fff",
              },
            },
          },
          roam: true, //是否允许缩放
          itemStyle: {
            normal: {
              color: "#101f32", //地图背景色
              borderColor: "#43d0d6", //省市边界线
              borderWidth: 1.1,
            },
            emphasis: {
              color: "#43d0d6", //悬浮背景
            },
          },
        },
        series: [
          {
            name: "其他(万吨)",
            type: "effectScatter",
            coordinateSystem: "geo",
            data: this.convertData(this.data0),
            encode: {
              value: 2,
            },
            symbolSize: function (val) {
              return val[2] / 200;
            },
            rippleEffect: {
              brushType: "stroke",
              period: 2, //特效动画时长
              scale: 3, //波纹的最大缩放比例
            },
            hoverAnimation: true,
            label: {
              formatter: "{b}",
              position: "right",
              show: this.labelstatus,
            },
            itemStyle: {
              color: "#f4e925",
              shadowBlur: 10,
              shadowColor: "#333",
            },
            zlevel: 1,
          },
          {
            name: "填埋厂",
            type: "effectScatter",
            coordinateSystem: "geo",
            data: this.convertData(this.data1),
            encode: {
              value: 2,
            },
            symbolSize: function (val) {
              return val[2] / 200;
            },
            rippleEffect: {
              brushType: "stroke",
              period: 2, //特效动画时长
              scale: 3, //波纹的最大缩放比例
            },
            hoverAnimation: true,
            label: {
              formatter: "{b}",
              position: "top",
              show: this.labelstatus,
            },
            itemStyle: {
              color: "#ff33cc",
              shadowBlur: 10,
              shadowColor: "#333",
            },
            zlevel: 1,
          },
          {
            name: "焚烧场",
            type: "effectScatter",
            coordinateSystem: "geo",
            data: this.convertData(this.data2),
            encode: {
              value: 2,
            },
            symbolSize: function (val) {
              return val[2] / 200;
            },
            rippleEffect: {
              brushType: "stroke",
              period: 2, //特效动画时长
              scale: 3, //波纹的最大缩放比例
            },
            hoverAnimation: true,
            label: {
              formatter: "{b}",
              position: "top",
              show: this.labelstatus,
            },
            itemStyle: {
              color: "#00ff00",
              shadowBlur: 10,
              shadowColor: "#333",
            },
            zlevel: 1,
          },
          {
            name: "预处理+厌氧处理",
            type: "effectScatter",
            coordinateSystem: "geo",
            data: this.convertData(this.data3),
            encode: {
              value: 2,
            },
            symbolSize: function (val) {
              return val[2] / 200;
            },
            rippleEffect: {
              brushType: "stroke",
              period: 2, //特效动画时长
              scale: 3, //波纹的最大缩放比例
            },
            hoverAnimation: true,
            label: {
              formatter: "{b}",
              position: "top",
              show: this.labelstatus,
            },
            itemStyle: {
              color: "#C6E2FF",
              shadowBlur: 10,
              shadowColor: "#333",
            },
            zlevel: 1,
          },
          {
            name: "预处理+好氧处理",
            type: "effectScatter",
            coordinateSystem: "geo",
            data: this.convertData(this.data4),
            encode: {
              value: 2,
            },
            symbolSize: function (val) {
              return val[2] / 200;
            },
            rippleEffect: {
              brushType: "stroke",
              period: 2, //特效动画时长
              scale: 3, //波纹的最大缩放比例
            },
            hoverAnimation: true,
            label: {
              formatter: "{b}",
              position: "top",
              show: this.labelstatus,
            },
            itemStyle: {
              color: "#ff0000",
              shadowBlur: 10,
              shadowColor: "#333",
            },
            zlevel: 1,
          },
        ],
      });
    },
  },
  mounted() {
    this.getData();
  },
};
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 95vh;
  background: url("../../../image/factory_bg.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}
.control-panel {
  width: 250px;
  height: 60px;
  position: absolute;
  top: 20px;
  right: 20px;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 100;
}
.button-list {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}
.button-list span {
  font-size: 15px;
  color: #fff;
}
</style>
