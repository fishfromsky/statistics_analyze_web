<template>
    <div>
        <el-table v-loading="table_loading" :data="page_data" stripe style="width: 100%; margin-top:20px">
            <el-table-column label="项目编号" width="60" align="center">
                <template slot-scope="{row}">
                    <span>{{row.project_id}}</span>
                </template>
            </el-table-column>
            <el-table-column label="项目名称" align="center">
                <template slot-scope="{row}">
                    <span>{{row.name}}</span>
                </template>
            </el-table-column>
            <el-table-column label="实验次数" width="60" align="center">
                <template slot-scope="{row}">
                    <span>{{row.time}}</span>
                </template>
            </el-table-column>
            <el-table-column label="项目描述" align="center">
                <template slot-scope="{row}">
                    <span>{{row.describe}}</span>
                </template>
            </el-table-column>
            <el-table-column label="添加时间" align="center">
                <template slot-scope="{row}">
                    <span>{{row.add_time}}</span>
                </template>
            </el-table-column>
            <el-table-column>
                <template slot-scope="scope">
                    <el-button size="mini" type="primary" @click="editAlgorithm(scope.$index)">编辑</el-button>
                    <el-button size="mini" type="danger" @click="deleteProject(scope.$index)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[10, 20, 30, 40, 50]"
            :page-size="page_size"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total_size"
            style="margin-top: 20px; margin-left: 2.5%">
        </el-pagination>
        <el-dialog :visible.sync="delete_dialog" title="删除提示">
            <div style="font-size: 20px">确定删除该项目吗？</div>
            <div style="font-size: 15px; margin-top: 20px">删除后，该项目所有实验数据将同步被删除</div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="delete_dialog = false">取 消</el-button>
                <el-button type="danger" @click="deleteConfirm">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import { getalgorithmlist, deletealgorithmlist } from '@/api/model'
export default {
    props:{
        parentmsg:{
            type: String,
            required: true
        }
    },
    data(){
        return{
            delete_dialog:false,
            table_loading: false,
            tableData: [],
            page_data: [],
            total_size: 0,
            currentPage: 1,
            page_size: 10,
            delete_id: null
        }
    },
    watch: {
        parentmsg:function(a, _){
            this.tableData = []
            this.page_data = []
            this.getData()
        }
    },
    methods: {
        editAlgorithm:function(index){
            let algorithm_id = this.page_data[parseInt(index)].project_id
            this.$router.push({
                path: '/project/select',
                query: {
                    id: algorithm_id
                }
            })
        },
        getCookie:function(name){
            var strcookie = document.cookie;
            var arrcookie = strcookie.split("; ");
            for ( var i = 0; i < arrcookie.length; i++) {
                var arr = arrcookie[i].split("=");
                if (arr[0] == name){
                    return arr[1];
                }
            }
            return "";
        },
        getData:function(){
            let that = this
            this.table_loading = true
            let data = {}
            data['name'] = this.getCookie('environment_name')
            getalgorithmlist(data).then(res=>{
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
        deleteProject:function(id){
            this.delete_id = this.page_data[parseInt(id)].project_id
            this.delete_dialog = true
        },
        deleteConfirm:function(){
            let that = this
            let dict = {}
            dict['project_id'] = this.delete_id
            deletealgorithmlist(dict).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: '删除成功'
                    })
                    that.delete_dialog = false
                    that.page_data = []
                    that.tableData = []
                    that.getData()
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
        }
    },
    mounted(){
        this.getData()
    }
}
</script>

<style scoped>

</style>