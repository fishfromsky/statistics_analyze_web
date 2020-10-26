<template>
    <div>
        <div class="header">
            <el-select v-model="selectId" placeholder="请选择算法ID" style="margin-left: 10px">
                <el-option v-for="item in selectlist" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
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
                    <el-card v-show="modelshow" style="margin-top: 20px"></el-card>
                </transition>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { algorithmlidlist, getbyidalgorithm } from '@/api/model'
import Mallki from '@/components/TextHoverEffect/Mallki'
export default {
    components:{
        Mallki
    },
    data(){
        return{
            selectId: null,
            selectlist: [],
            modeltext: '',
            modeldescribe: '',
            modelshow: false,
            username: ''
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
        }
    },
    methods:{
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
        }
    },
    mounted(){
        this.getID()
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
</style>