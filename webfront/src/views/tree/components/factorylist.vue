<template>
    <div>
        <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
            <el-table-column label="名称" align="center">
                <template slot-scope="{row}">
                    <span>{{row.name}}</span>
                </template>
            </el-table-column>
            <el-table-column label="地址" align="center">
                <template slot-scope="{row}">
                    <span>{{row.address}}</span>
                </template>
            </el-table-column>
            <el-table-column label="经度" align="center">
                <template slot-scope="{row}">
                    <span>{{row.longitude}}</span>
                </template>
            </el-table-column>
            <el-table-column label="纬度" align="center">
                <template slot-scope="{row}">
                    <span>{{row.latitude}}</span>
                </template>
            </el-table-column>
            <el-table-column label="处理量(吨/天)" align="center">
                <template slot-scope="{row}">
                    <span>{{row.deal}}</span>
                </template>
            </el-table-column>
            <el-table-column label="所属公司" align="center">
                <template slot-scope="{row}">
                    <span>{{row.company}}</span>
                </template>
            </el-table-column>
            <el-table-column label="类型" align="center">
                <template slot-scope="{row}">
                    <span>{{row.type}}</span>
                </template>
            </el-table-column>
            <el-table-column label="所属区" align="center">
                <template slot-scope="{row}">
                    <span>{{row.district}}</span>
                </template>
            </el-table-column>
            <el-table-column label="数据操作" align="center" min-width="80">
                <template slot-scope="scope">
                   <el-button size="mini" type="primary" @click="AmendData(scope.$index)">修改</el-button>
                   <el-button size="mini" type="danger" @click="DeleteData(scope.$index)" style="margin-left: 30px">删除</el-button>
               </template>
            </el-table-column>
        </el-table>
        <el-dialog title="修改无害化处理厂数据" :visible.sync="amend_dialog" width="30%">
            <el-form :model="form">
                <el-form-item label="处理厂名称">
                    <el-input v-model="form.name" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="处理厂地址">
                    <el-input v-model="form.address" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="经度">
                    <el-input v-model="form.longitude" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="纬度">
                    <el-input v-model="form.latitude" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="处理量(吨/天)">
                    <el-input v-model="form.deal"></el-input>
                </el-form-item>
                <el-form-item label="处理厂类型">
                    <el-select v-model="form.type">
                        <el-option label="焚烧" value="焚烧"></el-option>
                        <el-option label="填埋" value="填埋"></el-option>
                        <el-option label="其他" value="其他"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="所属公司">
                    <el-input v-model="form.company" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="所属区域">
                    <el-select v-model="form.district">
                        <el-option label="黄浦区" value="黄浦区"></el-option>
                        <el-option label="静安区" value="静安区"></el-option>
                        <el-option label="长宁区" value="长宁区"></el-option>
                        <el-option label="徐汇区" value="徐汇区"></el-option>
                        <el-option label="普陀区" value="普陀区"></el-option>
                        <el-option label="虹口区" value="虹口区"></el-option>
                        <el-option label="杨浦区" value="杨浦区"></el-option>
                        <el-option label="宝山区" value="宝山区"></el-option>
                        <el-option label="嘉定区" value="嘉定区"></el-option>
                        <el-option label="闵行区" value="闵行区"></el-option>
                        <el-option label="浦东新区" value="浦东新区"></el-option>
                        <el-option label="金山区" value="金山区"></el-option>
                        <el-option label="松江区" value="松江区"></el-option>
                        <el-option label="青浦区" value="青浦区"></el-option>
                        <el-option label="崇明区" value="崇明区"></el-option>
                        <el-option label="奉贤区" value="奉贤区"></el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="amend_dialog = false">取 消</el-button>
                <el-button type="primary" @click="AmendDataConfirm">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog title="删除无害化处理厂信息" :visible.sync="delete_dialog" width="30%">
            <span>确定删除该无害化处理厂信息吗？删除后不可恢复</span>
            <div slot="footer" class="dialog-footer">
                <el-button @click="delete_dialog = false">取 消</el-button>
                <el-button type="danger" @click="DeleteDataConfirm">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog title="增加无害化处理厂信息" :visible.sync="add_dialog" width="30%">
            <el-button style="margin-left: 16.5%; margin-bottom: 20px" type="primary" @click="showmap">点击选择，一键生成地理位置信息</el-button>
            <el-form v-model="add_form">
                <el-form-item label="处理厂名称" :label-width="labelwidth">
                    <el-input v-model="add_form.name" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="处理厂地址" :label-width="labelwidth">
                    <el-input v-model="add_form.address" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="经度" :label-width="labelwidth">
                    <el-input v-model="add_form.longitude" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="纬度" :label-width="labelwidth">
                    <el-input v-model="add_form.latitude" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="处理量(吨/天)" :label-width="labelwidth">
                    <el-input v-model="add_form.deal"></el-input>
                </el-form-item>
                <el-form-item label="处理厂类型" :label-width="labelwidth">
                    <el-select v-model="add_form.type">
                        <el-option label="焚烧" value="焚烧"></el-option>
                        <el-option label="填埋" value="填埋"></el-option>
                        <el-option label="其他" value="其他"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="所属公司" :label-width="labelwidth">
                    <el-input v-model="add_form.company" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="所属区域" :label-width="labelwidth">
                    <el-select v-model="add_form.district">
                        <el-option label="黄浦区" value="黄浦区"></el-option>
                        <el-option label="静安区" value="静安区"></el-option>
                        <el-option label="长宁区" value="长宁区"></el-option>
                        <el-option label="徐汇区" value="徐汇区"></el-option>
                        <el-option label="普陀区" value="普陀区"></el-option>
                        <el-option label="虹口区" value="虹口区"></el-option>
                        <el-option label="杨浦区" value="杨浦区"></el-option>
                        <el-option label="宝山区" value="宝山区"></el-option>
                        <el-option label="嘉定区" value="嘉定区"></el-option>
                        <el-option label="闵行区" value="闵行区"></el-option>
                        <el-option label="浦东新区" value="浦东新区"></el-option>
                        <el-option label="金山区" value="金山区"></el-option>
                        <el-option label="松江区" value="松江区"></el-option>
                        <el-option label="青浦区" value="青浦区"></el-option>
                        <el-option label="崇明区" value="崇明区"></el-option>
                        <el-option label="奉贤区" value="奉贤区"></el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="add_dialog = false">取 消</el-button>
                <el-button type="primary" @click="AddDataConfirm">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog title="获取地理位置信息" :visible.sync="map_dialog">
            <div class="amap-page-container">
                <el-amap-search-box class="search-box" :search-option="searchOption" :on-search-result="onSearchResult"></el-amap-search-box>
                <el-amap vid="amap" :plugin="plugin" :zoom="zoom" :center="center" class="amap-demo" :events="events" />
            </div>
        </el-dialog>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[10, 20, 30, 40, 50]"
            :page-size="page_size"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total_size"
            style="margin-top: 20px">
        </el-pagination>
    </div>
