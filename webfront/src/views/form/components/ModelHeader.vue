<template>
    <div>
      <div class="divider"></div>
      <div class="model-container">
        <el-input type="number" placeholder="输入模型编号" class="number-input" v-model="number"></el-input>
        <el-button type="primary" @click="ModelConfirm" class="confirm-btn">确认</el-button>
      </div>
    </div>
</template>

<script>
    export default {
        name: "ModelHeader",
        data(){
          return{
            number:''
          }
        },
      methods:{
          ModelConfirm:function () {
            if (this.number === ''){
              this.$message.error('请输入模型编号')
            }
            else{
              this.$emit('event1', this.number)
            }
          }
      }
    }
</script>

<style scoped>
  .divider{
    width: 100%;
    height: 0;
    border-top: #ddd 1px solid;
  }
  .model-container{
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 10px 10px;
    background: #fff;
  }
  .number-input{
    width: 200px;
    float: left;
    margin-left: 10px;
  }
  .confirm-btn{
    float: left;
    margin-left: 20px;
  }
</style>
