<template>
   <div>
       <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
           <el-table-column label="年份" align="center">
               <template slot-scope="{row}">
                   <span>{{row.year}}</span>
               </template>
           </el-table-column>
           <el-table-column label="厨余垃圾" align="center">
               <template slot-scope="{row}">
                   <span>{{row.cook}}</span>
               </template>
           </el-table-column>
           <el-table-column label="纸类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.paper}}</span>
               </template>
           </el-table-column>
           <el-table-column label="塑料类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.plastic}}</span>
               </template>
           </el-table-column>
           <el-table-column label="纺织类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.clothe}}</span>
               </template>
           </el-table-column>
           <el-table-column label="木竹类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.wood}}</span>
               </template>
           </el-table-column>
           <el-table-column label="灰土类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.ash}}</span>
               </template>
           </el-table-column>
           <el-table-column label="陶瓷砖瓦类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.china}}</span>
               </template>
           </el-table-column>
           <el-table-column label="玻璃类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.glass}}</span>
               </template>
           </el-table-column>
           <el-table-column label="金属类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.metal}}</span>
               </template>
           </el-table-column>
           <el-table-column label="其他" align="center">
               <template slot-scope="{row}">
                   <span>{{row.other}}</span>
               </template>
           </el-table-column>
           <el-table-column label="混合类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.mix}}</span>
               </template>
           </el-table-column>
           <el-table-column label="可回收物" align="center">
               <template slot-scope="{row}">
                   <span>{{row.recycle}}</span>
               </template>
           </el-table-column>
           <el-table-column label="可燃物" align="center">
               <template slot-scope="{row}">
                   <span>{{row.fire}}</span>
               </template>
           </el-table-column>
           <el-table-column label="数据操作" align="center">
               <template slot-scope="scope">
                   <el-button size="mini" type="primary" @click="AmendData(scope.$index)">修改</el-button>
                   <el-button size="mini" type="danger" @click="DeleteData(scope.$index)">删除</el-button>
               </template>
           </el-table-column>
       </el-table>
       <el-dialog :visible.sync="amend_dialog" title="修改数据" width="40%">
           <el-form :model="form">
               <el-form-item label="年份">
                   <el-input v-model="form.year" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="厨余垃圾">
                   <el-input v-model="form.cook" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="纸类">
                   <el-input v-model="form.paper" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="塑料类">
                   <el-input v-model="form.plastic" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="纺织类">
                   <el-input v-model="form.clothe" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="木竹类">
                   <el-input v-model="form.wood" auto-complete="off"></el-input>
               </el-form-item>
                <el-form-item label="灰土类">
                   <el-input v-model="form.ash" auto-complete="off"></el-input>
               </el-form-item>
                <el-form-item label="陶瓷砖瓦类">
                   <el-input v-model="form.china" auto-complete="off"></el-input>
               </el-form-item>
                <el-form-item label="玻璃类">
                   <el-input v-model="form.glass" auto-complete="off"></el-input>
               </el-form-item>
                <el-form-item label="金属类">
                   <el-input v-model="form.metal" auto-complete="off"></el-input>
               </el-form-item>
                <el-form-item label="其他">
                   <el-input v-model="form.other" auto-complete="off"></el-input>
               </el-form-item>
                <el-form-item label="混合类">
                   <el-input v-model="form.mix" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="可回收类">
                   <el-input v-model="form.recycle" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="可燃物">
                   <el-input v-model="form.fire" auto-complete="off"></el-input>
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
               <el-form-item label="厨余垃圾">
                   <el-input v-model="add_form.cook" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="纸类">
                   <el-input v-model="add_form.paper" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="橡塑类">
                   <el-input v-model="add_form.plastic" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="纺织类">
                   <el-input v-model="add_form.clothe" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="木竹类">
                   <el-input v-model="add_form.wood" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="灰土类">
                   <el-input v-model="add_form.ash" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="砖瓦陶瓷类">
                   <el-input v-model="add_form.china" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="玻璃类">
                   <el-input v-model="add_form.glass" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="金属类">
                   <el-input v-model="add_form.metal" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="其他类">
                   <el-input v-model="add_form.else" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="混合类">
                   <el-input v-model="add_form.mix" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="可回收类">
                   <el-input v-model="add_form.recycle" auto-complete="off"></el-input>
               </el-form-item>
               <el-form-item label="可燃物">
                   <el-input v-model="add_form.fire" auto-complete="off"></el-input>
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
import { getgarbageelement, amendelementgarbage, deleteelementgarbage, addelementbyrow } from '@/api/model'
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
            getgarbageelement().then(res=>{
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
            amendelementgarbage(data).then(res=>{
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
            deleteelementgarbage(this.delete_form).then(res=>{
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
            addelementbyrow(data).then(res=>{
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
