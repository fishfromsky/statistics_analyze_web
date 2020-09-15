<template>
  <div>
    <div class="dashboard-container">
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="17">
                <leftboard></leftboard>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="7">
                <rightboard></rightboard>
            </el-col>
        </el-row>
    </div>
  </div>
</template>

<script>
import rightboard from './components/rightboard/index'
import leftboard from './components/leftboard/index'
export default {
    components:{
        rightboard,
        leftboard
    },
    data(){
        return {

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