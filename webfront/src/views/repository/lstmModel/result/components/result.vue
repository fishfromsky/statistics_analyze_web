<template>
    <div>
        <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
            <el-table-column label="年份" align="center">
                <template slot-scope="{row}">
                    <span>{{row.year}}</span>
                </template>
            </el-table-column>
            <el-table-column label="实际值" align="center">
                <template slot-scope="{row}">
                    <span>{{row.real}}</span>
                </template>
            </el-table-column>
            <el-table-column label="预测值" align="center">
                <template slot-scope="{row}">
                    <span>{{row.pred}}</span>
                </template>               
            </el-table-column>
            <el-table-column label="实验时间" align="center">
                <template slot-scope="{row}">
                    <i class="el-icon-time"></i>
                    <span>{{row.time}}</span>
                </template>
            </el-table-column>
            <el-table-column label="实验编号" align="center">
                <template slot-scope="{row}">
                    <span>{{row.sort}}</span>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog :visible.sync="chart_dialog">
            <chartresult :chart-data="graph_data"></chartresult>
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
import { getlstmresult } from '@/api/model'
import chartresult from './components/resultchart'
export default {
    components:{
        chartresult
    },
    props:{
        projectId:{
            type: String,
            required: true
        }
    },
    data(){
        return{
            chart_dialog: false,
            table_loading: false,
            tablekey: 0,
            tableData: [],
            page_data: [],
            total_size: 0,
            currentPage: 1,
            page_size: 10,
            project_id: '',
            filename: 'lstm_result',
            autoWidth: true,
            bookType: 'xlsx',
            sort_list: [],
            graph_data:{
                real: [],
                pred: [],
                year: []
            }
        }
    },
    watch:{
        projectId:function(a, _){
            this.project_id = a
            this.initTable(a)
            this.page_data = []
            this.tableData = []
            this.sort_list = []
        }
    },
    methods:{
        showChart:function(id){
            this.graph_data.real = []
            this.graph_data.pred = []
            this.graph_data.year = []
            this.chart_dialog = true
            let chart_data = this.tableData
            for (let i=0; i<chart_data.length; i++){
                if (chart_data[i].sort === id){
                    this.graph_data.real.push(chart_data[i].real)
                    this.graph_data.pred.push(chart_data[i].pred)
                    this.graph_data.year.push(chart_data[i].year)
                }
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
        handleSizeChange:function(val){
            this.table_loading = true
            this.page_size = val
            this.currentPage = 1
            this.page_data = []
            this.initTable(this.project_id)
        },
        handleCurrentChange:function(val){
            this.currentPage = val
            this.page_data = []
            this.initTable(this.project_id)
        },
        initTable:function(id){
            let that = this
            let dict = {}
            dict['project_id'] = id
            getlstmresult(dict).then(res=>{
                that.table_loading = false
                that.tableData = res.data
                for (let i=0; i<res.data.length; i++){
                    let time = res.data[i].time
                    time = new Date(time.replace(/-/g,'/')).getTime()+3600*1000*8
                    res.data[i].time = that.timeStamptoTime(time)
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
                for (let i=0; i<that.tableData.length; i++){
                    if (!that.isInArray(that.sort_list, that.tableData[i].sort)){
                        that.sort_list.push(that.tableData[i].sort)
                    }
                }
                that.$emit('child-event', that.sort_list)
            })
        },
        isInArray:function(arr,value){
            for(var i = 0; i < arr.length; i++){
                if(value === arr[i]){
                    return true;
                }
            }
            return false;
        },
        formatJson(filterVal, jsonData) {
            return jsonData.map(v => filterVal.map(j => {
                if (j === 'timestamp') {
                return parseTime(v[j])
                } else {
                return v[j]
                }
            }))
        },
        download:function(){
            import('@/vendor/Export2Excel').then(excel => {
                const tHeader = ['Year', 'Real', 'Prediction', 'DateTime']
                const filterVal = ['year', 'real', 'pred', 'time']
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
        }
    },
    mounted(){

    }
}
</script>

<style scoped>

</style>