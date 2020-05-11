<template>
  <div>
    <el-dialog title="地点详情" :visible.sync="dialogvisible" width="50%">
      <el-table :data="dialogdata" border style="width: 100%">
        <el-table-column prop="name" label="工厂名称"/>
        <el-table-column prop="address" label="工厂地址"/>
        <el-table-column prop="deal" label="日处理量/吨"/>
      </el-table>
    </el-dialog>
    <div class="amap-container">
      <el-amap-circle v-for="circle in circles" :center="circle.center" :radius="circle.radius" :fill-opacity="circle.fillOpacity"></el-amap-circle>
      <el-amap-search-box class="search-box" :search-option="searchOption" :on-search-result="onSearchResult"></el-amap-search-box>
      <el-amap vid="amap" :plugin="plugin" class="amap-demo" :zoom="zoom" :center="center">
        <el-amap-marker
        v-for="(marker, index) in markers"
        :key="index"
        :position="marker.position"
        :visible="true"
        :draggable="false"
        :vid="marker.id"
        :title="marker.name"
        :events="marker.events"></el-amap-marker>
      </el-amap>
      <div class="input-box">
        <label class="search_label">地理编码，根据地址获取经纬度坐标</label>
        <el-input v-model="search_address" placeholder="请输入搜索地理信息">
          <template slot="prepend">地址</template>
        </el-input>
        <el-input v-model="search_geo" disabled style="margin-top: 20px">
          <template slot="prepend">坐标</template>
        </el-input>
        <el-button type="primary" style="width: 100%; margin-top: 20px" @click="Address_Transfer">坐标转换</el-button>
      </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    import VueAMap from 'vue-amap'
    import Vue from 'vue'
    import { getfactory, getfactorybyid, address_transfer } from "@/api/factory"
    Vue.use(VueAMap);
    VueAMap.initAMapApiLoader({
        key: 'b84d5392efeafdc572f53e8de8dfd501',
        plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor', 'AMap.Geolocation']
    });

    export default {
        name: "amap",
        data(){
            const self = this;
            return{
                center: [121.398858, 31.318299],
                search_address: '',
                search_geo:'',
                circles:[
                    {
                        center: [121.398858, 31.318299],
                        radius: 200,
                        fillOpacity: 0.5
                    }
                ],
                lng: 0,
                lat: 0,
                loaded: false,
                zoom: 15,
                markers: [],
                plugin: [
                    {
                        pName: 'Geolocation',
                        events: {
                            init(o) {
                                // o 是高德地图定位插件实例
                                o.getCurrentPosition((status, result) => {
                                    if (result && result.position) {
                                        self.lng = result.position.lng
                                        self.lat = result.position.lat
                                        self.center = [self.lng, self.lat]
                                        self.loaded = true
                                        self.$nextTick()
                                    }
                                })
                            }
                        }
                    },
                    {
                        pName: 'ToolBar',
                        events: {
                            init(instance) {
                                // console.log(instance);
                            }
                        }
                    }
                ],
                searchOption: {
                    citylimit: false
                },
                dialogvisible: false,
                dialogdata: null
            }
        },
        methods: {
            Address_Transfer:function(){
                let that = this
                let address = that.search_address
                axios({
                    method: 'get',
                    url: 'https://restapi.amap.com/v3/geocode/geo?address=' + address + '&key=c83eaee63075867503a71b3282e11a1a'
                }).then(res => {
                    let geos = res.data.geocodes[0].location
                    that.search_geo = geos
                }).catch(res => {
                    console.log(res)
                })
            },
            // 地图搜索地点触发的函数
            onSearchResult(pois) {
                let latSum = 0
                let lngSum = 0
                if (pois.length > 0) {
                    pois.forEach(poi => {
                        const { lng, lat } = poi
                        lngSum += lng
                        latSum += lat
                        this.markers.push([poi.lng, poi.lat])
                    })
                    const center = {
                        lng: lngSum / pois.length,
                        lat: latSum / pois.length
                    }
                    this.center = [center.lng, center.lat]
                }
            },
            getFactoryList(){
                let that = this;
                getfactory().then(res=>{
                    if (res.code === 20000){
                        let list = res.data;
                        for (let i=0; i<list.length; i++){
                            let dict = {};
                            dict['id'] = list[i].id;
                            dict['name'] = list[i].name;
                            dict['address'] = list[i].address;
                            dict['deal'] = list[i].deal;
                            dict['position'] = [list[i].longitude, list[i].latitude];
                            dict['events'] = {
                                click: (e) => {
                                    let data = {};
                                    data['id'] = e.target.F.vid;
                                    getfactorybyid(data).then(res => {
                                        that.dialogvisible = true;
                                        that.dialogdata = res.data
                                    })
                                }
                            }
                            that.markers.push(dict)
                        }
                    }
                    else{
                        this.$message.error('error')
                    }
                })
            }
        },
        mounted() {
            this.getFactoryList()
        }
    }
</script>

<style scoped>
  .amap-demo{
    width: 100%;
    height: 95vh;
  }
  .amap-container{
    position: relative;
  }
  .search-box {
    position: absolute;
    top: 25px;
    left: 80px;
  }
  .input-box{
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border-radius: .25rem;
    width: 22rem;
    border-width: 0;
    border-radius: 0.4rem;
    box-shadow: 0 2px 6px 0 rgba(114, 124, 245, .5);
    position: fixed;
    bottom: 1rem;
    right: 1rem;
    -ms-flex: 1 1 auto;
    flex: 1 1 auto;
    padding: 0.75rem 1.25rem;
  }
  .search_label{
    font-size: 13px;
    color: #333333;
    float: left;
    margin-bottom: 20px;
  }
</style>
