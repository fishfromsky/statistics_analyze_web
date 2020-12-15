<template>
    <div>
        <div class="header">
            <el-select v-model="selectId" placeholder="请选择算法ID" style="margin-left: 10px">
                <el-option v-for="item in selectlist" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
            <el-cascader v-model="rule" :options="rule_option" @change="ruleselect" placeholder="选择组合方式"
            :props="{ expandTrigger: 'hover' }" style="margin-left: 20px"></el-cascader>
        </div>
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="12">
                <transition name="el-zoom-in-top">
                    <el-card class="box-card-component" style="margin-top: 20px" v-show="modelshow">
                        <div slot="header" class="box-card-header">
                            <img src="../../../../image/AI_back.jpg">
                        </div>
                        <div class="card-header">
                            <div class="avatar-wrapper">
                                <img src="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif" class="user-avatar">
                            </div>
                            <span class="username">你好！{{username}}</span>
                        </div>
                        <div class="divider1"></div>
                        <div class="card-describe">
                            <div class="describe-box">
                                <span>算法名称:</span>
                                <mallki class-name="mallki-text" :text="modeltext" style="margin-top: 10px"/>
                            </div>
                        </div>
                        <div class="divider1" style="background: #3A71A8"></div>
                        <div class="card-describe">
                            <div class="describe-box">
                                <span style="color: #409eff">算法描述:</span>
                                <div class="record-text" style="margin-top: 10px">
                                    <span>{{modeldescribe}}</span>
                                </div>
                            </div>
                        </div>
                        <div class="divider1" style="background:#409eff"></div>
                    </el-card>
                </transition>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="12">
                <transition name="el-zoom-in-top">
                    <el-card v-show="modelshow" style="margin-top: 20px">
                        <div class="button-list">
                            <el-button type="primary" @click="startExperiment">开始实验</el-button>
                        </div>
                        <div v-for="item in modellist" :key="item.id">
                            <div class="model-container">
                                <div class="img-box">
                                    <img :src="item.pic_url">
                                </div>
                                <div class="title-box">
                                    <span>{{item.name}}</span>
                                </div>
                                <div class="delete-box" @click="DeleteModel(item.id)">
                                    <div class="delete-img">
                                        <img src="@/views/image/delete.png">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </el-card>
                </transition>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { algorithmlidlist, getbyidalgorithm, getinfomodel, addselectmodel, getmodelconstruction, deleteselectmodel } from '@/api/model'
