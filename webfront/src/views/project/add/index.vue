<template>
    <div class="dashboard-container">
        <div class="header">
            <el-button type="primary" icon="el-icon-document-add" @click="addClick" style="margin-left: 20px">添加模型</el-button>
        </div>
        <el-table v-loading="table_loading" :data="page_data" stripe style="width: 100%; margin-top:20px">
            <el-table-column label="模型名称" align="center">
                <template slot-scope="{row}">
                    <span>{{row.name}}</span>
                </template>
            </el-table-column>
            <el-table-column label="项目分类" align="center">
                <template slot-scope="{row}">
                    <span>{{row.type}}</span>
                </template>
            </el-table-column>
            <el-table-column label="模型描述" align="center" :show-overflow-tooltip="true">
                <template slot-scope="{row}">
                    <span>{{row.description}}</span>
                </template>
            </el-table-column>
            <el-table-column label="模型图片" align="center">
                <template slot-scope="{row}">
                    <el-image :src="row.pic_url" :preview-src-list="[row.pic_url]" style="width: 70px; height: 50px"></el-image>
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
        <el-dialog :visible.sync="add_dialog" title="添加模型" width="30%">
            <el-form :model="add_form">
                <el-form-item label="模型名称">
                    <el-input v-model="add_form.name" placeholder="请输入模型名称"></el-input>
                </el-form-item>
                <el-form-item label="模型类型">
                    <el-select v-model="add_form.type" placeholder="请选择模型类型">
                        <el-option v-for="item in select_type" :key="item.value" :label="item.label" :value="item.value"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="模型描述">
                    <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4} " placeholder="请输入模型描述" v-model="add_form.describe"></el-input>
                </el-form-item>
                <span class="model_pic_span">上传模型图片</span>
                <el-upload
                    class="upload-demo"
                    action="http://101.133.238.216:8000/api/upload_img"
                    :on-remove="handleRemove"
                    :on-success="uploadSuccess"
                    :on-exceed="exceedFile"
                    :file-list="fileList"
                    :limit="1"
                    list-type="picture"
                    style="margin-top: 10px">
                    <el-button size="small" type="primary">点击上传</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
                </el-upload>
            </el-form>
            <div slot="footer">
               <el-button @click="add_dialog=false">取消</el-button>
               <el-button @click="AddConfirm" type="primary">确定</el-button>
           </div>
        </el-dialog>
    </div>
</template>

<script>
import { getallmodels, savemodels } from '@/api/model'
export default {
    data(){
        return{
            add_dialog: false,
            table_loading: false,
            tableData: [],
            page_data: [],
            total_size: 0,
            currentPage: 1,
            page_size: 10,
            add_form: {
                name: '',
                type: '',
                describe: '',
                pic_url: ''
            },
            select_type:[
                {value: '数据预测模型', value: '数据预测模型'},
                {value: '数据拟合模型', value: '数据聚类模型'},
                {value: '关联分析模型', value: '关联分析模型'}
            ],
            fileList: []
        }
    },
    methods:{
        uploadSuccess(res, file, fileList){
            this.add_form.pic_url = res.url
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        addClick:function(){
            this.add_dialog = true
        },
        AddConfirm:function(){
            let that = this
            if (this.add_form.name === '' || this.add_form.type === '' || this.add_form.describe === '' || this.add_form.pic_url === ''){
                this.$message.error('表格未完善或未上传图片')
            }
            else{
                savemodels(this.add_form).then(res=>{
                    if (res.code === 20000){
                        this.$message({
                            type: 'success',
                            message: '增加成功'
                        })
                        that.add_form.name=that.add_form.type=that.add_form.describe=that.add_form.pic_url=''
                        that.add_dialog = false
                        that.tableData = []
                        that.page_data = []
                        that.getData()
                    }
                })
            }
        },
        exceedFile:function(){
            this.$message.error('超出最大上传文件数')
        },
        getData:function(){
            let that = this
            this.table_loading = true
            getallmodels().then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    let size = that.page_size
                    let index = that.currentPage-1
                    let data = res.data
                    for (let i=index*size; i<(index+1)*size; i++){
                        if (i==data.length){
                            break
                        }
                        that.page_data.push(data[i])
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
        }
    },
    mounted(){
        this.getData()
    }
}
</script>

<style scoped lang="scss">
    .dashboard {
        &-container {
        margin: 30px;
        }
        &-text {
        font-size: 30px;
        line-height: 46px;
        }
    }
    .header{
        width: 100%;
        height: 60px;
        box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
        background: #fff;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .model_pic_span{
        font-weight: bold;
    }
</style>
