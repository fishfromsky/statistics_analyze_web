<style scoped>
h2 {
  text-align: center;
  padding: 30px;
  font-size: 18px;
}
#shemid {
  width: 100%;
  height: 550px;
  margin: 0 auto;
}
</style>
<template>
  <div>
    <div id="shemid"></div>
  </div>
</template>
 
<script>
import echarts from 'echarts'
import resize from './mixins/resize'
export default {
  name: "SHEMID",
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
    let myChart = echarts.init(document.getElementById('shemid'));
    var xData = function () {
      var data = [];
      for (var i = 2010; i < 2020; i++) {
        data.push(i + "年");
      }
      return data;
    }();
    let option = {
      "title": {
        "text": "上海温室气体排放处理情况",
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
        top: '6%',
        textStyle: {
          color: '#fff',
        },
        selected: { // 设置默认不显示
          '焚烧抵消': false,
          '焚烧净排': false,
          '生物净排': false,
          '生物抵消': false,
          '总净排': false,
        },
        "data": ['填埋排放', '焚烧排放', '焚烧净排', '焚烧抵消', '生物排放', '生物净排', '生物抵消', '总排放', '总净排', '总抵消']
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
        "nameLocation" : 'end',
        "splitLine": {
          "show": false
        },
        "nameLocation" :'end',
        "axisLine": {
          lineStyle: {
            color:  '#fff'
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
          "stack": "总量",
          "barMaxWidth": 35,
          "barGap": "10%",
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
          "data": [6, 5, 6, 6, 5, 5, 5, 5, 6, 3],
        },
        {
          "name": "生物排放",
          "type": "bar",
          "stack": "总量",
          "barMaxWidth": 35,
          "barGap": '-100%',
          "itemStyle": {
            "normal": {
              "color": "#006633",
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
          "data": [0.061, 0.022, 0.336, 0.219, 0.118, 0.097, 0.077, 0.036, 0.013, 0.122],
        },

        {
          "name": "焚烧排放",
          "type": "bar",
          "stack": "总量",
          "itemStyle": {
            "normal": {
              "color": "#FA4A59",
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
          "data": [0.9, 0.5, 0.8, 1.4, 2.0, 2.0, 2.2, 3.0, 3.2, 4.0]
        },
        {
          "name": "总排放",
          "type": "line",
          symbolSize: 15,
          symbol: 'circle',
          "itemStyle": {
            "normal": {
              "color": "#FAD24F",
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
          "data": [7.1, 5.9, 6.8, 7.8, 6.9, 7.0, 7.2, 8.5, 9.0, 7.3]
        },
        //净排
        {
          "name": "生物净排",
          "type": "bar",
          "stack": "总量",
          "barMaxWidth": 35,
          "barGap": '-100%',
          "itemStyle": {
            "normal": {
              "color": "#669933",
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
          "data": [-0.003, -0.001, -0.015, -0.01, -0.005, -0.004, -0.003, -0.002, -0.001, -0.005],
        },

        {
          "name": "焚烧净排",
          "type": "bar",
          "stack": "总量",
          "itemStyle": {
            "normal": {
              "color": "#FF7D5E",
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
          "data": [0.2, 0.1, 0.2, 0.4, 0.5, 0.5, 0.6, 0.8, 0.8, 1.1]
        }, {
          "name": "总净排",
          "type": "line",
          symbolSize: 15,
          symbol: 'rect',
          "itemStyle": {
            "normal": {
              "color": "#41FA82",
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
          "data": [6.4, 5.5, 5.8, 6.6, 5.4, 5.4, 5.5, 6.3, 6.7, 4.3]
        },
        //抵消
        {
          "name": "生物抵消",
          "type": "bar",
          "stack": "总量",
          "barMaxWidth": 35,
          "barGap": '-100%',
          "itemStyle": {
            "normal": {
              "color": "#99CC00",
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
          "data": [-0.063, -0.023, -0.35, -0.229, -0.123, -0.101, -0.08, -0.037, -0.013, -0.128],
        },

        {
          "name": "焚烧抵消",
          "type": "bar",
          "stack": "总量",
          "itemStyle": {
            "normal": {
              "color": "#E68372",
              "barBorderRadius": 0,
              "label": {
                "show": true,
                "position": "inside",
                // formatter: function (p) {
                //   return p.value > 0 ? (p.value) : '';
                // }
              }
            }
          },
          "data": [-0.6, -0.4, -0.6, -1.0, -1.4, -1.5, -1.6, -2.2, -2.3, -3.0] 
        }, {
          "name": "总抵消",
          "type": "line",
          symbolSize: 15,
          symbol: 'triangle',
          "itemStyle": {
            "normal": {
              "color": "#7ECBE0",
              "barBorderRadius": 0,
              "label": {
                "show": true,
                "position": "top",
                // formatter: function (p) {
                //   return p.value > 0 ? (p.value) : '';
                // }
              }
            }
          },
          "data": [-0.7, -0.4, -1.0, -1.3, -1.6, -1.6, -1.7, -2.2, -2.3, -3.1]
        },

      ]
    };
    myChart.setOption(option);

    //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。
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
 