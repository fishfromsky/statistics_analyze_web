<template>
  <div>
        <div ref="map" class="map-container"></div>
        <div class="control-panel">
            <div class="button-list">
                <span>是否显示标签：</span>
                <el-switch v-model="labelstatus" @change="labelchange"></el-switch>
            </div>
        </div>
  </div>
</template>

<script>
    import { getfactorylist } from '@/api/model'
    import echarts from 'echarts'
    import 'echarts/extension/bmap/bmap'

    export default {
        name: "amap",
        components: {
        },
        data(){
            return{
              bmap: {},
              mapZoom: 10,
              chart: echarts.ECharts,
              data0: [],  // 其他
              data1: [],  //焚烧厂
              data2: [],  //填埋场
              geoCoordMap: {},
              labelstatus: false
            }
        },
        methods: {
            labelchange:function(){
                this.initChart()
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
            getData(){
                var that = this
                getfactorylist().then(res=>{
                    if (res.code === 20000){
                        let fac_data = res.data
                        for (let i=0; i<fac_data.length; i++){
                            let f_name = fac_data[i]['name']
                            let f_value = fac_data[i]['deal']
                            let f_longitude = fac_data[i]['longitude']
                            let f_latitude = fac_data[i]['latitude']
                            if (fac_data[i]['typeId'] === 0){
                                that.data0.push({name: f_name, value: f_value})
                            }
                            else if (fac_data[i]['typeId'] === 1){
                                that.data1.push({name: f_name, value: f_value})
                            }
                            else if (fac_data[i]['typeId'] === 2){
                                that.data2.push({name: f_name, value: f_value})
                            }
                            that.geoCoordMap[f_name] = [f_longitude, f_latitude]
                        }
                        that.initChart()
                    }
                })
            },
            initChart(){
            this.chart = echarts.init(this.$refs.map)
            this.chart.setOption({
              title: {
                  text: '上海市无害化固废垃圾处理厂信息表',
                  subtext: '截至2019年数据',
                  left: 'center',
                  top: 20,
                  textStyle: {
                      color: '#fff'
                  }
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
                    name: '其他(万吨)',
                    type: 'effectScatter',
                    coordinateSystem: 'bmap',
                    data: this.convertData(this.data0),
                    encode: {
                        value: 2
                    },
                    symbolSize: function (val) {
                        return val[2] / 5;
                    },
                    showEffectOn: 'emphasis',
                    rippleEffect: {
                        brushType: 'stroke'
                    },
                    hoverAnimation: true,
                    label: {
                        formatter: '{b}',
                        position: 'right',
                        show: this.labelstatus
                    },
                    itemStyle: {
                        color: '#f4e925',
                        shadowBlur: 10,
                        shadowColor: '#333'
                    },
                    zlevel: 1
                },
                {
                    name: '焚烧厂(万吨)',
                    type: 'effectScatter',
                    coordinateSystem: 'bmap',
                    data: this.convertData(this.data1),
                    encode: {
                        value: 2
                    },
                    symbolSize: function (val) {
                        return val[2] / 5;
                    },
                    showEffectOn: 'emphasis',
                    rippleEffect: {
                        brushType: 'stroke'
                    },
                    hoverAnimation: true,
                    label: {
                        formatter: '{b}',
                        position: 'top',
                        show: this.labelstatus
                    },
                    itemStyle: {
                        color: '#ff33cc',
                        shadowBlur: 10,
                        shadowColor: '#333'
                    },
                    zlevel: 1
                },
                {
                    name: '填埋场(万吨)',
                    type: 'effectScatter',
                    coordinateSystem: 'bmap',
                    data: this.convertData(this.data2),
                    encode: {
                        value: 2
                    },
                    symbolSize: function (val) {
                        return val[2] / 5;
                    },
                    showEffectOn: 'emphasis',
                    rippleEffect: {
                        brushType: 'stroke'
                    },
                    hoverAnimation: true,
                    label: {
                        formatter: '{b}',
                        position: 'top',
                        show: this.labelstatus
                    },
                    itemStyle: {
                        color: '#00ff00',
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

<style scoped>
    .map-container{
        width: 100%;
        height: 95vh;
    }
    .control-panel{
        width: 250px;
        height: 60px;
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 100
    }
    .button-list{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    .button-list span{
        font-size: 15px;
        color: #fff;
    }
</style>
</style>
