<style scoped>
h2 {
  text-align: center;
  padding: 30px;
  font-size: 18px;
}
#emission {
  width: 100%;
  height: 550px;
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
  name: "EMISSION",
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
          }
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
          "data": [
            142,
            148,
            155,
            155,
            158,
            169,
            175,
            178,
            173,
            161,
          ],
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
          "data": [
            0.5,
            1.2,
            1.1,
            0.7,
            0.9,
            1.0,
            1.2,
            1.5,
            1.9,
            2.5
          ],
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
          "data": [
            18,
            21,
            29,
            37,
            43,
            50,
            60,
            69,
            83,
            99
          ]
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
          "data": [
            161,
            171,
            186,
            193,
            203,
            221,
            237,
            248,
            258,
            263
          ]
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
          "data": [
            -0.02,
            -0.05,
            -0.04,
            -0.03,
            -0.03,
            -0.04,
            -0.05,
            -0.06,
            -0.08,
            -0.11
          ],
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
          "data": [
            5,
            5,
            7,
            10,
            11,
            13,
            16,
            18,
            22,
            26
          ]
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
          "data": [
            147,
            154,
            163,
            165,
            170,
            183,
            191,
            196,
            195,
            188
          ]
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
              }
            }
          },
          "data": [
            -0.3,
            -1.0,
            -0.9,
            -0.6,
            -0.7,
            -0.8,
            -1.0,
            -1.5,
            -1.9,
            -2.6
          ],
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
          "data": [
            -13,
            -15,
            -21,
            -27,
            -31,
            -35,
            -42,
            -49,
            -58,
            -70
          ]
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
          "data": [
            -11,
            -13,
            -19,
            -24,
            -28,
            -34,
            -41,
            -47,
            -59,
            -71
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
 