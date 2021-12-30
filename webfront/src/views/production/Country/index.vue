<template>
  <div class="echarts">
    <div :style="{ height: '100vh', width: '100%' }" ref="myEchart"></div>
  </div>
</template>
<script>
import { getgarbagecountry } from '@/api/model'
import echarts from "echarts";
import $ from "jquery"
import "../../../../node_modules/echarts-gl/dist/echarts-gl.js";
import "../../../../node_modules/echarts/map/js/province/shanghai.js";

export default {
  name: "echarts",
  props: ["userJson"],
  data() {
    return {
      chart: null,
      datax: [],
      min: null,
      max: null
    };
  },
  mounted() {
    this.getData()
  },
  beforeDestroy() {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    getData:function(){
      let that = this
      this.datax = []
      this.min = null
      this.max = null
      getgarbagecountry().then(res=>{
        if (res.code === 20000){
          let result = res.data
          let min_val = parseFloat(result[0].production)
          let max_val = parseFloat(result[0].production)
          for (let i=0; i<result.length; i++){
            if (parseFloat(result[i].production) > max_val){
              max_val = result[i].production
            }
            if (parseFloat(result[i].production) < min_val){
              min_val = result[i].production
            }
            that.datax.push([result[i].longitude, result[i].latitude, parseFloat(result[i].production)])
          }
          that.min = min_val
          that.max = max_val
          that.chinaConfigure()
        }
      })
    },
    tipFormatter:function(params){
        var name = params.data[3];
        var value = params.data[4];
        let res =
          "<div class='div-tip'><span style='color:#fff;'>" +
          name +
          "</span><br/>数据：" +
          value+"</div>";
        return res
    },
    chinaConfigure() {
      let that = this
      let myChart = echarts.init(this.$refs.myEchart); //这里是为了获得容器所在位置
      window.onresize = myChart.resize;
      myChart.setOption({
        title:{
          text: '上海市2020年城镇固废产量',
          textStyle:{
            color: '#fff'
          },
          left: "20",
          top: "20",
        },
        visualMap: {
          type: 'continuous',
          min: parseInt(that.min),
          max: parseInt(that.max),
          bottom: 10,
          left: 10,
          range: [parseInt(that.min), parseInt(that.max)],
          inRange: {
            color: ['#AFEEEE', '#FAE900', '#F6AE00', '#C41A1A'],
            colorAlpha: [0.8, 0.9]
          },
          outOfRange: {
            color: ['rgba(0,0,0,0)'],
            opacity: 0
          }
        },
        // 进行相关配置
        backgroundColor: "rgba(0, 0, 0, 0)",
        tooltip: {
          trigger: "item",
          backgroundColor: "rgba(0, 161, 255, 0.5)",
          borderColor: "#00faff",
          showDelay: 0,
          hideDelay: 0,
          enterable: true,
          transitionDuration: 0,
          extraCssText: "z-index:100",
          formatter: function (params, ticket, callback) {
            //根据业务自己拓展要显示的内容
            return that.tipFormatter(params)
          },
        },
        geo3D: {
          map: "上海",
          shading: "lambert",
          regions: [
            {
              name: "黄浦区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "徐汇区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "长宁区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "静安区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "普陀区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "虹口区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "杨浦区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "闵行区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "宝山区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "嘉定区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "浦东新区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "金山区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "松江区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "青浦区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "奉贤区",
              itemStyle: {
                color: "#062031",
              },
            },
            {
              name: "崇明区",
              itemStyle: {
                color: "#062031",
              },
            },
          ],
          light: {
            main: {
              intensity: 4,
              shadow: true,
              shadowQuality: "low",
              alpha: 150,
              beta: 100,
            },
            ambient: {
              intensity: 0,
            },
          },
          viewControl: {
            distance: 130,
            panMouseButton: "left",
            rotateMouseButton: "right",
            alpha:40,
            center: [0,-30,0], // 视角中心点，旋转也会围绕这个中心点旋转，默认为[0,0,0]
          },
          groundPlane: {
            show: false,
            color: "#999",
          },
          postEffect: {
            enable: true,
            bloom: {
              enable: false,
            },
            SSAO: {
              radius: 1,
              intensity: 1,
              enable: true,
            },
            depthOfField: {
              enable: false,
              focalRange: 10,
              blurRadius: 10,
              fstop: 1,
            },
          },
          temporalSuperSampling: {
            enable: true,
          },
          itemStyle: {
            borderWidth: 1.5,
            borderColor: "#43D0D6",
          },
          regionHeight: 2,
        },
        series: [
          {
            type: "bar3D",
            coordinateSystem: "geo3D",
            shading: "lambert",
            data: that.datax,
            barSize: 0.8,
            minHeight: 0.2,
            // silent: true,
            itemStyle: {
              color: "#33ffff",
              opacity: 0.7,
            },
          },
        ],
      });
    },
  },
};
</script>

<style scoped>
.echarts{
  background: url('bg.png');
  background-position: center center;
  background-size: 100% 100%;
  background-repeat: no-repeat;
}
.div-tip{
  width: 80px;
  height: 50px;
  background: url("frame.png");
  background-repeat: no-repeat;
  background-size: 100% 100%;
  background-position: center center;
}
</style>
