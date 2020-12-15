<template>
  <div>
      <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 95%; margin: 0 auto">
        <el-table-column label="项目编号" align="center">
          <template slot-scope="{row}">
            <span>{{row.project_id}}</span>
          </template>
        </el-table-column>
        <el-table-column label="年份" align="center">
          <template slot-scope="{row}">
            <span>{{row.year}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人口总量" align="center">
          <template slot-scope="{row}">
            <span>{{row.population}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人口密度" align="center">
          <template slot-scope="{row}">
            <span>{{row.population_density}}</span>
          </template>
        </el-table-column>
        <el-table-column label="自然增长率" align="center">
          <template slot-scope="{row}">
            <span>{{row.natural_growth_rate}}</span>
          </template>
        </el-table-column>
        <el-table-column label="总户数" align="center">
          <template slot-scope="{row}">
            <span>{{row.total_households}}</span>
          </template>
        </el-table-column>
        <el-table-column label="平均每户人数" align="center">
          <template slot-scope="{row}">
            <span>{{row.average_person_per_household}}</span>
          </template>
        </el-table-column>
        <el-table-column label="失业率" align="center">
          <template slot-scope="{row}">
            <span>{{row.unemployment_rate}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GDP总量" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人均GDP" align="center">
          <template slot-scope="{row}">
            <span>{{row.per_capita_gdp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="GDP增长率" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp_growth_rate}}</span>
          </template>
        </el-table-column>
        <el-table-column label="固废产量" align="center">
          <template slot-scope="{row}">
            <span>{{row.residential_garbage}}</span>
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
import { getlstmparameter } from '@/api/model'
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
      filename: 'lstm_input_data',
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
    download:function(){
      import('@/vendor/Export2Excel').then(excel => {
          const tHeader = ['project_id', 'year', 'population', 'population_density', 'natural_growth_rate', 'total_household', 'average_person_per_household',
          'unemployment_rate', 'gdp', 'per_capita_gdp', 'gdp_growth_rate', 'residential_garbage']
          const filterVal = ['project_id', 'year', 'population', 'population_density', 'natural_growth_rate', 'total_household', 'average_person_per_household',
          'unemployment_rate', 'gdp', 'per_capita_gdp', 'gdp_growth_rate', 'residential_garbage']
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
  formatJson(filterVal, jsonData) {
        return jsonData.map(v => filterVal.map(j => {
            if (j === 'timestamp') {
            return parseTime(v[j])
            } else {
            return v[j]
            }
        }))
    },
    getData:function(){
      let data = {}
      let that = this
      data['project_id'] = this.project_id
      getlstmparameter(data).then(res => {
        if (res.code === 20000){
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