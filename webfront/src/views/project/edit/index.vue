<template>
    <div>
        <div class="dashboard-container">
            <el-row :gutter="20">
                <el-col :xs="24" :sm="24" :lg="16">
                    <mainbody></mainbody>
                </el-col>
                <el-col :xs="24" :sm="24" :lg="8">
                    <rightboard></rightboard>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import rightboard from './components/rightboard/index'
import mainbody from './components/mainbody/index'
export default {
    components:{
        rightboard,
        mainbody
    },
    data(){
        return{

        }
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