</template>

<script>
import { getfactorylist, amendfactorylist, deletefactorylist, addfactorylistbyrow } from '@/api/model'
import VueAMap from 'vue-amap'
import Vue from 'vue'
Vue.use(VueAMap)
VueAMap.initAMapApiLoader({
    key: 'b84d5392efeafdc572f53e8de8dfd501',
    plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor', 'AMap.Geolocation', 'Geocoder']
})
export default {
    name: 'factorylist',
    data(){
        const self = this
        return {
            table_loading: true,
            tablekey: 0,
            tableData: [],
            page_data: [],
            formData: [],
            total_size: 0,
            currentPage: 1,
            page_size: 10,
            amend_dialog: false,
            delete_dialog: false,
            add_dialog: false,
            form: {},
            delete_form: {
                id: ''
            },
            add_dialog: false,
            add_form: {
                name: '',
                address: '',
                logitude: '',
                latitude: '',
                deal: '',
                type: '',
                district: ''
            },
            labelwidth: '120px',
            map_dialog: false,
            zoom: 15,
            center: [121.456848, 31.274044],
            plugin: [{
                pName: 'Geolocation',
                events: {
                
                }
            }],
             searchOption: {
                city: '上海',
                citylimit: false
            },
            events: {
                click(e) {
                    const { lng, lat } = e.lnglat
                    self.add_form.longitude = lng
                    self.add_form.latitude = lat
                    // 这里通过高德 SDK 完成。
                    var geocoder = new AMap.Geocoder({
                        radius: 1000,
                        extensions: 'all'
                    })
                    geocoder.getAddress([lng, lat], function(status, result) {
                        if (status === 'complete' && result.info === 'OK') {
                            if (result && result.regeocode) {
                                self.add_form.address = result.regeocode.formattedAddress
                                self.add_form.name = result.regeocode.aois[0].name
                                self.add_form.district = result.regeocode.addressComponent.district
                                self.$nextTick()
                                self.$message({
                                    message: '获取位置成功',
                                    type: 'success'
                                })
                                self.map_dialog = false
                            }
                        }
                    })
                }
            },
            filename: 'factorylist',
            autoWidth: true,
            bookType: 'xlsx',
        }
    },
    methods:{
        formatJson(filterVal, jsonData) {
            return jsonData.map(v => filterVal.map(j => {
                if (j === 'timestamp') {
                return parseTime(v[j])
                } else {
                return v[j]
                }
            }))
        },
        DownLoad:function(){
            import('@/vendor/Export2Excel').then(excel => {
                const tHeader = ['name', 'address', 'longitude', 'latitude', 'deal', 'company', 'type', 'district']
                const filterVal = ['name', 'address', 'longitude', 'latitude', 'deal', 'company', 'type', 'district']
                const list = this.tableData
                const data = this.formatJson(filterVal, list)
                excel.export_json_to_excel({
                header: tHeader,
                data,
                filename: this.filename,
                autoWidth: this.autoWidth,
                bookType: this.bookType
                })
            })
        },
        onSearchResult(pois) {
          let latSum = 0;
          let lngSum = 0;
          if (pois.length > 0) {
            pois.forEach(poi => {
                let {lng, lat} = poi;
                lngSum += lng;
                latSum += lat;
                });
                let cent = {
                    lng: lngSum / pois.length,
                    lat: latSum / pois.length
                };
                this.center = [cent.lng, cent.lat];
            }
        },
        showmap:function(){
            this.map_dialog = true
        },
        addData(){
            this.add_dialog = true
        },
        getData(){
            var that = this
            getfactorylist().then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    let size = that.page_size
                    let index = that.currentPage-1
                    for (let i=index*size; i<(index+1)*size; i++){
                        if (i==res.data.length){
                            break
                        }
                        that.page_data.push(res.data[i])
                    }
                    that.total_size = res.data.length
                }
            })
        },
        handleSizeChange(val){
            this.table_loading = true
            this.page_size = val
            this.currentPage = 1
            this.page_data = []
            this.getData()
        },
        handleCurrentChange(val){
            this.currentPage = val
            this.page_data = []
            this.getData()
        },
        AmendData(val){
            this.form = this.page_data[val]
            this.amend_dialog = true
        },
        AmendDataConfirm(){
            var that = this
            let type = this.form['type']
            if (type === '焚烧'){
                this.form['typeId'] = 1
            }
            else if (type === '填埋'){
                this.form['typeId'] = 2
            }
            else{
                this.form['typeId'] = 0
            }
            amendfactorylist(this.form).then(res=>{
                if (res.code === 20000){
                    that.$message({
                        type: 'success',
                        message: '修改成功'
                    })
                    that.page_data = []
                    that.getData()
                }
                that.amend_dialog = false
            })
        },
         DeleteData(index){
            this.delete_dialog = true
            this.delete_form.id = this.page_data[index].id
        },
        DeleteDataConfirm(){
            var that = this
            deletefactorylist(this.delete_form).then(res=>{
                if (res.code === 20000){
                    that.$message({
                        type: 'success',
                        message: '删除成功'
                    })
                    that.page_data = []
                    that.delete_dialog = false
                    that.getData()
                }
            })
        },
        AddDataConfirm(){
            let that = this
            if (this.add_form.name === '' || this.add_form.address === '' || this.add_form.longitude === '' || this.add_form.latitude === ''
             || this.add_form.type === '' || this.add_form.district === '' || this.add_form.company === '' || this.add_form.deal === ''){
                 this.$message.error('表格信息不完整，请完善信息')
            }
            else{
                 let type = this.add_form.type
                if (type === '焚烧'){
                    this.add_form.typeId = 1
                }
                else if (type === '填埋'){
                    this.add_form.typeId = 2
                }
                else{
                    this.add_form.typeId = 0
                }
                addfactorylistbyrow(this.add_form).then(res=>{
                    if (res.code === 20000){
                        that.$message({
                            type: 'success',
                            message: '添加成功'
                        })
                        that.page_data = []
                        that.add_dialog = false
                        that.getData()
                    }
                })
            }
        }
    },
    mounted(){
        this.getData()
    }
}
</script>
<style lang="less" scoped>
    .amap-page-container{
        position: relative;
    }
    .search-box {
        position: absolute;
        top: 25px;
        left: 20px;
    }
    .amap-demo{
        width: 100%;
        margin: auto;
        height: 50vh
    }
</style>