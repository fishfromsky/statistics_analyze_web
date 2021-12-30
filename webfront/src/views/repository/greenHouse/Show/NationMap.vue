<template>

        <div class="border">
        <div class="border_center">
        <div class="div_any_title">全国分布地图</div>
         <div id="center_chart" ref="chart" style="width:100%;height:95%;display: inline-block;"></div>

        </div>
         <div class="border_right">
            <div class="div_any_title">各省份情况</div>
            <pro-emission datastyle="height: 100vh"></pro-emission>
         <div id="right_chart1" ref="chart_r" style="width:100%; height:50% ;border:1px solid transparent ;margin-top: 0px" ></div>
        <div id="rightchart2" ref="chart_r2" style="width:100%; height:50% ;border:1px solid transparent;top: 50% " ></div>
        </div> 
      </div>      
            
     

</template>

<script src="echarts.min.js"></script>
<script>
import *as echarts from 'echarts';
import 'echarts/map/js/china.js'; // 引入中国地图数据
import proEmission from './components/proEmission.vue'
import schooldata from './map.js';


export default {
  name: 'NationMap',
  components: {
      proEmission,
          },
  data () {
    return {
    schooldata: {},
    center_chart:null,
    geoJson: {
                features: []
            },
    }
    },
    mounted(){
      this.showchart_center();
      this.getGeoJson(100000); // 获取全国地图
    //   this.leftchart1 = this.$echarts.init(document.getElementById('leftchart1'));
    
         },
  methods:{

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
        color: ['#5475f5', '#9feaa5', '#85daef','#98FB98', '#e6ac53', '#9fb5ea'] , //设置坐标点从小到大的颜色,蓝、绿、淡蓝、
        pieces: [{
                lte: 100,
                label: '总量<=100'
            },{
                gt:100,
                lte: 200,
                label: '100<总量<=200'
            },
            {
                gt:200,
                lte: 300,
                label: '200<总量<=300'
            },
            {
                gt: 300,
                label: '总量>300'
            },
        ],
        textStyle: {
            color: '#aaaaaa'
        },
        itemWidth: 10,
        itemHeight: 10,
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
                 data:schooldata,
            }, 
        ]
};
      chart.setOption(option);   
      var index = 0; //播放所在下标
      this.mTime = setInterval(function() {
      chart.dispatchAction({
          type: 'showTip',
          seriesIndex: 1,
          dataIndex: index,
     });
     index++;
     if(index >= schooldata.length) {
       index = 0;
     }
}, 3000);
	chart.on('click', function(params){
			alert(1);
			console.log(params);//此处写点击事件内容
		});
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