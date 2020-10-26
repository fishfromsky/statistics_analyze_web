<template>
    <div class="card-container">
        <div v-for="(item, index) in algorithm_item" :key="index">
            <div class="card" :class="item.color">
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
        </div>
    </div>
</template>

<script>
import { filtermodels } from '@/api/model'
export default {
    props:{
        parentmsg: {
            type: String,
            required: true
        }
    },
    data(){
        return{
            algorithm_item: []
        }
    },
    methods:{
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
</style>