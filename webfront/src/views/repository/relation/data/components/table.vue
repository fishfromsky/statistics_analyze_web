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
        <el-table-column label="垃圾清运量" align="center">
          <template slot-scope="{row}">
            <span>{{row.garbage_clear}}</span>
          </template>
        </el-table-column>
        <el-table-column label="常住人口" align="center">
          <template slot-scope="{row}">
            <span>{{row.population}}</span>
          </template>
        </el-table-column>
        <el-table-column label="城镇人口比重" align="center">
          <template slot-scope="{row}">
            <span>{{row.ratio_city_rural}}</span>
          </template>
        </el-table-column>
        <el-table-column label="户数" align="center">
          <template slot-scope="{row}">
            <span>{{row.household}}</span>
          </template>
        </el-table-column>
        <el-table-column label="每户平均人口" align="center">
          <template slot-scope="{row}">
            <span>{{row.people_per_capita}}</span>
          </template>
        </el-table-column>
        <el-table-column label="性别比例" align="center">
          <template slot-scope="{row}">
            <span>{{row.ratio_sex}}</span>
          </template>
        </el-table-column>
        <el-table-column label="年龄构成(0-14)" align="center">
          <template slot-scope="{row}">
            <span>{{row.age_0_14}}</span>
          </template>
        </el-table-column>
        <el-table-column label="年龄构成(15-64)" align="center">
          <template slot-scope="{row}">
            <span>{{row.age_15_64}}</span>
          </template>
        </el-table-column>
        <el-table-column label="年龄构成（65以上)" align="center">
          <template slot-scope="{row}">
            <span>{{row.age_65}}</span>
          </template>
        </el-table-column>
        <el-table-column label="城市居民人均可支配收入" align="center">
          <template slot-scope="{row}">
            <span>{{row.disposable_income}}</span>
          </template>
        </el-table-column>
        <el-table-column label="城市居民人均消费支出" align="center">
          <template slot-scope="{row}">
            <span>{{row.consume_cost}}</span>
          </template>
        </el-table-column>
        <el-table-column label="一般性公共财政支出" align="center">
          <template slot-scope="{row}">
            <span>{{row.public_cost}}</span>
          </template>
        </el-table-column>
        <el-table-column label="国内生产总值" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="第一产业生产总值" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp_first_industry}}</span>
          </template>
        </el-table-column>
        <el-table-column label="第二产业生产总值" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp_second_industry}}</span>
          </template>
        </el-table-column>
        <el-table-column label="第三产业生产总值" align="center">
          <template slot-scope="{row}">
            <span>{{row.gdp_third_industry}}</span>
          </template>
        </el-table-column>
        <el-table-column label="人均生产总值" align="center">
          <template slot-scope="{row}">
            <span>{{row.gnp}}</span>
          </template>
        </el-table-column>
        <el-table-column label="就业人员受教育程度" align="center">
          <template slot-scope="{row}">
            <span>{{row.education}}</span>
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
import { getparameterrelation } from '@/api/model'
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
      filename: 'relation_data',
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
          const tHeader = ['project_id', 'year', 'garbage_clear', 'population', 'ratio_city_rural', 'household', 'people_per_capita', 'ratio_sex', 'age_0_14', 'age_15_64', 'age_65', 'disposable_income', 'consume_cost',
          'public_cost', 'gdp', 'gdp_first_industry', 'gdp_second_industry', 'gdp_third_industry', 'gnp', 'education']
          const filterVal = ['project_id', 'year', 'garbage_clear', 'population', 'ratio_city_rural', 'household', 'people_per_capita', 'ratio_sex', 'age_0_14', 'age_15_64', 'age_65', 'disposable_income', 'consume_cost',
          'public_cost', 'gdp', 'gdp_first_industry', 'gdp_second_industry', 'gdp_third_industry', 'gnp', 'education']
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
      getparameterrelation(data).then(res => {
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