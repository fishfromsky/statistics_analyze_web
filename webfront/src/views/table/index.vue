<template>
  <div class="app-container">
    <upload-excel-component v-if="!hasData" :on-success="handleSuccess" :before-upload="beforeUpload" />
    <div v-else class="save-list">
      <div class="data-list">
        <div class="model-name">
          <span class="name-span">数据级别</span>
          <el-select v-model="area" placeholder="选择数据级别" class="name-input">
            <el-option v-for="item in level_list" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
        </div>
        <div class="model-name">
          <span class="name-span">数据类型</span>
          <el-select v-model="kind" placeholder="请输入具体表项类型" class="rate">
            <el-option v-for="item in kind_list" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
        </div>
        <el-button type="primary" icon="el-icon-document-add" class="addmodel-btn" @click="AddModel">导入数据</el-button>
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
import { addcityeconomydata, addcitypopulationdata, addgarbagecity, addcitygarbagedeal, addcitygarbagecapacity, addcitygarbagevolume, addfacorylist, addtransferfactory, addcollectfactory, addelementgarbage } from '@/api/model'
export default {
  name: 'UploadExcel',
  components: { UploadExcelComponent },
  data() {
    return {
      tableData: [],
      tableHeader: [],
      hasData: false,
      area: '',
      kind: '',
      level_list: [
        {
          value: '1',
          label: '市级'
        }
        // {
        //     value: '2',
        //     label: '区级'
        // },
        // {
        //     value: '3',
        //     label: '乡级'
        // }
      ],
      kind_list: [
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
        },
        {
          value: '7',
          label: '无害化处理厂信息'
        },
        {
          value: '8',
          label: '垃圾中转站信息'
        },
        {
          value: '9',
          label: '垃圾收集点信息'
        },
        {
          value: '10',
          label: '固废成分信息'
        }
      ],
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
    DataInput(func){
      var that = this;
      this.table_loading = true
      const table = []
      for (let i = 0; i < this.tableData.length; i++) {
        table.push(this.tableData[i])
      }
      const data = {}
      data['data'] = table
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
      }).catch(res => {
        console.log(res)
        that.table_loading = false
      })
    },
    AddModel: function() {
      var that = this
      if (that.area === '') {
        that.$message.error('数据级别不能为空')
      } else if (that.kind === '') {
        that.$message.error('数据表类型不能为空')
      } else {
        if (that.area === '1' && that.kind === '1') {
          this.DataInput(addcityeconomydata)
        } 
        else if (that.area === '1' && that.kind === '2') {
          this.DataInput(addcitypopulationdata)
        } 
        else if (that.area === '1' && that.kind === '3') {
          this.DataInput(addgarbagecity)
        } 
        else if (that.area === '1' && that.kind === '4') {
          this.DataInput(addcitygarbagedeal)
        } 
        else if (that.area === '1' && that.kind === '5') {
          this.DataInput(addcitygarbagecapacity)
        } 
        else if (that.area === '1' && that.kind === '6') {
          this.DataInput(addcitygarbagevolume)
        }
        else if (that.area === '1' && that.kind === '7') {
          this. DataInput(addfacorylist)
        }
        else if (that.area === '1' && that.kind === '8') {
          this.DataInput(addtransferfactory)
        }
        else if (that.area === '1' && that.kind === '9') {
          this.DataInput(addcollectfactory)
        }
        else if (that.area === '1' && that.kind === '10'){
          this.DataInput(addelementgarbage)
        }
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
