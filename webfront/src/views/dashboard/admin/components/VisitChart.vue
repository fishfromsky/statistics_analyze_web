<template>
  <div :class="className" :style="{ width: width, height: height }">
    <div ref="map" class="map-container"></div>
    <div class="control-panel">
      <div class="button-list">
        <el-switch v-model="labelstatus" @change="labelchange"></el-switch>
      </div>
    </div>
  </div>
</template>

<script>
import { gettransferfactory } from "@/api/model";
import echarts from "echarts";
import shanghai from "./mapdata/shanghai.json";
import resize from "./mixins/resize";
echarts.registerMap("shanghai", shanghai);
export default {
  name: "amap",
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: "chart",
    },
    width: {
      type: String,
      default: "100%",
    },
    height: {
      type: String,
      default: "300px",
    },
    autoResize: {
      type: Boolean,
      default: true,
    },
  },
  components: {},
  data() {
    return {
      bmap: {},
      mapZoom: 10,
      chart: echarts.ECharts,
      data: [],
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
      gettransferfactory().then((res) => {
        if (res.code === 20000) {
          let fac_data = res.data;
          for (let i = 0; i < fac_data.length; i++) {
            let f_name = fac_data[i]["name"];
            let f_capacity = fac_data[i]["capacity"];
            let f_longitude = fac_data[i]["longitude"];
            let f_latitude = fac_data[i]["latitude"];
            that.data.push({ name: f_name, value: f_capacity });
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
        legend: {
          data: ["中转站"],
          top: "100",
          right: "20",
          textStyle: {
            color: "#fff",
          },
          orient: "vertical",
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
            data: this.convertData(this.data),
            encode: {
              value: 2,
            },
            symbolSize: function (val) {
              return val[2] / 35;
            },
            rippleEffect: {
              brushType: "stroke",
              period: 3, //特效动画时长
              scale: 4, //波纹的最大缩放比例
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
  height: 100%;
}
.control-panel {
  width: 60px;
  height: 30px;
  position: absolute;
  top: 10px;
  right: 0;
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
  font-size: 10px;
  color: #fff;
}
</style>
