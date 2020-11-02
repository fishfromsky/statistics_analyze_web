<template>
    <div class="card-container">
        <div v-for="(item, index) in algorithm_item" :key="index">
            <el-tooltip class="item" effect="dark" content="点击卡片进行添加" placement="top-start">
                <div class="card" :class="item.color" @click="selectConfirm(item.id)">
                    <el-row :gutter="10">
                        <el-col :span="8">
                            <el-image class="card-img" :src="item.pic_url" fit="fill"></el-image>
                        </el-col>
                        <el-col :span="16">
                                <div class="card-title">{{item.name}}</div>
                                <div class="divider"></div>
                                <div class="card-detail">{{item.description}}</div>
                        </el-col>
                    </el-row>
                </div>
            </el-tooltip>
        </div>
        <el-dialog title="增加模型" :visible.sync="add_dialog">
            <div class="dialog_title">
                <span>您将要添加以下模型到您的算法中，请予以确认</span>
            </div>
            <div class="main-dialog">
                <div class="main-dialog-img">
                    <img :src="model_info.pic_url">
                </div>
                <div class="dialog-title">
                    <span class="dialog-model-name">{{model_info.name}}</span>
                    <div class="divider1"></div>
                    <span class="dialog-model-describe">{{model_info.description}}</span>
                </div>
            </div>
            <div slot="footer">
                <el-button @click="add_dialog=false">取消</el-button>
                <el-button type="primary" @click="addConfirm">确认添加</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
import { filtermodels, getinfomodel } from '@/api/model'
export default {
    props:{
        parentmsg: {
            type: String,
            required: true
        }
    },
    data(){
        return{
            algorithm_item: [],
            addmodelId: null,
            add_dialog: false,
            model_info: {}
        }
    },
    methods:{
        addConfirm:function(){
            this.$emit('child-event', this.addmodelId)
            this.add_dialog = false
        },
        selectConfirm:function(id){
            let that = this
            this.addmodelId = id
            let data = {}
            data['id'] = id
            getinfomodel(data).then(res=>{
                if (res.code === 20000){
                    that.model_info = res.data[0]
                }
            })
            this.add_dialog = true
        },
        getData:function(){
            let color = ['light-blue-btn', 'tiffany-btn', 'green-btn', 'yellow-btn', 'pink-btn']
            let that = this
            let data = {}
            if (this.parentmsg === '1'){
                data['type'] = '数据预测模型'
            }
            else if (this.parentmsg === '2'){
                data['type'] = '数据聚类模型'
            }
            else if (this.parentmsg === '3'){
                data['type'] = '关联分析模型'
            }
            filtermodels(data).then(res=>{
                if (res.code === 20000){
                    let results = res.data
                    for (let i=0; i<results.length; i++){
                        results[i].color = color[i%results.length]
                        that.algorithm_item.push(results[i])
                    }
                }
            })
        }
    },
    watch:{
        
    },
    mounted(){
        this.getData()
    }
}
</script>

<style scoped>
    .card-container{
        width: 100%;
        min-width: 100%;
        padding: 20px;
    }
    .card{
        width: 100%;
        min-height: 120px;
        margin: 0 auto;
        margin-top: 20px;
        border-radius: 5px;
        padding: 5px;
        cursor: pointer;
        transition: all ease 0.5s;
    }
    .card:hover{
        transform: scale(1.05);
    }
    .card-img{
        width: 90%;
        height: 100px;
        margin-top: 10px;
        margin-left: 10px;
    }
    .card-content{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .card-title{
        font-size: 18px;
        font-weight: bold;
        color: #fff;
        margin-top: 10px;
    }
    .divider{
        width: 100%;
        height: 0;
        border-top: 1px solid #fff;
        margin-top: 5px;
    }
    .card-detail{
        font-size: 12px;
        color: #fff;
        margin-top: 5px;
    }
        .dialog_title{
        width: 100%;
        height: 30px;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .dialog_title span{
        font-size: 15px;
        color: #555;
        font-weight: bold;
    }
    .main-dialog{
        margin-top: 20px;
        width: 100%;
        min-height: 200px;
        display: flex;
        flex-direction: row;
    }
    .main-dialog-img{
        width: 30%;
        height: 150px;
        box-shadow:  0 0 10px 5px rgba(153, 153, 153, 0.2);
    }
    .main-dialog-img img{
        width: 100%;
        height: 100%;
    }
    .dialog-title{
        width: 60%;
        margin-left: 20px;
        display: flex;
        flex-direction: column;
    }
    .divider1{
        width: 100%;
        height: 0;
        border-top: 2px solid #333;
    }
    .dialog-model-name{
        font-size: 20px;
        color: #555;
        font-weight: bold;
        margin-bottom: 10px;
        margin-left: 20px;
    }
    .dialog-model-describe{
        margin-top: 10px;
    }
</style>