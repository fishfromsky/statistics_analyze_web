<template>
   <div>
       <el-table v-show="tableshow" v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
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
           <el-table-column label="运行类型" align="center" min-width="50">
               <template slot-scope="{row}">
                   <el-tag>{{row.tag}}</el-tag>
               </template>
           </el-table-column>
            <el-table-column label="运行状态" align="center" min-width="50">
               <template slot-scope="scope">
                   <el-tag :type="scope.row.status == '未运行' ? 'info':scope.row.status=='正在运行'?'success':'danger'">{{scope.row.status}}</el-tag>
                   <el-button size="mini" @click="Refresh" type="primary">刷新</el-button>
               </template>
           </el-table-column>
           <el-table-column label="数据操作" align="center" min-width="100">
               <template slot-scope="scope">
                   <el-button size="mini" type="primary" @click="AmendData(scope.$index)">修改信息</el-button>
                   <el-button size="mini" type="danger" @click="Experiment(scope.$index)">模型实验</el-button>
                   <el-button size="mini" type="warning" @click="ChooseType(scope.$index)">实验选择</el-button>
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
       <el-dialog :visible.sync="choose_data_dialog" title="选择实验数据">
           <el-checkbox-group v-model="selected_list">
                <el-checkbox v-for="item in choose_data" :key="item" :label="item"></el-checkbox>
           </el-checkbox-group>
           <div slot="footer">
               <el-button @click="choose_data_dialog=false">取消</el-button>
               <el-button @click="TrainExperiment" type="primary">确定</el-button>
           </div>
       </el-dialog>
       <el-dialog :visible.sync="choose_test_dialog" title="选择实验数据">
           <el-checkbox-group v-model="predict_list">
                <el-checkbox v-for="item in choose_data" :key="item" :label="item"></el-checkbox>
           </el-checkbox-group>
           <div slot="footer">
               <el-button @click="choose_test_dialog=false">取消</el-button>
               <el-button @click="PredictExperiment" type="primary">确定</el-button>
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
import { getLstmProject, addLstmProject, amendLstmProject, LstmProjectStart } from '@/api/model'
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
            choose_data_dialog: false,
            choose_test_dialog: false,
            LocationImage: false,
            form: {},
            choose_dialog: false,
            add_form: {
                project_id: '',
                name: ''
            },
            get_form: {
                project_id: '',
                plot_num: ''
            },
            url: '',
            image_loading: false,
            choose_item: ['未选择', '模型训练', '模型预测'],
            choose_data: ['人口', '人口密度', '自然增长率', '户数', '平均每户人口', '失业率', 'GDP', '人均GDP', 'GDP增长率'],
            selected_list: [],
            predict_list: [],
            tableshow: true,
            selected_project: null
        }
    },
    methods: {
        Select_Index:function(arr, item){
            for (let i=0; i<arr.length; i++){
                if (arr[i] === item){
                    return i;
                }
            }
            return -1;
        },
        PredictExperiment:function(){
            if (this.predict_list === []){
                this.$message.error('选择数据不能为空!')
            }
            else{
                this.choose_data_dialog = false
                let val = this.selected_project
                let that = this
                let data = {}
                let index_list = []
                data['project_id'] = this.page_data[val].project_id
                for (let i=0; i<this.predict_list.length; i++){
                    index_list.push(this.Select_Index(this.choose_data, this.predict_list[i]))
                }
                data['select_list'] = index_list.toString()
                data['type'] = '0'
                LstmProjectStart(data).then(res=>{
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
        TrainExperiment:function(){
            if (this.selected_list === []){
                this.$message.error('选择数据不能为空!')
            }
            else{
                this.choose_test_dialog = false
                let val = this.selected_project
                let that = this
                let data = {}
                let index_list = []
                data['project_id'] = this.page_data[val].project_id
                for (let i=0; i<this.selected_list.length; i++){
                    index_list.push(this.Select_Index(this.choose_data, this.selected_list[i]))
                }
                data['select_list'] = index_list.toString()
                data['type'] = '1'
                LstmProjectStart(data).then(res=>{
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
        ChooseType:function(index){
            let index_item=null;
            let msg = this.page_data[index].tag
            let data = this.page_data
            for (let i=0; i<this.choose_item.length; i++){
                if (this.choose_item[i]==msg){
                    index_item=i;
                    break;
                }
            }
            if (index_item === this.choose_item.length-1){
                index_item=0;
            }
            else{
                index_item++;
            }
            data[index].tag = this.choose_item[index_item]
            this.page_data = data
            this.table_loading = true
            this.tableshow = false
            setTimeout(() => {
                this.table_loading = false
                this.tableshow = true
            }, 100);
        },
        Refresh:function(){
            this.table_loading = true
            this.page_data = []
            this.tableData = []
            this.getData()
        },
        Experiment:function(val){
            if (this.page_data[val].tag === '未选择'){
                this.$message.error('请选择实验类型')
            }
            else if (this.page_data[val].tag === '模型训练'){
                this.choose_data_dialog = true
                this.selected_project = val
            }
            else{
                this.choose_test_dialog = true
                this.selected_project = val
            }
        },
        getData(){
            let that = this
            getLstmProject().then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    let size = that.page_size
                    let index = that.currentPage-1
                    for (let i=index*size; i<(index+1)*size; i++){
                        if (i==res.data.length){
                            break
                        }
                        res.data[i].tag = '未选择'
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
            amendLstmProject(data).then(res=>{
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
                addLstmProject(data).then(res=>{
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
