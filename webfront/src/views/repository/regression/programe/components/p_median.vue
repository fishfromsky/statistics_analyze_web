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
           <el-table-column label="实验类型" align="center" min-width="50">
               <template>
                   <el-tag type="primary">数据预测</el-tag>
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
       <el-dialog title="选择实验数据" :visible.sync="choose_dialog">
           <el-checkbox-group v-model="choose_list">
               <el-checkbox v-for="item in choose_data" :key="item" :label="item"></el-checkbox>
           </el-checkbox-group>
           <div slot="footer">
               <el-button @click="choose_dialog=false">取消</el-button>
               <el-button @click="ChooseConfirm" type="primary">确认</el-button>
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
import { getregression, addregression, amendregression, startregression, judgeregression } from '@/api/model'
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
            chooseIndex: null,
            choose_dialog: false,
            choose_data: ['人口', '人口密度', '住户数', '平均每户人口', '人均可支配收入', '人均消费支出', '公共支出', '基础设施投资','城市人口密度','绿植覆盖率',
            'GDP', '人均GDP', '第一产业', '第二产业','第三产业', '环保投资','大学生数','受教育程度'],
            choose_list: [],
        }
    },
    methods: {
        Refresh:function(){
            this.table_loading = true
            this.page_data = []
            this.tableData = []
            this.getData()
        },
        Select_Index:function(arr_main, arr_child){
            let index = []
            let flag = true
            for (let i=0; i<arr_main.length; i++){
                flag = true
                for (let j=0; j<arr_child.length; j++){
                    if (arr_main[i]===arr_child[j]){
                        flag=false
                        break
                    }
                }
                if (flag){
                    index.push(i)
                }
            }
            return index;
        },
        ChooseConfirm:function(){
            if (this.choose_list === []){
                this.$message.error('选择数据不能为空')
            }
            else{
                this.choose_dialog = false
                let val = this.chooseIndex
                let that = this
                let data = {}
                let index_list = []
                data['project_id'] = this.page_data[val].project_id
                index_list = this.Select_Index(this.choose_data, this.choose_list)
                data['index_list'] = index_list.toString()
                startregression(data).then(res=>{
                    if (res.code === 20000){
                        this.$message({
                            type:'success',
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
        Experiment:function(val){
            this.chooseIndex = val
            this.choose_dialog = true
            // startregression(data).then(res=>{
            //     if (res.code === 20000){
            //         that.$message({
            //             type: 'success',
            //             message: '运行成功'
            //         })
            //         that.table_loading = true
            //         that.page_data = []
            //         that.tableData = []
            //         that.getData()
            //     }
            // })
        },
        getData(){
            let that = this
            getregression().then(res=>{
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
            amendregression(data).then(res=>{
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
                addregression(data).then(res=>{
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
