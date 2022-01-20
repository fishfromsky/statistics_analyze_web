<template>

        <div class="border">
        <div class="border_center">
        <div class="div_any_title">全国总排放分布地图</div>
         <div id="center_chart" ref="chart" style="width:100%;height:95%;display: inline-block;"></div>

        </div>
         <div class="border_right">
            <div class="div_any_title">各省份情况</div>
            <div id="proEmission" style="width: 100%;height: 60%;border: 1px solid #344b58;margin: 0 auto;"></div>
            <div id="proPie" style="width: 100%;height: 40%;border: 1px solid #344b58;margin: 0 auto;"></div>
        
        </div> 
      </div>      
            
     

</template>

<script src="echarts.min.js"></script>
<script>
import *as echarts from 'echarts';
import 'echarts/map/js/china.js'; // 引入中国地图数据
import proEmission from './components/proEmission.vue'
import mapdata from './map.js';
import prodata from './province.js';
import piedata from './pieData.js';


export default {
  name: 'NationMap',
  components: {
      proEmission,
          },
  data () {
    return {
    mapdata: {},
    provinceData:prodata,
    SelectPro:"各省份",
    update:false,
    bioNet:  [-0.02,-0.05,-0.04,-0.03,-0.03,-0.04,-0.05,-0.06,-0.08,-0.11],
    buryNet:[142,148,155,155,158,169,175,178,173,161],
    burnNet: [5,5,7,10,11,13,16,18,22,26],
    bioOut:[],
    buryOut:[],
    burnOut:[],
    center_chart:null,
    geoJson: {
        features: []
            },
    }
    },
    mounted(){
      this.showchart_center();
      this.showchart_right();
      this.showchart_right_bottom();
      this.getGeoJson(100000); // 获取全国地图
         },
  methods:{
dataUpdate(name){
    let that=this;
    console.log("使用dataUpdate"+name);
        that.update=false;
        for(var i=0;i<prodata.length;i++){
             if(prodata[i].province==name){
                that.bioNet=prodata[i].bio
                that.burnNet=prodata[i].burn
                that.buryNet=prodata[i].bury
            }
        }
        for(var i=0;i<piedata.length;i++){
             if(piedata[i].province==name){
                that.bioOut=piedata[i].bio
                that.burnOut=piedata[i].burn
                that.buryOut=piedata[i].bury
            }
        }
        that.SelectPro=name
        console.log(that.SelectPro)
        that.showchart_right();
        this.showchart_right_bottom();

},
showchart_center(){
var attr={
    'unitname':'总量',
    'unit':'百万吨'
       }
this.$echarts.registerMap('100000', this.geoJson); //注册
let chart = this.$echarts.init(this.$refs.chart);
let option={
    geo: {
            map: 'china',
            aspectScale: 0.75, //长宽比
            zoom: 1.1,
            roam: false,
            itemStyle: {
                normal: {
                    areaColor: {
                        type: 'radial',
                        x: 0.5,
                        y: 0.5,
                        r: 0.8,
                        colorStops: [{
                            offset: 0,
                            color: '#09132c' // 0% 处的颜色
                        }, {
                            offset: 1,
                            color: '#274d68' // 100% 处的颜色
                        }],
                        globalCoord: true // 缺省为 false
                    },
                    shadowColor: 'rgb(58,115,192)',
                    shadowOffsetX: 10,
                    shadowOffsetY: 11
                },
                emphasis: {
                    areaColor: '#66CDAA',
                    borderWidth: 0,
                    color: 'green',
                    label: {
                        show: false
                    }
                }
            },
            regions: [{
                name: '南海诸岛',
                itemStyle: {
                    areaColor: 'rgba(0, 10, 52, 1)',

                    borderColor: 'rgba(0, 10, 52, 1)',
                    normal: {
                        opacity: 0,
                        label: {
                            show: false,
                            color: "#009cc9",
                        }
                    }
                },


            }],
        },
    legend: {
        textStyle:{
          color:'white'
        },
    },
    tooltip:{
        trigger: 'item',
         formatter: function(param) {},
    },
    visualMap: {
        type: 'piecewise',
        left: '10%',
        top: '75%',
        min: 0,
        max: 10000, //根据后台最大数值确定
        splitNumber: 5,
        color: ['#BA55D3', '#e6ac53', '#00BFFF', '#40E0D0'] , //设置坐标点从小到大的颜色
        pieces: [{
                lte: 20,
                label: '<=2千万吨',
            },{
                gt:20,
                lte: 50,
                label: '2~5千万吨'
            },
            {
                gt:50,
                lte: 90,
                label: '5~9千万吨'
            },
            {
                gt: 90,
                label: '>9千万吨'
            },
        ],
        textStyle: {
            color: '#F8F8FF'
        },
        itemWidth: 20,
        itemHeight: 20,
    },
    
    series: [{
                type: 'map',
                roam: false,
                label: {
                    normal: {
                        show: true,
                        textStyle: {
                            color: '#FFFF00',
                            fontSize:16,
                            fontWeight:'bold'
                            
                        }
                    },
                },
                tooltip:{
                    formatter: function(param) {
                                return param.data.name+'<br>'+attr.unitname+':'+param.data.value+attr.unit
                            }
                },
                itemStyle: {
                    normal: {
                        borderColor: 'rgb(147, 235, 248)',
                        borderWidth: 0.6,
                        areaColor: {
                            type: 'radial',
                            x: 0.5,
                            y: 0.5,
                            r: 0.8,
                            colorStops: [{
                                offset: 0,
                                color: '#09132c' // 0% 处的颜色
                            }, {
                                offset: 1,
                                color: '#274d68' // 100% 处的颜色
                            }],
                            globalCoord: true // 缺省为 false
                        },
                    },
                    emphasis: {
                        areaColor: '#FFB6C1',
                        borderWidth: 0.1
                    }
                },
                zoom: 1.1,
                map: 'china', //使用
                 data:mapdata,
            }, 
        ]
};
    chart.setOption(option);   
    let that = this;  
	chart.on('click', function(params){
            that.SelectPro=params.name
            console.log("地图"+that.SelectPro)
			console.log(params);//此处写点击事件内容
            that.update=true;
            that.$options.methods.dataUpdate(params.name);
		});
},

showchart_right(){
     let this_ = this;
    console.log("柱状图地区"+this_.SelectPro)
    let myChart = echarts.init(document.getElementById('proEmission'));
    var xData = function () {
      var data = [];
      for (var i = 2010; i < 2020; i++) {
        data.push(i + "年");
      }
      return data;
    }();
    let option = {
     
      "title": {
        "text": this_.SelectPro+"温室气体排放-处理情况",
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
          color: '#FFF0F5',
        },
        "data": ['焚烧净排', '生物净排', '填埋净排']
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
        "name": "填埋净排",
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
        "data": this.buryNet,
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
        "data":this.bioNet,
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
        "data":this.burnNet
      }, 
      ]
    };
    myChart.setOption(option);
    window.addEventListener('resize', function () { myChart.resize() });
},
showchart_right_bottom(){
     let this_ = this;
    let pieChart = echarts.init(document.getElementById('proPie'));
    let option = {
    title: {
        text: '排放比例饼图',
        x: "4%",
        textStyle: {
          color: '#fff',
          fontSize: '22'
        },
    },
    

    tooltip: {
        trigger: 'item',
        formatter: "{b} : {c} ({d}%)"
    },

    visualMap: {
        show: false,
        min: 500,
        max: 600,
        inRange: {
            //colorLightness: [0, 1]
        }
    },
    series: [{
        name: '排放',
        type: 'pie',
        radius: '50%',
        center: ['50%', '50%'],
        color: [ 'rgb(131,249,103)','#FE5050','#FBFE27','#1DB7E5', , ], //'#FBFE27','rgb(11,228,96)','#FE5050'
        data: [           
          
             {
                value: this.bioOut,
                name: '生物排放'
            },
               {
                value: this.burnOut,
                name: '焚烧排放'
            },
            {
                value: this.buryOut,
                name: '填埋排放'
            },
        ].sort(function(a, b) {
            return a.value - b.value
        }),
        emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      },
        label: {
            normal: {
                formatter: ['{c|{c}百万吨}', '{b|{b}}'].join('\n'),
                rich: {
                    c: {
                        color: 'rgb(241,246,104)',
                        fontSize: 20,
                        fontWeight:'bold',
                        lineHeight: 5
                    },
                    b: {
                        color: 'rgb(98,137,169)',
                        fontSize: 15,
                        height: 40
                    },
                },
            }
        },
        labelLine: {
            normal: {
                lineStyle: {
                    color: 'rgb(98,137,169)',
                },
                smooth: 0.2,
                length: 10,
                length2: 20,

            }
        },
        itemStyle: {
            normal: {
                shadowColor: 'rgba(0, 0, 0, 0.8)',
                shadowBlur: 50,
            }
        }
    }]
};
    pieChart.setOption(option);
    window.addEventListener('resize', function () { myChart.resize() });
},
 getGeoJson(adcode) {
            let that = this;
            AMapUI.loadUI(['geo/DistrictExplorer'], DistrictExplorer => {
                var districtExplorer = new DistrictExplorer()
                districtExplorer.loadAreaNode(adcode, function(error, areaNode) {
                    if (error) {
                        console.error(error);
                        return;
                    }
                    let Json = areaNode.getSubFeatures()
                    if (Json.length > 0) {
                        that.geoJson.features = Json
                        console.log('geoJson', Json)
                    } else if (Json.length === 0) {
                        that.geoJson.features = that.geoJson.features.filter(item => item.properties.adcode == adcode)
                        if (that.geoJson.features.length === 0) return
                    }
                });
            })

        },
},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss' scoped>

