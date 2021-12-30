<template>
    <div>
        <div class="container">
            <div class="header-item" @click="select_status = true">
                <mallki class-name="mallki-text" text="算法搭配区域"/>
            </div>
            <transition name="fade" mode="out-in">
                <selectbox v-if="select_status" @child-event="handleChild"></selectbox>
                <algorithm v-else  @child-event="handleChildEvent" :parentmsg="select_id"></algorithm>
            </transition>
        </div>
    </div>
</template>

<script>
import Mallki from '@/components/TextHoverEffect/Mallki'
import selectbox from './selectbox/index'
import algorithm from './selectbox/algorithm'
export default {
    components: {
        Mallki,
        selectbox,
        algorithm
    },
    data(){
        return{
            select_status: true,
            select_id: ''
        }
    },
    methods:{
        handleChildEvent:function(data){
            this.$emit('child-event', data)
        },
        handleChild:function(msg){
           if (msg === '1'){
               this.select_id = '1'
               this.select_status = false
            }
            else if (msg === '2'){
                this.select_id = '2'
                this.select_status = false
            }
            else if (msg === '3'){
                this.select_id = '3'
                this.select_status = false
            }
        }
    }
}
</script>

<style scoped>
    .container{
        width: 100%;
        min-height: 600px;
        background: #eef1f6;
        box-shadow: 0 0 10px 10px rgba(153, 153, 153, 0.1);
    }
    .header-item{
        width: 100%;
        min-height: 50px;
        background: #eef1f6;
        border-bottom: 1px #ccc solid;
        padding: 10px;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
</style>