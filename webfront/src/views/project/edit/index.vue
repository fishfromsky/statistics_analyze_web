<template>
    <div>
        <div class="dashboard-container">
            <el-row :gutter="20">
                <el-col :xs="24" :sm="24" :lg="16">
                    <mainbody :parentmsg="modelId"></mainbody>
                </el-col>
                <el-col :xs="24" :sm="24" :lg="8">
                    <rightboard @child-event="handleChild"></rightboard>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import rightboard from './components/rightboard/index'
import mainbody from './components/mainbody/index'
import { getparameterkmeans } from '@/api/model'
import { param } from 'jquery'
export default {
    components:{
        rightboard,
        mainbody
    },
    data(){
        return{
            modelId: null,
            selectId: null
        }
    },
    methods:{
        handleChild:function(data){
            this.modelId = data
        }
    },
    created(){
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
</style>