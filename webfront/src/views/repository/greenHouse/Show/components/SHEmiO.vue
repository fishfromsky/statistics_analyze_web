<style scoped>
h2 {
  text-align: center;
  padding: 30px;
  font-size: 18px;
}
#shemio {
  width: 100%;
  height: 550px;
  margin: 0 auto;

}
</style>
<template>
  <div>
    <div id="shemio"></div>
  </div>
</template>
 
<script>
import echarts from 'echarts'
import resize from './mixins/resize'
export default {
  name: "SHEMIO",
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '500px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {}
  },
  mounted() {
    let this_ = this;
    let myChart = echarts.init(document.getElementById('shemio'));
    var xData = function () {
      var data = [];
      for (var i = 2010; i < 2020; i++) {
        data.push(i + "年");
      }
      return data;
    }();
    let option = {
      
      "title": {
        "text": "上海温室气体排放-排放类别",
        x: "4%",

        textStyle: {
          color: '#fff',
          fontSize: '22'
        },
        subtextStyle: {
          color: '#90979c',
          fontSize: '16',

        },
      },
      "toolbox":{
        "feature":{
          "saveAsImage":{
            title:"保存为图片",
            show:true,
            "iconStyle":{
              color:'#7EE0D6',
               borderWidth :3
            },
            backgroundColor: "rgb(8, 15, 62)"
          },
          "magicType": {
            type: ['line', 'bar','stack']
                },  //切换为折线图，切换为柱状图
        }
      },
      "tooltip": {
        "trigger": "axis",
        "axisPointer": {
          "type": "shadow",
          textStyle: {
            color: "#fff"
          }
        },
      },
      "grid": {
        "borderWidth": 0,
        "top": 110,
        "bottom": 95,
        textStyle: {
          color: "#fff"
        }
      },
      "legend": {
        x: '4%',
        top: '8%',
        textStyle: {
          color: '#90979c',
        },
        "data": ['CO2净排','N2O净排','CH4净排']
      },


      "calculable": true,
      "xAxis": [{
        "type": "category",
        "axisLine": {
          lineStyle: {
            color: '#fff'
          }
        },
        "splitLine": {
          "show": false
        },
        "axisTick": {
          "show": false
        },
        "splitArea": {
          "show": false
        },
        "axisLabel": {
          "interval": 0,

        },
        "data": xData,
      }],
      "yAxis": [{
        "type": "value",
        "name": '单位：百万吨',
        "splitLine": {
          "show": false
        },
        "axisLine": {
          lineStyle: {
            color: '#fff'
          }
        },
        "axisTick": {
          "show": false
        },
        "axisLabel": {
          "interval": 0,

        },
        "splitArea": {
          "show": false
        },

      }],
      "dataZoom": [{
        "show": true,
        "height": 30,
        "xAxisIndex": [
          0
        ],
        bottom: 30,
        "start": 10,
        "end": 80,
        handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
        handleSize: '110%',
        handleStyle: {
          color: "#d3dee5",

        },
        textStyle: {
          color: "#fff"
        },
        borderColor: "#90979c"


      }, {
        "type": "inside",
        "show": true,
        "height": 15,
        "start": 1,
        "end": 35
      }],
      "series": [
      {
        "name": "CO2净排",
        "type": "bar",
        "itemStyle": {
          "normal": {
            "color": "rgba(65,105,225,1)",
            "label": {
              "show": true,
              "textStyle": {
                "color": "#fff"
              },
              "position": "inside",
              formatter: function (p) {
                return p.value > 0 ? (p.value) : '';
              }
            }
          }
        },
        "data": [1.7, 0.4, 2.0, 2.3, 3.6, 3.6, 3.7, 5.2, 5.3, 7.1],
      },
      {
        "name": "N2O净排",
        "type": "bar",

        "itemStyle": {
          "normal": {
            "color": "rgba(64,224,208,1)",
            "label": {
              "show": true,
              "textStyle": {
                "color": "#fff"
              },
              "position": "inside",
              formatter: function (p) {
                return p.value > 0 ? (p.value) : '';
              }
            }
          }
        },
        "data": [0.1, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3],
      },  
      {
        "name": "CH4净排",
        "type": "bar",
        "itemStyle": {
          "normal": {
            "color": "#FF6666",
            "barBorderRadius": 0,
            "label": {
              "show": true,
              "position": "inside",
              formatter: function (p) {
                return p.value > 0 ? (p.value) : '';
              }
            }
          }
        },
        "data": [6.2, 5.4, 5.8, 6.3, 4.9, 4.9, 4.9, 5.5, 5.8, 3.3]
      },
      ]
    };
    myChart.setOption(option);

    //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
    window.addEventListener('resize', function () { myChart.resize() });
  },
  methods: {
    setOptions(val) {
        console.log(val)
    }
  },
  created() {

  }
}
</script>
 