<template>
  <div class="app-container">
    <div class="main-content">
      <div class="input-content">
        <el-select v-model="level" placeholder="请选择爬取的数据" class="input-item">
          <el-option v-for="item in level_option"  :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <el-select v-if="level == '3'" v-model="kind" placeholder="请选择爬取数据的关键字" class="input-item">
          <el-option v-for="item in kind_option" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <el-input v-model="input_key_word" v-if="kind == '其他' && level == '3'" placeholder="请输入爬取数据的关键字" style="width:200px;margin-left:20px"></el-input>
        <el-input v-model="count" v-if="level == '3'" placeholder="请输入爬取数据的数量" style="width:200px;margin-left:20px"></el-input>
         <el-input v-model="district" v-if="level == '3'" placeholder="请输入地址关键字" style="width:200px;margin-left:20px"></el-input>
        <el-date-picker v-model="startYear" v-if="level == '3'" type="year" placeholder="开始年份" format="yyyy" style="margin-left:20px">
        </el-date-picker>
        <el-date-picker v-model="endYear"  v-if="level == '3'" type="year" placeholder="结束年份" format="yyyy" style="margin-left:20px">
        </el-date-picker>
        <div class="divider"></div>
        <el-button type="primary" icon="el-icon-download" class="input-item" @click="getData" :loading="data_loading">爬取数据</el-button>
        <el-button type="primary" icon="el-icon-stopwatch" class="input-item" @click="getHistory">查看历史</el-button>
      </div>
      <div v-if="excel_download == true" style="text-align:center;margin-top:20px;margin-bottom:20px;">
        <a style="text-decoration:underline;font-style:italic;color:blue" :href="excel_url">点击下载表格</a>
      </div>
    </div>
    <div class="main-content" v-if="showHistory">
    <div class="filter-container">
      <el-select v-model="listQuery.year" placeholder="年份" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in year_option" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-if="level=='3'" v-model="listQuery.key_words" placeholder="关键字" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in kw_option" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-if="level=='3'" v-model="listQuery.city" placeholder="城市" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in city_option" :key="item" :label="item" :value="item" />
      </el-select>

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter" style="margin-left:20px">
        查询
      </el-button>
    </div>
    <el-table v-loading="table_loading" :key="tablekey" :data="page_data" border fit highlight-current-row style="width: 100%; margin-top: 20px">
           <el-table-column label="日期" align="center">
               <template slot-scope="{row}">
                   <span>{{row.date}}</span>
               </template>
           </el-table-column>
           <el-table-column label="时间" align="center">
               <template slot-scope="{row}">
                   <span>{{row.time}}</span>
               </template>
           </el-table-column>
           <el-table-column label="表格种类" align="center">
               <template slot-scope="{row}">
                   <span>{{row.table_type}}</span>
               </template>
           </el-table-column>
           <el-table-column label="关键字信息" align="center">
               <template slot-scope="{row}">
                   <span>{{row.key_words}}</span>
               </template>
           </el-table-column>
           <el-table-column label="城市" align="center">
               <template slot-scope="{row}">
                   <span>{{row.city}}</span>
               </template>
           </el-table-column>
           <el-table-column label="数据操作" align="center">
               <template slot-scope="{row}">
                   <a style="color:#1890FF;font-size:12px" :href=row.file_location>下载</a>
                   <el-button size="mini" type="text" @click="deleteData(row.id)" style="margin-left: 30px">删除</el-button>
               </template>
           </el-table-column>
       </el-table>
        <el-dialog :visible.sync="delete_dialog" title="删除数据" width="30%">
           <span>确定删除改数据吗？删除后不可恢复</span>
           <div slot="footer" class="dialog-footer">
                <el-button @click="delete_dialog = false">取 消</el-button>
                <el-button type="danger" @click="deleteDataConfirm">确 定</el-button>
            </div>
       </el-dialog>
       <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[10, 20, 30, 40, 50]"
            :page-size="page_size"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total_size"
            style="margin-top: 20px">
        </el-pagination>
       </div>
  </div>
</template>

