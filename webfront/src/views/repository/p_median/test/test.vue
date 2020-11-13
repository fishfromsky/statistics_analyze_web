<template>
  <div>
    <div class="select-box">
      <el-input
        type="number"
        placeholder="输入p值"
        v-model="selectP"
      ></el-input>
      <el-button class="confirm-btn" @click="selectConfirm">确定</el-button>
    </div>
    <div
      v-loading="map_loading"
      element-loading-background="rgba(0, 0, 0, 0.5)"
      element-loading-text="加载中，请稍后"
      id="map"
      style="width: 100%; height: 95vh"
    ></div>
  </div>
</template>

<script>
import echarts from "echarts";
import shanghai from "./mapdata/shanghai.json";
echarts.registerMap("shanghai", shanghai);
import { fetchall_list } from "@/api/app01/utputallocation";
import da from 'element-ui/src/locale/lang/da';
export default {
  data() {
    return {
      map_loading: false,
      project_id: "p001",
      chinaGeoCoordMap: {},
      chinaDatas: [],
      series: [],
      centrl_geo: [121.477665, 31.226048],
      zoom: 1.2,
      selectP: "",
      selectRRC: "",
      chart: null,
      max_deal: null,
      min_deal: null
    };
  },
  computed: {
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
        backgroundColor: "#013954",
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
               color: '#062031',
                borderWidth: 1.1,
                borderColor: '#43D0D6'
            },
            emphasis: {
                areaColor: '#43D0D6'
            },
          },
        },
        series: this.series,
      };
    },
  },
  methods: {
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
                curveness: 0.3, //尾迹线条曲直度
                color:'#FFFF00',  // 飞线颜色
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
                return 5+(val[2]*10)/that.max_deal;
            },
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            rippleEffect: {
              //涟漪特效
              period: 4, 
              brushType: "stroke",
              scale: 4, 
            },
            label: {
                formatter: '{b}',
                position: 'right',
                show: true
            },
            itemStyle: {
                color: '#FF7F50',
                shadowBlur: 10,
                shadowColor: '#333'
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
          that.max_deal = data[0].rrc_deal
          that.min_deal = data[0].rrc_deal
          for (let i = 0; i < data.length; i++) {
            if (!that.isInArray(rrc_list, data[i].rrc)) {
              rrc_list.push(data[i].rrc);
              rrc_detail.push(data[i]);
            }
            that.chinaGeoCoordMap[data[i].ts] = [
              data[i].ts_lng,
              data[i].ts_lat,
            ];
            if (data[i].rrc_deal > that.max_deal){
                that.max_deal = data[i].rrc_deal
            }
            if (data[i].rrc_deal < that.min_deal){
                that.min_deal = data[i].rrc_deal
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
            that.controlSeries({name: rrc_detail[i].rrc, value: rrc_detail[i].rrc_deal}, [
              rrc_detail[i].rrc_lng,
              rrc_detail[i].rrc_lat,
            ]);
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
    // this.getList()
    this.chart = echarts.init(document.getElementById("map"));
    this.chart.setOption(this.option);
  },
};
</script>

<style scoped lang="scss">
.select-box {
  position: absolute;
  z-index: 100;
  width: 200px;
  height: 250px;
  border: #00faff solid 1px;
  margin-left: 20px;
  margin-top: 20px;
  padding: 10px;
}
/deep/ .el-input__inner {
  background-color: rgba(0, 161, 255, 0.2);
  border: #00a1ff 1px solid;
  color: #00faff;
}
.confirm-btn {
  margin-top: 20px;
  background: rgba(0, 161, 255, 0.2);
  color: #00faff;
  border: #00a1ff 1px solid;
}
</style>