import Mallki from '@/components/TextHoverEffect/Mallki'
import da from 'element-ui/src/locale/lang/da'
import { param } from 'jquery'
export default {
    components:{
        Mallki
    },
    props:{
        parentmsg: {
            type: Number,
            default: true
        }
    },
    data(){
        return{
            selectId: null,
            selectlist: [],
            modeltext: '',
            modeldescribe: '',
            modelshow: false,
            username: '',
            modellist: [],
            rule: [],
            rule_option:[
                {
                    value: '1',
                    label: '组合模板1',
                    children: [
                        {
                            value: '1',
                            label: '关联分析+多元回归'
                        },
                        {
                            value: '2',
                            label: '关联分析+LSTM'
                        }
                    ]
                },
                {
                    value: '2',
                    label: '组合模板2',
                    children: [
                        {
                            value: '1',
                            label: '聚类分析'
                        }
                    ]
                }
            ]
        }
    },
    watch:{
        selectId(val){
            let that = this
            let data = {}
            data['id'] = val
            getbyidalgorithm(data).then(res=>{
                if (res.code === 20000){
                    that.username = that.getCookie('environment_name')
                    that.modeltext = res.data.name
                    that.modeldescribe = res.data.describe
                    that.modelshow = true
                }
            })
            this.getmodelconstruction()
        },
        parentmsg(val){
            let that = this
            let data = {}
            data['model_id'] = val
            data['name'] = this.getCookie('environment_name')
            data['algorithm_id'] = this.selectId
            if (this.selectId === null){
                this.$message.error('请选择编辑算法的ID')
            }
            else{
                if (this.rule.length === 0){
                    this.$message.error('请选择组合方式')
                }
                else{
                    addselectmodel(data).then(res=>{
                        if (res.code === 20000){
                            this.$message({
                                type: 'success',
                                message: '添加成功'
                            })
                            that.getmodelconstruction()
                        }
                    })
                }
            }
        }
    },
    methods:{
        ruleselect:function(value){
            this.value = value
        },
        startExperiment:function(){
            let template_list = []
            for (let i=0; i<this.modellist.length; i++){
                template_list.push(this.modellist[i].sort_Id)
            }
            if (this.rule[0]==="1" && this.rule[1]==="1"){
                if (template_list[0]===3 && template_list[1]===1){
                    this.$router.push({
                        path: '/project/test',
                        query: {
                            username: this.getCookie('environment_name'),
                            algorithm_Id: this.selectId,
                            rule: this.rule
                        }
                    })
                }
                else{
                    this.$message.error('不符合模板规则')
                }
            }
            else if (this.rule[0]==="1" && this.rule[1]==="2"){
                if (template_list[0]===3 && template_list[1]===0){
                    this.$router.push({
                        path: '/project/test',
                        query: {
                            username: this.getCookie('environment_name'),
                            algorithm_Id: this.selectId,
                            rule: this.rule
                        }
                    })
                }
                else{
                    this.$message.error('不符合模板规则')
                }
            }
            else if (this.rule[0] === '2' && this.rule[1] === '1'){
                if (template_list[0]===2){
                    this.$router.push({
                        path: '/project/test',
                        query: {
                            username: this.getCookie('environment_name'),
                            algorithm_Id: this.selectId,
                            rule: this.rule
                        }
                    })
                }
                else{
                    this.$message.error('不符合模板规定')
                }
            }
        },
        DeleteModel:function(id){
            let that = this
            let data = {}
            data['model_id'] = id
            data['algorithm_id'] = this.selectId
            data['name'] = this.getCookie('environment_name')
            deleteselectmodel(data).then(res=>{
                if (res.code === 20000){
                    this.$message({
                        type: 'success',
                        message: '删除成功'
                    })
                    that.getmodelconstruction()
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
        getID:function(){
            let that = this
            let data = {}
            let cookie = this.getCookie('environment_name')
            data['username'] = cookie
            algorithmlidlist(data).then(res=>{
                if (res.code === 20000){
                    let data = res.data
                    let list = []
                    for (let i=0; i<data.length; i++){
                        list.push({value: data[i].project_id, label: data[i].project_id})
                    }
                    that.selectlist = list
                }
            })
        },
        getmodelconstruction:function(){
            let that = this
            let data = {}
            data['name'] = this.getCookie('environment_name')
            data['algorithm_id'] = this.selectId
            getmodelconstruction(data).then(res=>{
                if (res.code === 20000){
                    that.modellist = res.data
                }
            })
        }
    },
    mounted(){
        this.getID()
    },
    created(){
        let params = this.$route.query.id
        if (params != undefined){
            this.selectId = params
        }
    }

}
</script>

<style lang="scss" >
.username{
    font-size: 20px;
    font-weight: bold;
    color: #4AB7BD;
    margin-left: 20px;
}
.box-card-component{
  .el-card__header {
    padding: 0px!important;
  }
}
</style>
<style scoped lang="scss">
    .header{
        width: 100%;
        height: 70px;
        background: #fff;
        box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .describe-box{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .describe-box span{
        font-size: 16px;
        font-weight: bold;
        color: #3A71A8;
    }
    .box-card-component {
        .box-card-header {
            position: relative;
            height: 150px;
            img {
                width: 100%;
                height: 100%;
                transition: all 0.2s linear;
                &:hover {
                    transform: scale(1.1, 1.1);
                    filter: contrast(130%);
                }
            }
        }
    }
    .avatar-wrapper{
        width: 80px;
        height: 80px;
        margin-left: 10px;
        border-radius: 50%;
        padding: 10px;
        .user-avatar{
            width: 100%;
            height: 100%;
            border-radius: 50%;
        }
    }
    .card-header{
        width: 100%;
        height: 80px;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .divider1{
        margin-top: 10px;
        width: 90%;
        margin-left: 5%;
        height: 5px;
        border-top-left-radius: 2.5px;
        border-top-right-radius: 2.5px;
        border-bottom-left-radius: 2.5px;
        border-bottom-right-radius: 2.5px;
        background: #4AB7BD;
    }
    .card-describe{
        width: 100%;
        min-height: 50px;
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 20px;
    }
    .record{
        width: 63px;
        height: 63px;
        padding: 10px;
        border-radius: 50%;
        background: #409eff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .record img{
        width: 30px;
        height: 30px
    }
    .record-text{
        word-wrap:break-word;
        word-break:normal; 
    }
    .record-text span{
        font-weight: 500;
        font-size: 15px;
        color: #409eff;
    }
    .model-container{
        width: 100%;
        height: 80px;
        padding: 5px;
        border: 1px solid #ccc;
        border-radius: 5px;
        display: flex;
        flex-direction: row;
        margin-bottom: 20px;
    }
    .img-box{
        width: 30%;
        height: 100%;
    }
    .img-box img{
        width: 100%;
        height: 100%;
    }
    .title-box{
        width: 50%;
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .title-box span{
        font-size: 20px;
        color: #555;
        margin-left: 20px;
        font-weight: bold;
    }
    .delete-box{
        width: 20%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .delete-img{
        width: 20px;
        height: 20px;
        cursor: pointer;
        transition: all ease 0.2s;
    }
    .delete-img:hover{
        transform: scale(1.1);
    }
    .delete-img img{
        width: 100%;
        height: 100%;
    }
    .button-list{
        position: relative;
        width: 100%;
        min-height: 50px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
</style>