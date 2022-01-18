<style scoped>
h2 {
  text-align: center;
  padding: 30px;
  font-size: 18px;
}
#emission {
  width: 100%;
  height: 550px;
  border: 1px solid #344b58;
  margin: 0 auto;
}
</style>
<template>
  <div>
    <div id="emission"></div>
  </div>
</template>
 
<script>
import echarts from 'echarts'
import resize from './mixins/resize'
export default {
  name: "PROEMISSION",
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
    return {
      chartData
    }
  },
  watch:{
     chartData: {
        deep: true,
        handler(val) {
        this.setOptions(val)
                }
      }
  },
  mounted() {
    let this_ = this;
    let myChart = echarts.init(document.getElementById('emission'));
    var xData = function () {
      var data = [];
      for (var i = 2010; i < 2020; i++) {
        data.push(i + "年");
      }
      return data;
    }();
    let option = {
     
      "title": {
        "text": "温室气体排放-处理情况",
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
        "data": ['填埋排放','焚烧排放','焚烧净排','焚烧抵消', '生物排放', '生物净排', '生物抵消','总排放','总净排', '总抵消']
      },


      "calculable": true,
      "xAxis": [{
        "type": "category",
        "axisLine": {
          lineStyle: {
            color: '#90979c'
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
        "splitLine": {
          "show": false
        },
        "axisLine": {
          lineStyle: {
            color: '#90979c'
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
        "name": "填埋排放",
        "type": "bar",
        "barMaxWidth": 35,
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
        "data": [
            142.023,
            148.913,
            155.552,
            155.256,
            158.982,
            169.912,
            175.587,
            178.118,
            173.210,
            161.996
        ],
      },
      //净排
        {
        "name": "生物净排",
        "type": "bar",
        "barMaxWidth": 35,
        "itemStyle": {
          "normal": {
            "color": "rgba(	60,179,113,1)",
            "label": {
              "show": true,
              "textStyle": {
                "color": "#fff"
              },
              "position": "inside",
              // formatter: function (p) {
              //   return p.value > 0 ? (p.value) : '';
              // }
            }
          }
        },
        "data": [
          -0.022,
          -0.052,
          -0.048,
          -0.033,
          -0.039,
          -0.043,
          -0.053,
          -0.066,
          -0.083,
          -0.110
        ],
      },
      
      {
        "name": "焚烧净排",
        "type": "bar",
        "itemStyle": {
          "normal": {
            "color": "#FF9966",
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
        "data": [
        5.051,
        5.667,
        7.814,
        10.103,
        11.620,
        13.465,
        16.087,
        18.453,
         22.207,
         26.426
        ]
      }, {
        "name": "总净排",
        "type": "line",
        symbolSize: 10,
        symbol: 'circle',
        "itemStyle": {
          "normal": {
            "color": "rgba(255,0,255,1)",
            "barBorderRadius": 0,
            "label": {
              "show": true,
              "position": "top",
              formatter: function (p) {
                return p.value > 0 ? (p.value) : '';
              }
            }
          }
        },
        "data": [
         147.052,
         154.527,
         163.318,
         165.326,
         170.563,
          183.333,
          191.621,
          196.505,
          195.334,
          188.312
        ]
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
 