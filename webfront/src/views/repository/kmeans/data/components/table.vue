<template>
  <div>
      <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 95%; margin: 0 auto">
        <el-table-column label="项目编号" align="center">
          <template slot-scope="{row}">
            <span>{{row.project_id}}</span>
          </template>
        </el-table-column>
        <el-table-column label="地区" align="center">
          <template slot-scope="{row}">
            <span>{{row.district}}</span>
          </template>
        </el-table-column>
        <el-table-column label="地区英文" align="center">
          <template slot-scope="{row}">
            <span>{{row.en_name}}</span>
          </template>
        </el-table-column>
        <el-table-column label="级别" align="center">
          <template slot-scope="{row}">
            <span>{{row.range}}</span>
          </template>
        </el-table-column>
        <el-table-column label="年份" align="center">
          <template slot-scope="{row}">
            <span>{{row.year}}</span>
          </template>
        </el-table-column>
        <el-table-column label="MSW" align="center">
          <template slot-scope="{row}">
            <span>{{row.msw}}</span>
          </template>
        </el-table-column>
        <el-table-column label="POP" align="center">
          <template slot-scope="{row}">
            <span>{{row.pop}}</span>
          </template>
        </el-table-column>
        <el-table-column label="PUP" align="center">
          <template slot-scope="{row}">
            <span>{{row.pup}}</span>
          </template>
        </el-table-column>
        <el-table-column label="HOU" align="center">
          <template slot-scope="{row}">
            <span>{{row.hou}}</span>
          </template>
        </el-table-column>
        <el-table-column label="APH" align="center">
          <template slot-scope="{row}">
            <span>{{row.aph}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GEN" align="center">
          <template slot-scope="{row}">
            <span>{{row.gen}}</span>
          </template>
        </el-table-column>
        <el-table-column label="AGE1" align="center">
          <template slot-scope="{row}">
            <span>{{row.age1}}</span>
          </template>
        </el-table-column>
        <el-table-column label="AGE2" align="center">
          <template slot-scope="{row}">
            <span>{{row.age2}}</span>
          </template>
        </el-table-column>
        <el-table-column label="AGE3" align="center">
          <template slot-scope="{row}">
            <span>{{row.age3}}</span>
          </template>
        </el-table-column>
        <el-table-column label="INC" align="center">
          <template slot-scope="{row}">
            <span>{{row.inc}}</span>
          </template>
        </el-table-column>
        <el-table-column label="EXP" align="center">
          <template slot-scope="{row}">
            <span>{{row.exp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="BUD" align="center">
          <template slot-scope="{row}">
            <span>{{row.bud}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GDP" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GDP1" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp1}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GDP2" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp2}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GDP3" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp3}}</span>
          </template>
        </el-table-column>
        <el-table-column label="pGDP" align="center">
          <template slot-scope="{row}">
            <span>{{row.pgdp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="EDU" align="center">
          <template slot-scope="{row}">
            <span>{{row.edu}}</span>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[10, 20, 30, 40, 50]"
        :page-size="page_size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total_size"
        style="margin-top: 20px; margin-left: 2.5%">
      </el-pagination>
  </div>
</template>

<script>
import { getparameterkmeans } from '@/api/model'
import resize from '@/views/element/components/mixins/resize'
export default {
  props: {
    parentmsg: {
      type: String,
      required: true
    }
  },
  data(){
    return{
      project_id: null,
      table_loading: false,
      tablekey: 0,
      tableData: [],
      page_data: [],
      total_size: 0,
      currentPage: 1,
      page_size: 10,
      filename: 'kmeans_data',
      autoWidth: true,
      bookType: 'xlsx',
    }
  },
  watch: {
    parentmsg: function(a, b){
      let that = this
      this.project_id = a
      let data = {}
      this.tableData = []
      this.page_data = []
      this.getData()
    }
  },
  methods: {
    formatJson(filterVal, jsonData) {
        return jsonData.map(v => filterVal.map(j => {
            if (j === 'timestamp') {
            return parseTime(v[j])
            } else {
            return v[j]
            }
        }))
    },
    download:function(){
      import('@/vendor/Export2Excel').then(excel => {
          const tHeader = ['project_id', 'district', 'en_name', 'range', 'year', 'msw', 'pop', 'pup', 'hou', 'aph', 'gen', 'age1', 'age2', 
          'age3', 'inc', 'exp', 'bud', 'gdp', 'gdp1', 'gdp2', 'gdp3', 'pgdp', 'edu']
          const filterVal = ['project_id', 'district', 'en_name', 'range', 'year', 'msw', 'pop', 'pup', 'hou', 'aph', 'gen', 'age1', 'age2', 
          'age3', 'inc', 'exp', 'bud', 'gdp', 'gdp1', 'gdp2', 'gdp3', 'pgdp', 'edu']
          const list = this.tableData
          const data = this.formatJson(filterVal, list)
          excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: this.filename,
          autoWidth: this.autoWidth,
          bookType: this.bookType
          })
      })
    },
    getData:function(){
      let data = {}
      let that = this
      data['project_id'] = this.project_id
      getparameterkmeans(data).then(res => {
        if (res.code === 20000){
          console.log(res)
          that.table_loading = false
          that.tableData = res.data
          let size = that.page_size
          let index = that.currentPage-1
          for (let i=index*size; i<(index+1)*size; i++){
              if (i==res.data.length){
                  break
              }
              that.page_data.push(res.data[i])
          }
          that.total_size = res.data.length
        }
      })
    },
    handleSizeChange(val){
      this.table_loading = true
      this.page_size = val
      this.currentPage = 1
      this.page_data = []
      this.getData()
    },
    handleCurrentChange(val){
      this.currentPage = val
      this.page_data = []
      this.getData()
    }
  }
}
</script>

<style>

</style>