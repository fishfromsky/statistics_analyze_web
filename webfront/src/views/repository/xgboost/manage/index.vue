<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="16">
        <div class="main-content">
          <div class="input-content">
            <el-select v-model="kind" placeholder="请选择项目类型" class="input-item">
              <el-option v-for="item in kind_option" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <div class="divider"></div>
            <el-button  type="primary" icon="el-icon-upload2" @click="addData" style="margin-left: 20px">添加项目</el-button>
          </div>
          <tabledata v-if="kind == '1'" ref="tabledata"></tabledata>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="table-box">
          <div class="box-title">
            <span class="box-title-span">xgboost实验数据上传</span>
          </div>
          <el-upload
            class="upload-demo"
            action="http://101.133.238.216:8000/api/uploadxgboostfile"
            :file-list="fileList"
            :on-error="handleError"
            :on-success="handleSuccess"
          >
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">
              上传数据文件，仅限excel文件
            </div>
          </el-upload>
          <div class="box-title" style="margin-top: 10px">
            <span class="box-title-span">数据上传历史</span>
          </div>
          <el-table
            :data="tableData"
            v-loading="table_loading"
            border
            style="margin-top: 20px"
          >
            <el-table-column
              label="日期"
              width="150"
              prop="time"
            ></el-table-column>
            <el-table-column label="文件名" prop="name"></el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
              <template slot-scope="scope">
                <el-button
                  @click="handleDownload(scope.$index)"
                  type="text"
                  size="small"
                  >下载</el-button
                >
                <el-button
                  @click="handleDelete(scope.$index)"
                  type="text"
                  size="small"
                  >删除</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import tabledata from './components/tabledata'

import { getxgboostfilelist, deletemodelfile } from '@/api/model'

export default {
  components: {
    tabledata
  },
  data() {
    return {
      level: '',
      kind: '',
      kind_option: [
        {
          value: '1',
          label: 'xgboost项目'
        }
      ],
      tableData: [],
      table_loading: false,
      fileList: [],
    }
  },
  watch: {

  },
  methods: {
    handleSuccess: function () {
      this.getFileList();
    },
    handleError:function(){
      this.$message.error('上传文件失败')
    },
    handleDownload(val){
      window.open('http://101.133.238.216:8000/'+this.tableData[val].path)
    },
    handleDelete(val){
      let that = this
      let data = {}
      data['url'] = this.tableData[val].path
      deletemodelfile(data).then(res=>{
        if (res.code === 20000){
          this.$message({
            type: 'success',
            message: '删除成功'
          })
          that.getFileList()
        }
      })
    },
    getFileList: function () {
      let that = this;
      this.tableData = [];
      this.table_loading = true;
      getxgboostfilelist().then((res) => {
        if (res.code === 20000) {
          let data = res.data;
          that.table_loading = false;
          for (let i = 0; i < data.length; i++) {
            let dict = {};
            dict["index"] = i;
            dict["name"] = data[i].name;
            dict["path"] = data[i].url;
            let splttime = data[i].url.split("/");
            dict["time"] =
              splttime[splttime.length - 4] +
              "年" +
              splttime[splttime.length - 3] +
              "月" +
              splttime[splttime.length - 2] +
              "日";
            that.tableData.push(dict);
          }
        }
      });
    },
    addData() {
      if (this.kind === ''){
        this.$message.error('请选择项目编号')
      }
      else{
        this.$refs.tabledata.addPrograme()
      }
    }

  },
  mounted() {
    this.getFileList()
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
  .main-content{
    position: relative;
    width: 100%;
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
  .table-box {
    width: 100%;
    min-height: 400px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
    padding: 10px;
  }
  .box-title {
    width: 100%;
    height: 40px;
    &-span {
      color: #4AB7BD;
      font-size: 20px;
      font-weight: bold;
    }
  }
  .col_dialog {
    width: 100%;
    min-height: 100px;
    display: flex;
    flex-direction: column;
  }
</style>

