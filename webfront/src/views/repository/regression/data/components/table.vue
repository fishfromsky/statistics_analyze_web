<template>
  <div>
      <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 95%; margin: 0 auto">
        <el-table-column label="项目编号" align="center">
          <template slot-scope="{row}">
            <span>{{row.project_id}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人口(10,000)" align="center">
          <template slot-scope="{row}">
            <span>{{row.resident_population}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人口密度(p/sq km)" align="center">
          <template slot-scope="{row}">
            <span>{{row.population_of_density}}</span>
          </template>
        </el-table-column>
        <el-table-column label="住户数(10,000)" align="center">
          <template slot-scope="{row}">
            <span>{{row.number_of_households}}</span>
          </template>
        </el-table-column>
        <el-table-column label="平均每户人口(p)" align="center">
          <template slot-scope="{row}">
            <span>{{row.average_population_per_household}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人均可支配收入(元)" align="center">
          <template slot-scope="{row}">
            <span>{{row.urban_residents_per_capita_disposable_income}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人均消费支出(元)" align="center">
          <template slot-scope="{row}">
            <span>{{row.consumer_expenditure}}</span>
          </template>
        </el-table-column>
        <el-table-column label="公共支出(十亿)" align="center">
          <template slot-scope="{row}">
            <span>{{row.general_public_expenditure}}</span>
          </template>
        </el-table-column>
        <el-table-column label="基础设施投资(十亿)" align="center">
          <template slot-scope="{row}">
            <span>{{row.investment_in_urban_infrastructure}}</span>
          </template>
        </el-table-column>
        <el-table-column label="城市人口密度(p/sq km)" align="center">
          <template slot-scope="{row}">
            <span>{{row.urban_population_density}}</span>
          </template>
        </el-table-column>
        <el-table-column label="绿植覆盖率(%)" align="center">
          <template slot-scope="{row}">
            <span>{{row.greening_coverage}}</span>
          </template>
        </el-table-column>
        <el-table-column label="本地生产总值(十亿)" align="center">
          <template slot-scope="{row}">
            <span>{{row.gross_local_product}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人均GDP(元)" align="center">
          <template slot-scope="{row}">
            <span>{{row.gross_domestic_product_per_capita}}</span>
          </template>
        </el-table-column>
        <el-table-column label="第一产业产值(十亿)" align="center">
          <template slot-scope="{row}">
            <span>{{row.gross_domestic_product_of_the_first_industry}}</span>
          </template>
        </el-table-column>
        <el-table-column label="第二产业产值(十亿)" align="center">
          <template slot-scope="{row}">
            <span>{{row.gross_value_of_secondary_industry}}</span>
          </template>
        </el-table-column>
        <el-table-column label="第三产业产值(十亿)" align="center">
          <template slot-scope="{row}">
            <span>{{row.investment_in_environmental_protection}}</span>
          </template>
        </el-table-column>
        <el-table-column label="环保投资(百万)" align="center">
          <template slot-scope="{row}">
            <span>{{row.investment_in_environmental_protection}}</span>
          </template>
        </el-table-column>
        <el-table-column label="大学生数(10,000)" align="center">
          <template slot-scope="{row}">
            <span>{{row.number_of_college_students}}</span>
          </template>
        </el-table-column>
        <el-table-column label="员工受教育程度(%)" align="center">
          <template slot-scope="{row}">
            <span>{{row.level_of_education}}</span>
          </template>
        </el-table-column>
        <el-table-column label="垃圾产量(10,000吨)" align="center">
          <template slot-scope="{row}">
            <span>{{row.municial_household_garbage}}</span>
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
import { getregressionpara } from '@/api/model'
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
      filename: 'regression_data',
      autoWidth: true,
      bookType: 'xlsx',
    }
  },
  watch: {
    parentmsg: function(a, b){
      let that = this
      this.project_id = a
      this.page_data = []
      this.tableData = []
      let data = {}
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
          const tHeader = ['project_id', 'resident_population', 'population_of_density', 'number_of_households', 'average_population_per_household', 'urban_residents_per_capita_disposable_income',
          'consumer_expenditure', 'general_public_expenditure', 'investment_in_urban_infrastructure', 'urban_population_density', 'greening_coverage', 'gross_local_product', 'gross_domestic_product_per_capita',
          'gross_domestic_product_of_the_first_industry', 'gross_value_of_secondary_industry', 'gross_value_of_the_tertiary_industry', 'investment_in_environmental_protection', 'number_of_college_students',
          'level_of_education', 'municial_household_garbage']
          const filterVal = ['project_id', 'resident_population', 'population_of_density', 'number_of_households', 'average_population_per_household', 'urban_residents_per_capita_disposable_income',
          'consumer_expenditure', 'general_public_expenditure', 'investment_in_urban_infrastructure', 'urban_population_density', 'greening_coverage', 'gross_local_product', 'gross_domestic_product_per_capita',
          'gross_domestic_product_of_the_first_industry', 'gross_value_of_secondary_industry', 'gross_value_of_the_tertiary_industry', 'investment_in_environmental_protection', 'number_of_college_students',
          'level_of_education', 'municial_household_garbage']
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
      this.table_loading = true
      let data = {}
      let that = this
      data['project_id'] = this.project_id
      getregressionpara(data).then(res => {
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