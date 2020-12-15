<template>
  <div class="app-container">
    <div class="main-content">
      <div class="input-content">
        <el-select v-model="kind" placeholder="请选择项目类型" class="input-item">
          <el-option v-for="item in kind_option" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <div class="divider"></div>
        <el-button  type="primary" icon="el-icon-upload2" @click="addData" style="margin-left: 20px">添加项目</el-button>
      </div>
      <pmedian v-if="kind == '1'" ref="p_median"></pmedian>
    </div>
  </div>
</template>

<script>
import pmedian from './components/p_median'

export default {
  components: {
    pmedian
  },
  data() {
    return {
      level: '',
      kind: '',
      kind_option: [
        {
          value: '1',
          label: '多元线性回归'
        }
      ],
    }
  },
  watch: {

  },
  methods: {
    addData() {
      if (this.kind === ''){
        this.$message.error('请选择项目编号')
      }
      else{
        this.$refs.p_median.addPrograme()
      }
    }

  },
  mounted() {

  }
}
</script>
<style scoped>
  .main-content{
    position: relative;
    width: 98%;
    min-height: 100px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    margin: 0 auto;
    padding: 10px 10px;
  }
  .input-content{
    height: 40px;
    margin-top: 20px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .input-item{
    float: left;
    margin-left: 35px;
  }
  .divider{
    width: 0;
    height: 30px;
    border-left: #aaa 1px solid;
    margin-left: 35px;
  }
</style>

