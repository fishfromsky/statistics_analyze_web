<template>
  <div class="app-container">
    <div class="main-content">
      <div class="input-content">
        <el-select v-model="kind" placeholder="请选择数据表类型" class="input-item">
          <el-option v-for="item in kind_option" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <div class="divider"></div>
        <el-button type="primary" icon="el-icon-download" class="input-item">导出数据</el-button>
                   <el-button  type="info" icon="el-icon-upload2" @click="addData" style="text-align: center" plain>添加数据</el-button>
      </div>
      <p_median v-if="kind == '1'" ref="p_median"></p_median>
    </div>
  </div>
</template>

<script>
import p_median from './components/p_median'

export default {
  components: {
    p_median
  },
  data() {
    return {
      level: '',
      kind: '',
      adddata_dialog: false,

      kind_option: [
        {
          value: '1',
          label: 'p_median项目'
        }
      ],
    }
  },
  watch: {

  },
  methods: {
    addData() {
      this.$refs.p_median.addData()
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

