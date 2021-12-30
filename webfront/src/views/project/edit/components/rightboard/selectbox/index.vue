<template>
    <div>
        <div class="select-box">
            <div class="choose-item" v-for="(item, index) in choose_item" :key="index" :class="item.color" @click="handleClick(item.value)">
                <span>{{item.label}}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    components: {
    },
    data(){
        return{
            choose_item:[
                {
                    value: '1',
                    label: '数据预测模型',
                    color: 'pan-btn light-blue-btn'
                },
                {
                    value: '2',
                    label: '数据聚类模型',
                    color: 'pan-btn green-btn'
                },
                {
                    value: '3',
                    label: '关联分析模型',
                    color: 'pan-btn tiffany-btn'
                }
            ]
        }
    },
    methods:{
        handleClick:function(id){
            this.$emit('child-event', id)
        }
    }
}
</script>

<style lang="scss">
    .select-box{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .choose-item{
        width: 90%;
        margin: 0 auto;
        margin-top: 20px;
        cursor: pointer;
        &-option {
            width: 100%;
            height: 50px;
            position: relative;
        }
    }
</style>