<script>
import {getnationpm, getnationwaterpollution, getnationsolidpollution, getworldpm, getCrawlDataRecord, deleteCrawlData, selectCrawlRecord } from '@/api/model'
export default {
  components: {
  },
  data() {
    return {
      level: '',
      kind: '',
      year: '',
      showHistory: false,
      input_key_word: '',
      count: '',
      table_loading: false,
      tablekey: 0,
      tableData: [],
      page_data: [],
      formData: [],
      delete_dialog: false,
      delete_id: '',
      total_size: 0,
      currentPage: 1,
      page_size: 10,
      excel_url: '',
      startYear: '',
      endYear: '',
      district: '',
      table_type: '',
      excel_download: false,
      data_loading: false,
      form: {
        table_kind: '',
        key_word: '',
        startYear: '',
        endYear: '',
        count: '',
        district: ''
       },
       listQuery: {
        table_type: '',
        year: '',
        key_words: '',
        city: ''
       },
      year_option: [],
      kw_option: [],
      city_option: [],
      level_option: [
        {
          value: '1',
          label: '国内空气污染数据'
        },
        {
          value: '2',
          label: '国内水体污染数据'
        },
        {
          value: '3',
          label: '国内固体废物数据'
        }
      ],
      kind_option: [
        {
          value: '垃圾',
          label: '垃圾'
        },
        {
          value: '废弃物',
          label: '废弃物'
        },
        {
          value: '回收',
          label: '回收'
        },
        {
          value: '塑料',
          label: '塑料'
        },
        {
          value: '金属',
          label: '金属'
        },
        {
          value: '纸业',
          label: '纸业'
        },
        {
          value: '其他',
          label: '其他',
        }
      ]
    }
  },
  watch: {

  },
  methods: {
    getData() {
      var that = this
      if (that.level === '') {
        that.$message.error('数据种类不能为空')
      } else if (that.level === '1') {
        this.form.table_kind = that.level
        let data = this.form
        this.data_loading = true
        this.excel_download = false
        getnationpm(data).then(res=>{
          if(res.code === 20000) {
            this.$message({
              type: 'success',
              message: 'success'
            })
            this.data_loading = false
            this.excel_download = true
            this.excel_url = res.excel_url
          }
          this.data_loading = false
        })
      } else if (that.level === '2') {
        this.form.table_kind = that.level
        let data = this.form
        this.data_loading = true
        this.excel_download = false
        getnationwaterpollution(data).then(res=>{
          if(res.code === 20000) {
            this.$message({
              type: 'success',
              message: 'success'
            })
            this.data_loading = false
            this.excel_download = true
            this.excel_url = res.excel_url
          }
          this.data_loading = false
        })
      } else if (that.level === '3') {
        if (that.kind === '' || that.count === '' || that.startYear === '' || that.endYear === '') {
          that.$message.error('请填写完整数据！')
        } else {
            if (that.kind === '其他') {
              this.form.key_word = that.input_key_word
            } else {
              this.form.key_word = that.kind
            }
            if ( that.startYear > that.endYear ) {
              that.$message.error('请填写正确的时间区间！')
            } else {
                    this.form.table_kind = that.level
                    this.form.startYear = that.startYear
                    this.form.endYear = that.endYear
                    this.form.count = that.count
                    this.form.district = that.district
                    let data = this.form
                    this.data_loading = true
                    this.excel_download = false
                    getnationsolidpollution(data).then(res=>{
                    if(res.code === 20000) {
                      this.$message({
                        type: 'success',
                        message: 'success'
                    })
                    this.data_loading = false
                    this.excel_download = true
                    this.excel_url = res.excel_url
                    }
                    this.data_loading = false
                    })
                  }
        }
      }
    },
    getHistory() {
      let that = this
      if (that.level === '') {
        that.$message.error('数据种类不能为空')
      } else {
        if (that.level === '1'){
          that.table_type = '国内空气污染数据'
        } else if (that.level === '2'){
          that.table_type = '国内水体污染数据'
        } else if (that.level === '3') {
          that.table_type = '国内固体废物数据'
        }
        this.showHistory = true
        getCrawlDataRecord(that.table_type).then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    let size = that.page_size
                    let index = that.currentPage-1
                    that.page_data = []
                    for (let i=index*size; i<(index+1)*size; i++){
                        if (i==res.data.length){
                            break
                        }
                        that.page_data.push(res.data[i])
                    }
                    that.total_size = res.data.length
                    that.year_option = res.unique_year_list
                    that.kw_option = res.unique_kw_list
                    that.city_option = res.unique_city_list
                }
            })
      }
    },
    handleFilter() {
      let that = this
      that.listQuery.table_type = that.table_type
      selectCrawlRecord(that.listQuery).then(res=>{
                if (res.code === 20000){
                    that.table_loading = false
                    that.tableData = res.data
                    let size = that.page_size
                    let index = that.currentPage-1
                    that.page_data = []
                    this.$message({
              type: 'success',
              message: res.data
            })
                    for (let i=index*size; i<(index+1)*size; i++){
                        if (i==res.data.length){
                            break
                        }
                        that.page_data.push(res.data[i])
                    }
                    that.total_size = res.data.length
                    that.year_option = res.unique_year_list
                    that.kw_option = res.unique_kw_list
                    that.city_option = res.unique_city_list
                }
            })
    },
    deleteData(id) {
      this.delete_dialog = true
      this.delete_id = id
    },
    deleteDataConfirm() {
      deleteCrawlData(this.delete_id).then(res=>{
        if(res.code === 20000){
          this.$message({
            type: 'success',
            message: '删除成功'
          })
          this.delete_dialog = false
          this.getHistory()
        }
      }
      )
    },
    handleSizeChange(val){
            this.table_loading = true
            this.page_size = val
            this.currentPage = 1
            this.page_data = []
            this.getHistory()
    },
    handleCurrentChange(val){
            this.currentPage = val
            this.page_data = []
            this.getHistory()
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
    margin-top:20px;
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