.border{
     width: 100%;
     height:95vh;
     background-color:  rgb(8, 15, 62);
     display: flex;
    flex-direction: row;
    
}
.div_any_title{
    background-image: url('./images/边框.png') ;
    background-size: 100% 100%;
    border-radius: 18px;
    position: absolute;
    top:20px;
    height: 60px;
    width: 84%;
    top:10px;
    left: 9%;
    line-height: 52px;
    text-align: center;
    font-size: 1.9rem;
    font-family: MicrosoftYaHei;
    font-weight: bold;
    color: #00FFFF;
}
#left {
    margin-left: 1%;
    width: 30%;
    height:30%;
    margin-top:60px;
    margin-right:12px;

}
.border_center {
    width: 55%;
    margin-left:50px;
    border: 0px solid #185FAE;
    border-radius:10px;
    box-sizing: border-box;
    position: relative;
    box-shadow: -8px 0px 10px #034c6a inset,
    8px 0px 10px #034c6a inset;
    height: 700px;
    padding-top:100px;
}
.border_right {
    width: 35%;
    margin-left:50px;
    border: 0px solid #185FAE;
    border-radius:10px;
    box-sizing: border-box;
    position: relative;
    box-shadow: -8px 0px 10px #034c6a inset,
    8px 0px 10px #034c6a inset;
    height: 700px;
    padding-top:100px;
}
.border-div2 {
    border: 4px solid #185FAE;
    border-radius:12px;
    width: 100%;
    min-height: 350px;
    margin-top: 100px;
    margin-bottom: 32px;
    position: relative;
}
</style>