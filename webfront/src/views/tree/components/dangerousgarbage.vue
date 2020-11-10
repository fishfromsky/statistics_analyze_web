<template>
   <div>
       <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
           <el-table-column label="年份" align="center">
               <template slot-scope="{row}">
                   <span>{{row.year}}</span>
               </template>
           </el-table-column>
           <el-table-column label="危险废物产生量" align="center">
               <template slot-scope="{row}">
                   <span>{{row.production}}</span>
               </template>
           </el-table-column>
           <el-table-column label="危险废物处置量" align="center">
               <template slot-scope="{row}">
                   <span>{{row.deal}}</span>
               </template>
           </el-table-column>
           <el-table-column label="危险废物综合利用" align="center">
               <template slot-scope="{row}">
                   <span>{{row.use}}</span>
               </template>
           </el-table-column>
           <el-table-column label="危险废物储存量" align="center">
               <template slot-scope="{row}">
                   <span>{{row.store}}</span>
               </template>
           </el-table-column>
           <el-table-column label="数据操作" align="center">
               <template slot-scope="scope">
                   <el-button size="mini" type="primary" @click="AmendData(scope.$index)">修改</el-button>
                   <el-button size="mini" type="danger" @click="DeleteData(scope.$index)" style="margin-left: 30px">删除</el-button>
               </template>
           </el-table-column>
       </el-table>
       <el-dialog :visible.sync="amend_dialog" title="修改数据" width="40%">
           <el-form :model="form">
               <el-form-item label="危险垃圾产生量">
                   <el-input v-model="form.production" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾处置量">
                   <el-input v-model="form.deal" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾综合利用">
                   <el-input v-model="form.use" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾储存量">
                   <el-input v-model="form.store" auto-complete="off"></el-input>
               </el-form-item>
           </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="amend_dialog = false">取 消</el-button>
                <el-button type="primary" @click="AmendDataConfirm">确 定</el-button>
            </div>
       </el-dialog>
       <el-dialog :visible.sync="delete_dialog" title="删除数据" width="30%">
           <span>确定删除改数据吗？删除后不可恢复</span>
           <div slot="footer" class="dialog-footer">
                <el-button @click="delete_dialog = false">取 消</el-button>
                <el-button type="danger" @click="DeleteDataConfirm">确 定</el-button>
            </div>
       </el-dialog>
       <el-dialog :visible.sync="add_dialog" title="添加数据" width="40%">
           <el-form :model="add_form">
               <el-form-item label="年份">
                   <el-input v-model="add_form.year" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾产生量">
                   <el-input v-model="add_form.production" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾处置量">
                   <el-input v-model="add_form.deal" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾综合利用">
                   <el-input v-model="add_form.use" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="危险垃圾储存量">
                   <el-input v-model="add_form.store" auto-complete="off"></el-input>
               </el-form-item>
           </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="add_dialog = false">取 消</el-button>
                <el-button type="primary" @click="addDataConfirm">确 定</el-button>
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
import { getdangerousgarbage, amenddangerousgarbage, deletedangeroudgarbage, addbyrowdangerousgarbage } from '@/api/model'
export default {
    data(){
        return{
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
            add_form: {},
            delete_form: {
                id: ''
            }
        }
    },
    methods: {
        getData(){
            let that = this
            getdangerousgarbage().then(res=>{
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
        AmendData(index){
           this.form = this.page_data[index]
           this.amend_dialog = true
        },
        AmendDataConfirm(){
            let data = this.form
            let that = this
            amenddangerousgarbage(data).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: '修改成功'
                    })
                    that.page_data = []
                    that.getData()
                }
            })
            this.amend_dialog = false
        },
        DeleteData(index){
            this.delete_dialog = true
            this.delete_form.id = this.page_data[index].id
        },
        DeleteDataConfirm(){
            let that = this
            deletedangeroudgarbage(this.delete_form).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: '删除成功'
                    })
                    that.page_data = []
                    that.delete_dialog = false
                    that.getData()
                }
            })
        },
        addData(){
          this.add_dialog = true
        },
        addDataConfirm(){
            let data = this.add_form
            let that = this
            addbyrowdangerousgarbage(data).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: '添加成功'
                    })
                    that.page_data = []
                    that.getData()
                }
            })
            this.add_dialog = false
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
        }
    },
    mounted(){
        this.getData()
    }
}
</script>

<style scoped>

</style>
