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
export default {
    props:{
        parentmsg: {
            type: String,
            required: true
        }
    },
    data(){
        return{
            algorithm_item: [
                {
                    name: 'LSTM模型',
                    pic_url: require('@/views/image/lstm.jpg'),
                    description: '长短期记忆（Long short-term memory, LSTM）是一种特殊的RNN，主要是为了解决长序列训练过程中的梯度消失和梯度爆炸问题。简单来说，就是相比普通的RNN，LSTM能够在更长的序列中有更好的表现',
                    color: 'light-blue-btn'
                },
                {
                    name: '多元回归模型',
                    pic_url: require('@/views/image/regression.jpg'),
                    description: '多元回归分析(Multiple Regression Analysis)是指在相关变量中将一个变量视为因变量，其他一个或多个变量视为自变量，建立多个变量之间线性或非线性数学模型数量关系式并利用样本数据进行分析的统计分析方法',
                    color: 'tiffany-btn'
                }
            ]
        }
    },
    watch:{
        
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