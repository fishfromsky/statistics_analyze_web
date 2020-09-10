<template>
   <div>
       <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
           <el-table-column label="项目ID" align="center">
               <template slot-scope="{row}">
                   <span>{{row.project_id}}</span>
               </template>
           </el-table-column>
           <el-table-column label="项目名称" align="center" min-width="80">
               <template slot-scope="{row}">
                   <span>{{row.name}}</span>
               </template>
           </el-table-column>
           <el-table-column label="basic表长度" align="center" min-width="50">
               <template slot-scope="{row}">
                   <span>{{row.basic_size}}</span>
               </template>
           </el-table-column>
           <el-table-column label="ts表长度" align="center" min-width="50">
               <template slot-scope="{row}">
                   <span>{{row.ts_size}}</span>
               </template>
           </el-table-column>
           <el-table-column label="rrc表长度" align="center" min-width="50">
               <template slot-scope="{row}">
                   <span>{{row.rrc_size}}</span>
               </template>
           </el-table-column>
           <el-table-column label="cost_matrix表长度" align="center" min-width="50">
               <template slot-scope="{row}">
                   <span>{{row.cost_matrix_size}}</span>
               </template>
           </el-table-column>
           <el-table-column label="项目状态" align="center" min-width="50">
               <template slot-scope="{row}">
                   <span>{{row.project_state}}</span>
               </template>
           </el-table-column>
           <el-table-column label="数据操作" align="center" min-width="100">
               <template slot-scope="scope">
                   <el-button size="mini" type="primary" @click="AmendData(scope.$index)">修改</el-button>
                   <el-button size="mini" type="danger" @click="GetLocation(scope.$index)" style="margin-left: 30px">模型实验</el-button>
               </template>
           </el-table-column>
       </el-table>
       <el-dialog :visible.sync="amend_dialog" title="修改数据" width="40%">
           <el-form :model="form">
               <el-form-item label="项目名称">
                   <el-input v-model="form.name" auto-complete="off"></el-input>
               </el-form-item>
           </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="amend_dialog = false">取 消</el-button>
                <el-button type="primary" @click="AmendDataConfirm">确 定</el-button>
            </div>
       </el-dialog>
       <el-dialog :visible.sync="get_dialog" title="获取集散厂位置" width="30%">
           <el-form :model="form">
               <el-form-item label="集散厂数量">
                   <el-input v-model="form.plot_num" auto-complete="off"></el-input>
               </el-form-item>
           </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="get_dialog = false">取 消</el-button>
                <el-button type="primary" @click="GetLocationConfirm">确 定</el-button>
            </div>
       </el-dialog>
        <el-dialog :visible.sync="add_dialog" title="添加数据" width="40%">
           <el-form :model="form">
           <el-form-item label="项目ID">
                   <el-input v-model="form.project_id" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="项目名称">
                   <el-input v-model="form.name" auto-complete="off"></el-input>
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
        <el-image v-show="LocationImage" v-loading="image_loading" style="width: 700px; height: 700px" :src="url"></el-image>
   </div>
</template>

<script>
import { getpmedianproject, addpmedianproject, amendpmedianproject, getplotlocation } from '@/api/model'
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
            get_dialog: false,
            add_dialog: false,
            LocationImage: false,
            form: {},
            get_form: {
                project_id: '',
                plot_num: ''
            },
            url: '',
            image_loading: false
        }
    },
    methods: {
        getData(){
            let that = this
            getpmedianproject().then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    let size = that.page_size
                    let index = that.currentPage-1
                    that.page_data = []
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
            amendpmedianproject(data).then(res=>{
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
        GetLocation(index){
        if (this.page_data[index].basic_size === 0 || this.page_data[index].ts_size === 0 || this.page_data[index].rrc_size === 0 ) {
          this.$message.error('请先导入实验参数表')
        } else {
            this.get_form.project_id = this.page_data[index].project_id
            let that = this
            that.page_data[index].project_state = '正在运行'
            getplotlocation(this.get_form).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: 'success'
                    })
                }
                that.getData()
            })

        }
        },
        GetLocationConfirm(){
            let that = this
            getplotlocation(this.get_form).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: 'success'
                    })
                }
            })
        },
        addData(){
          this.add_dialog = true
        },
        addDataConfirm(){
            let data = this.form
            let that = this
            addpmedianproject(data).then(res=>{
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
