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
        <el-dialog title="修改无害化处理厂数据" :visible.sync="amend_dialog" width="40%">
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
        <el-dialog title="删除无害化处理厂信息" :visible.sync="delete_dialog" width="40%">
            <span>确定删除该无害化处理厂信息吗？删除后不可恢复</span>
            <div slot="footer" class="dialog-footer">
                <el-button @click="delete_dialog = false">取 消</el-button>
                <el-button type="danger" @click="DeleteDataConfirm">确 定</el-button>
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
import { getfactorylist, amendfactorylist, deletefactorylist } from '@/api/model'
export default {
    name: 'factorylist',
    data(){
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
            }
        }
    },
    methods:{
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
        }
    },
    mounted(){
        this.getData()
    }
}
</script>