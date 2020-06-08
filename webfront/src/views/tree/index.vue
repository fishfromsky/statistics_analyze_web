<template>
  <div class="app-container">
    <div class="main-content">
      <div class="input-content">
        <el-select v-model="level" placeholder="请选择数据级别" class="input-item">
          <el-option v-for="item in level_option"  :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <el-select v-model="kind" placeholder="请选择数据表类型" class="input-item">
          <el-option v-for="item in kind_option" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <div class="divider"></div>
        <el-button type="primary" icon="el-icon-download" class="input-item">导出数据</el-button>
      </div>
      <cityeconomy v-if="level == '1' && kind == '1'"></cityeconomy>
    </div>
  </div>
</template>

<script>
import cityeconomy from './components/cityeconomy'
export default {
  components: {
    cityeconomy
  },
  data() {
    return {
      level: '',
      kind: '',
      adddata_dialog: false,
      level_option: [
        {
          value: '1',
          label: '市级'
        }
      ],
      kind_option: [
        {
          value: '1',
          label: '经济数据'
        },
        {
          value: '2',
          label: '人口数据'
        },
        {
          value: '3',
          label: '生活垃圾处理'
        },
        {
          value: '4',
          label: '无害化处理厂数量'
        },
        {
          value: '5',
          label: '无害化处理能力'
        },
        {
          value: '6',
          label: '无害化处理量'
        }
      ],
    }
  },
  watch: {

  },
  methods: {
  
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
    margin-left: 20px;
  }
  .divider{
    width: 0;
    height: 30px;
    border-left: #aaa 1px solid;
    margin-left: 35px;
  }
</style>

