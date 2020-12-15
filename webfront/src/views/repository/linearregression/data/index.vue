<template>
  <div>
    <column @child-event="handle_dialog" @id-event="handle_id" @download-event="handle_download"></column>
    <datatable :parentmsg="table_transfer_id" ref="datatable"></datatable>
    <el-dialog title="上传数据" :visible.sync="upload_dialog" width="80%">
      <div class="btn-column">
        <el-button @click="cancelInput">取消</el-button>
        <el-button @click="InputParameter" type="primary">上传</el-button>
        <el-select placeholder="项目编号" v-model="project_id" class="project_id">
            <el-option v-for="item in id_list" :key="item.project_id" :label="item.project_id" :value="item.project_id"></el-option>
        </el-select>
      </div>
      <uploadexcel v-if="!hasData" :on-success="handleSuccess" :before-upload="beforeUpload" style="margin-top: 20px"></uploadexcel>
      <el-table v-loading="table_loading" :data="tableData" border highlight-current-row style="width: 100%;margin-top:20px;">
        <el-table-column v-for="item of tableHeader" :key="item" :prop="item" :label="item" />
      </el-table>
    </el-dialog>
  </div>
</template>

<script>
import column from './components/column.vue'
import datatable from './components/table.vue'
import uploadexcel from './components/UploadFile.vue'
import { addlinearregressionparameter, getlinearregressionidlist } from '@/api/model'
export default {
  name: 'index',
  components: {
    column,
    datatable,
    uploadexcel
  },
  data(){
    return{
      table_loading: false,
      upload_dialog: false,
      hasData: false,
      tableData: [],
      tableHeader: [],
      project_id: '',
      id_list: [],
      table_transfer_id: ''
    }
  },
  methods: {
    get_project_id:function(){
      var that = this
      getlinearregressionidlist().then(res=>{
        let data = res.data
        for (let i=0; i<data.length; i++){
            that.id_list.push(data[i])
        }
      })
    },
    handle_dialog:function(data){
      this.upload_dialog = true
    },
    handle_download:function(){
      this.$refs.datatable.download()
    },
    handle_id: function(data){
      if (data !== ''){
        this.table_transfer_id = data
      }
    },
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
    cancelInput:function(){
      this.tableData = []
      this.tableHeader = []
      this.upload_dialog = false,
      this.hasData = false
    },
    DataInput(func){
      if (this.project_id === ''){
        this.$message.error('请选择项目编号')
      }
      else{
        var that = this;
        this.table_loading = true
        const table = []
        for (let i = 0; i < this.tableData.length; i++) {
          table.push(this.tableData[i])
        }
        const data = {}
        data['data'] = table
        data['project_id'] = this.project_id
        func(data).then(res => {
          that.table_loading = false
          if (res.code === 20000) {
            this.$message({
              type: 'success',
              message: '导入数据成功'
            })
          } else {
            this.$message.error(res.message)
            that.table_loading = false
          }
          that.tableData = []
          that.tableHeader = []
          that.hasData = false
        }).catch(res => {
          console.log(res)
          that.table_loading = false
          that.tableData = []
          that.tableHeader = []
          that.hasData = false
        })
      }
    },
    InputParameter:function(){
      this.DataInput(addlinearregressionparameter)
    },
  },
  mounted(){
    this.get_project_id()
  }
}
</script>

<style lang="less" scoped>
  .btn-column{
    width: 100%;
    height: 50px;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
</style>