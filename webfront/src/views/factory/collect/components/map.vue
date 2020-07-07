<template>
    <div ref="map" class="map-container"></div>
</template>
<script>
import echarts from 'echarts'
import 'echarts/extension/bmap/bmap'
import { gettransferfactory } from '@/api/model'
import da from 'element-ui/src/locale/lang/da'
export default {
    data(){
        return{
            chart: echarts.ECharts,
            data: [],
            geoCoordMap: {}
        }
    },
    methods: {
        getData(){
            var that = this
            gettransferfactory().then(res=>{
                if (res.code === 20000){
                    let data = res.data
                    for (let i=0; i<data.length; i++){
                        let name = data[i]['name']
                        let value = data[i]['capacity']
                        let longitude = data[i]['longitude']
                        let latitude = data[i]['latitude']
                        that.data.push({name: name, value: value})
                        that.geoCoordMap[name] = [longitude, latitude]
                    }
                    that.initChart()
                }
            })
        },
        convertData(data){
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = this.geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value)
                    });
                }
            }
            return res;
        },
        initChart(){
            this.chart = echarts.init(this.$refs.map)
            this.chart.setOption({
              title: {
                  text: '上海市垃圾中转站信息表',
                  subtext: '截至2019年数据',
                  left: 'center',
                  textStyle: {
                      color: '#fff'
                  },
                  top: 20
              },
              tooltip : {
                  trigger: 'item'
              },
              bmap: {
                    center: [121.478423, 31.222243],
                    zoom: 11,
                    roam: true,
                    mapStyle: {
                        styleJson: [
                        {
                            "featureType": "water",
                            "elementType": "all",
                            "stylers": {
                                "color": "#044161"
                            }
                        },
                        {
                            "featureType": "land",
                            "elementType": "all",
                            "stylers": {
                                "color": "#004981"
                            }
                        },
                        {
                            "featureType": "boundary",
                            "elementType": "geometry",
                            "stylers": {
                                "color": "#064f85"
                            }
                        },
                        {
                            "featureType": "railway",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "highway",
                            "elementType": "geometry",
                            "stylers": {
                                "color": "#004981"
                            }
                        },
                        {
                            "featureType": "highway",
                            "elementType": "geometry.fill",
                            "stylers": {
                                "color": "#005b96",
                                "lightness": 1
                            }
                        },
                        {
                            "featureType": "highway",
                            "elementType": "labels",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "arterial",
                            "elementType": "geometry",
                            "stylers": {
                                "color": "#004981"
                            }
                        },
                        {
                            "featureType": "arterial",
                            "elementType": "geometry.fill",
                            "stylers": {
                                "color": "#00508b"
                            }
                        },
                        {
                            "featureType": "poi",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "green",
                            "elementType": "all",
                            "stylers": {
                                "color": "#056197",
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "subway",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "manmade",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "local",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "arterial",
                            "elementType": "labels",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "boundary",
                            "elementType": "geometry.fill",
                            "stylers": {
                                "color": "#029fd4"
                            }
                        },
                        {
                            "featureType": "building",
                            "elementType": "all",
                            "stylers": {
                                "color": "#1a5787"
                            }
                        },
                        {
                            "featureType": "label",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        }
                    ]
                  }
              },
              series : [
                {
                    name: '垃圾中转站',
                    type: 'effectScatter',
                    coordinateSystem: 'bmap',
                    data: this.convertData(this.data),
                    encode: {
                        value: 2
                    },
                    symbolSize: function (val) {
                        return val[2] / 15;
                    },
                    showEffectOn: 'emphasis',
                    rippleEffect: {
                        brushType: 'stroke'
                    },
                    hoverAnimation: true,
                    label: {
                        formatter: '{b}',
                        position: 'right',
                        show: true
                    },
                    itemStyle: {
                        color: '#f4e925',
                        shadowBlur: 10,
                        shadowColor: '#333'
                    },
                    zlevel: 1
                },
              ]
            })
        }
    },
    mounted(){
        this.getData()
    }
}
</script>

<style lang="less" scoped>
    .map-container{
        width: 100%;
        height: 95vh;
    }
</style>