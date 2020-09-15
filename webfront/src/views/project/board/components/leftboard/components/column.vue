<template>
    <div>
        <div class="container">
            <el-button type="primary" icon="el-icon-document-add" @click="addData" class="add_btn">创建项目</el-button>
        </div>
        <el-dialog :visible.sync="add_dialog" title="创建项目">
            <el-form :model="form">
                <el-form-item label="项目编号">
                    <el-input v-model="form.project_id" type="number" placeholder="输入项目编号"></el-input>
                </el-form-item>
                <el-form-item label="项目名称">
                    <el-input v-model="form.name" placeholder="请输入您的项目名称"></el-input>
                </el-form-item>
                <el-form-item label="项目简介">
                    <el-input v-model="form.describe" placeholder="大概介绍一下您的项目吧"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="add_dialog = false">取 消</el-button>
                <el-button type="primary" @click="addDataConfirm">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import { addalgorithmlist } from '@/api/model'
export default {
    data(){
        return{
            add_dialog: false,
            form: {
                project_id: null,
                name: '',
                describe: ''
            }
        }
    },
    methods:{
        addData:function(){
            this.add_dialog = true
        },
        addDataConfirm:function(){
            let that = this
            if (this.form.project_id == null || parseInt(this.form.project_id) <= 0){
                this.$message.error('编号不能为空或小于等于0')
            }
            else if (this.form.name === ''){
                this.$message.error('项目名称不能为空')
            }
            else if (this.form.describe === ''){
                this.$message.error('项目描述不能为空')
            }
            else{
                addalgorithmlist(this.form).then(res=>{
                    if (res.code === 20000){
                        this.$message({
                            type: 'success',
                            message: '添加成功'
                        })
                        that.add_dialog = false
                        that.$emit('reload-table', that.form.project_id)
                    }
                })
            }
        }
    }
}
</script>

<style scoped>
    .container{
        width: 100%;
        height: 70px;
        background: #fff;
        box-shadow: 0 0 10px 10px rgba(153, 153, 153, 0.1);
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .add_btn{
        margin-left: 20px;
    }
</style>