<template>
  <div class="app-container">
    <upload-excel-component v-if="!hasData" :on-success="handleSuccess" :before-upload="beforeUpload" />
    <div v-else class="save-list">
      <div class="data-list">
        <div class="model-name">
          <span class="name-span">模型名称</span>
          <el-input v-model="modelname" class="name-input" placeholder="输入添加模型的名称"></el-input>
        </div>
        <div class="model-name">
          <span class="name-span">模型评分</span>
          <el-rate v-model="star" :max="5" class="rate"></el-rate>
        </div>
        <el-button type="primary" icon="el-icon-circle-plus-outline" class="addmodel-btn" @click="AddModel">添加模型</el-button>
      </div>
    </div>
    <el-table v-loading="table_loading" :data="tableData" border highlight-current-row style="width: 100%;margin-top:20px;">
      <el-table-column v-for="item of tableHeader" :key="item" :prop="item" :label="item" />
    </el-table>
  </div>
</template>

<script>
import UploadExcelComponent from './components/UploadFile'
import { getName } from '@/utils/auth'
import { addmodel } from '@/api/model'
export default {
  name: 'UploadExcel',
  components: { UploadExcelComponent },
  data() {
    return {
      tableData: [],
      tableHeader: [],
      hasData: false,
      modelname: '',
      star: null,
      table_loading: false
    }
  },
  methods: {
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1

      if (isLt1M) {
        return true
      }
      this.$message({
        message: 'Please do not upload files larger than 1m in size.',
        type: 'warning'
      })
      return false
    },
    handleSuccess({ results, header }) {
      this.tableData = results
      this.tableHeader = header
      this.hasData = true
    },
    AddModel:function () {
      var that = this;
      if (that.modelname === ''){
          that.$message.error('模型名称不能为空')
      }
      else if (that.star === null || that.star === 0){
          that.$message.error('模型评分至少为1星')
      }
      else{
          let name = getName();
          let data = {};
          data['author'] = name;
          data['name'] = that.modelname;
          data['star'] = that.star;
          addmodel(data).then(res=>{
              if (res.code === 20000){
                  that.table_loading = true;
                  setTimeout(function () {
                      that.table_loading = false;
                      that.$message({
                          message: '添加成功',
                          type: 'success'
                      })
                  },1000)
              }
          })
      }
    }
  }
}
</script>
<style scoped>
  .save-list{
    width: 100%;
    height: 160px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .data-list{
    margin: 0 auto;
    width: 100%;
    height: 80px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .model-name{
    width: 300px;
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    float: left;
    margin-left: 20px;
  }
  .name-span{
    float: left;
    margin-left: 20px;
    color: #5a5e66;
    font-size: 15px;
  }
  .name-input{
    width: 200px;
    float: left;
    margin-left: 20px;
  }
  .rate{
    margin-left: 20px;
  }
  .addmodel-btn{
    float: left;
    margin-left: 20px;
  }
</style>
