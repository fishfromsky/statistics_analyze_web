<template>
  <div>
    <div class="dashboard-container">
        <el-row :gutter="20">
            <el-col :xs="24" :sm="24" :lg="24">
                <leftboard></leftboard>
            </el-col>
        </el-row>
    </div>
  </div>
</template>

<script>
import leftboard from './components/leftboard/index'
export default {
    components:{
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