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
           <el-table-column label="添加时间" align="center" min-width="50">
               <template slot-scope="{row}">
                   <span>{{row.add_time}}</span>
               </template>
           </el-table-column>
            <el-table-column label="运行状态" align="center" min-width="50">
               <template slot-scope="scope">
                   <el-tag effect="dark" :type="scope.row.status == '未运行' ? 'info':'success'">{{scope.row.status}}</el-tag>
                   <el-button size="mini" @click="Refresh" type="primary">刷新</el-button>
               </template>
           </el-table-column>
           <el-table-column label="数据操作" align="center" min-width="100">
               <template slot-scope="scope">
                   <el-button size="mini" type="primary" @click="AmendData(scope.$index)">修改信息</el-button>
                   <el-button size="mini" type="danger" @click="Experiment(scope.$index)">模型实验</el-button>
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
       <el-dialog :visible.sync="add_dialog" title="添加数据">
           <el-form :model="add_form">
               <el-form-item label="项目ID">
                   <el-input v-model="add_form.project_id" placeholder="请输入项目ID" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="项目名称">
                   <el-input v-model="add_form.name" placeholder="请输入项目名称" auto-complete="off"></el-input>
               </el-form-item>
           </el-form>
           <div slot="footer">
               <el-button @click="add_dialog=false">取消</el-button>
               <el-button @click="addDataConfirm" type="primary">确定</el-button>
           </div>
       </el-dialog>
       <el-dialog :visible.sync="choose_dialog" title="选择关联分析算法" width="30%">
           <el-select v-model="choose_value" placeholder="请选择想要进行的算法">
               <el-option v-for="item in choose_item" :key="item.value" :label="item.label" :value="item.value"></el-option>
           </el-select>
           <div slot="footer">
               <el-button @click="choose_dialog=false">取消</el-button>
               <el-button @click="ExperimentConfirm" type="primary">确定</el-button>
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
import { getrelationproject, addrelationproject, amendrelationproject, startrelation } from '@/api/model'
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
            choose_dialog: false,
            choose_value: null,
            choose_item: [
                { value: '1', label: '相关矩阵'},
                { value: '2', label: '随机森林'}
            ],
            choose_id: null,
            LocationImage: false,
            form: {},
            add_form: {
                project_id: '',
                name: ''
            },
            get_form: {
                project_id: '',
                plot_num: ''
            },
            url: '',
            image_loading: false
        }
    },
    methods: {
        Refresh:function(){
            this.table_loading = true
            this.page_data = []
            this.tableData = []
            this.getData()
        },
        Experiment:function(val){
            this.choose_dialog = true
            this.choose_id = this.page_data[val].project_id
        },
        ExperimentConfirm:function(){
            let that = this
            if (this.choose_value === null){
                this.$message.error('请选择具体算法')
            }
            else{
                let data = {}
                data['project_id'] = this.choose_id
                data['algorithm'] = this.choose_value
                startrelation(data).then(res=>{
                    that.choose_dialog = false
                    if (res.code === 20000){
                        that.$message({
                            type: 'success',
                            message: '运行成功'
                        })
                        that.table_loading = true
                        that.page_data = []
                        that.tableData = []
                        that.getData()
                    }
                })
            }
        },
        timeStamptoTime:function(time){
            var date = new Date(time);
            let Y = date.getFullYear() + '-';
            let M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
            let D = date.getDate() + ' ';
            let h = date.getHours() + ':';
            let m = date.getMinutes() + ':';
            let s = date.getSeconds();
            return Y+M+D+h+m+s;
        },
        getData(){
            let that = this
            getrelationproject().then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    for (let i=0; i<res.data.length; i++){
                        let time = res.data[i].add_time
                        time = new Date(time.replace(/-/g,'/')).getTime()+3600*1000*8
                        res.data[i].add_time = that.timeStamptoTime(time)
                    }
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
            amendrelationproject(data).then(res=>{
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
        Project_start(index){
        if (this.page_data[index].lstm_project_table_size === 0) {
          this.$message.error('请先导入实验参数表')
        } else {
            let that = this
            LstmProjectStart(this.page_data[index].project_id).then(res=>{
              if(res.code === 20000) {
                this.$message({
                  type: 'success',
                  message: '模型开始运行'
                })
              } else if (res.code === 50000) {
                this.$message({
                  type: 'error',
                  message: '模型已在运行中！'
                })
              }
            }
            )
        }
        },
        addPrograme(){
          this.add_dialog = true
        },
        addDataConfirm(){
            let data = this.add_form
            if (this.add_form.project_id === ''){
                this.$message.error('请输入项目ID')
            }
            else if (this.add_form.name === ''){
                this.$message.error('请输入项目名称')
            }
            else{
                 let that = this
                addrelationproject(data).then(res=>{
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
            }
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
