<template>

  <div class="app-container">
    <div class="filter-container">

      <el-input v-model="listQuery.title" placeholder="标题" style="width: 100px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.importance" placeholder="重要性" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in importanceOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.type" placeholder="类型" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in typeOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.sort" style="width: 140px" class="filter-item" @change="handleFilter">
        <el-option v-for="item in sortOptions" :key="item.key" :label="item.label" :value="item.key" />
      </el-select>

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        查询
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        新增
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        下载
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-upload2" @click="showHandleUpload">
        上传
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-delete-solid" @click="showHandleClear">
        清空
      </el-button>

      <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisibleupload">
        <upload-excel-component :on-success="handleSuccess" :before-upload="beforeUpload" />
        <el-table :data="tableData" border highlight-current-row style="width: 100%;margin-top:20px;">
          <el-table-column v-for="item of tableHeader" :key="item" :prop="item" :label="item" />
        </el-table>
        <div slot="title" class="dialog-footer">
          <el-button @click="hideHandleUpload">
            取消
          </el-button>
          <el-button type="primary" @click="handleUpload">
            确认
          </el-button>
        </div>
      </el-dialog>

      <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisibleclear">
        <p>确认清空筛选的数据吗？</p>
        <div slot="footer" class="dialog-footer">
          <el-button @click="hideHandleClear">
            不清空
          </el-button>
          <el-button type="primary" @click="handleClear">
            确认清空
          </el-button>
        </div>
      </el-dialog>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
    >

      <el-table-column label="时间戳" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.timestamp }}</span>
        </template>
      </el-table-column>
      <el-table-column label="作者" width="200.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.author }}</span>
        </template>
      </el-table-column>
      <el-table-column label="审核" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.reviewer }}</span>
        </template>
      </el-table-column>
      <el-table-column label="标题" width="200.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.title }}</span>
        </template>
      </el-table-column>
      <el-table-column label="概要" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.content_short }}</span>
        </template>
      </el-table-column>
      <el-table-column label="内容" width="200.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.content }}</span>
        </template>
      </el-table-column>
      <el-table-column label="预测" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.forecast }}</span>
        </template>
      </el-table-column>
      <el-table-column label="重要性" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.importance }}</span>
        </template>
      </el-table-column>
      <el-table-column label="类型" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="平台" width="nanpx" align="center">
        <template slot-scope="{row}">
          <span>{{ row.platforms }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" width="250" class-name="small-padding fixed-width">
        <template slot-scope="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            编辑
          </el-button>
          <el-button type="success" size="mini" @click="handleUpdate(row)">
            查询
          </el-button>
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="handleDelete(row,$index)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="150px" style="width: 500px; margin-left:100px;">
        <el-form-item label="时间戳">
          <el-date-picker v-model="temp.timestamp" type="datetime" placeholder="选择时间" />
        </el-form-item>
        <el-form-item label="审核">
          <el-input v-model="temp.reviewer" type="忽略" placeholder="输入审核者" />
        </el-form-item>
        <el-form-item label="标题">
          <el-input v-model="temp.title" type="忽略" placeholder="输入标题" />
        </el-form-item>
        <el-form-item label="内容">
          <el-input v-model="temp.content" type="textarea" placeholder="输入内容" />
        </el-form-item>
        <el-form-item label="预测">
          <el-input v-model="temp.forecast" type="number" placeholder="输入数字" />
        </el-form-item>

      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          确认
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel" />
        <el-table-column prop="pv" label="Pv" />
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">确认</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import UploadExcelComponent from '@/components/UploadExcel/index.vue'
import { fetchList, fetchPv, createarticle1, updatearticle1, deletearticle1, downloadarticle1, uploadarticle1, cleararticle1 } from '@/api/app01/article1'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import XLSX from 'xlsx'

export default {
  name: 'ComplexTable',
  components: { Pagination, UploadExcelComponent },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      tableData: [],
      tableHeader: [],
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      importanceOptions: [],
      typeOptions: [],

      listQuery: {
        page: 1,
        limit: 20,
        title: undefined,
        importance: undefined,
        type: undefined,

        sort: '-id'
      },

      sortOptions: [{ label: '升序', key: '+id' }, { label: '降序', key: '-id' }],
      temp: {
        id: undefined
      },
      dialogFormVisible: false,
      dialogFormVisibleupload: false,
      dialogFormVisibleclear: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        // type: [{ required: true, message: 'type is required', trigger: 'change' }],
        // timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        // title: [{ required: true, message: 'title is required', trigger: 'blur' }]
      }
      // downloadLoading: false
    }
  },
  created() {
    this.getList()
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
    },

    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total

        this.importanceOptions = response.data.unique_importance
        this.typeOptions = response.data.unique_type

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    resetTemp() {
      this.temp = {
        id: undefined
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          // this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          // this.temp.author = 'vue-element-admin'
          createarticle1(this.temp).then(() => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },

    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },

    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          updatearticle1(tempData).then(() => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },

    handleDelete(row, index) {
      this.list.splice(index, 1)
      console.log(row.id)
      deletearticle1(row.id).then(() => {
        this.$notify({
          title: 'Success',
          message: 'Update Successfully',
          type: 'success',
          duration: 2000
        })
      })
    },

    handleFetchPv(pv) {
      fetchPv(pv).then(response => {
        this.pvData = response.data.pvData
        this.dialogPvVisible = true
      })
    },

    handleDownload() {
      this.listLoading = true
      downloadarticle1(this.listQuery).then(response => {
        // response = response.json();
        this.list = response.data.items
        // console.log('data.................', data)
        const tHeader = ['时间戳', '作者', '审核', '标题', '概要', '内容', '预测', '重要性', '类型', '状态', '展示时间', '可评论', '页码', '图片链接', '平台']
        const filterVal = ['timestamp', 'author', 'reviewer', 'title', 'content_short', 'content', 'forecast', 'importance', 'type', 'status', 'display_time', 'comment_disabled', 'pageviews', 'image_uri', 'platforms']
        const data = this.formatJson(filterVal)

        import('@/vendor/Export2Excel').then(excel => {
          excel.export_json_to_excel({
            header: tHeader,
            data,
            filename: '我的文章'
          })
        })
        console.log('test13.................')
      })
      this.listLoading = false
    },

    showHandleUpload() {
      this.dialogFormVisibleupload = true
    },
    showHandleClear() {
      this.dialogFormVisibleclear = true
    },

    hideHandleUpload() {
      this.dialogFormVisibleupload = false
    },

    hideHandleClear() {
      this.dialogFormVisibleclear = false
    },

    handleClear() {
      this.listLoading = true
      this.dialogFormVisibleclear = false
      cleararticle1(this.listQuery).then(() => {
        this.$notify({
          title: 'Success',
          message: '清空成功',
          type: 'success',
          duration: 2000
        })
      })
      this.listLoading = false
      location.reload() // 刷新页面
    },

    handleUpload() {
      this.dialogFormVisibleupload = false
      console.log('handleUpload..................')
      console.log('this.tableData', this.tableData)
      uploadarticle1(this.tableData).then(() => {
        this.$notify({
          title: 'Success',
          message: '上传成功',
          type: 'success',
          duration: 2000
        })
      })
      location.reload() // 刷新页面
    },

    handleClick(e) {
      console.log('handleClick................................................')
      const files = e.target.files
      const rawFile = files[0] // only use files[0]
      if (!rawFile) return
      this.upload(rawFile)
    },

    upload(rawFile) {
      this.$refs['excel-upload-input'].value = null // fix can't select the same excel
      console.log('upload................................................')
      if (!this.beforeUpload) {
        this.readerData(rawFile)
        return
      }
      const before = this.beforeUpload(rawFile)
      if (before) {
        this.readerData(rawFile)
      }
    },

    readerData(rawFile) {
      this.loading = true
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.onload = e => {
          const data = e.target.result
          const workbook = XLSX.read(data, { type: 'array' })
          const firstSheetName = workbook.SheetNames[0]
          const worksheet = workbook.Sheets[firstSheetName]
          const header = this.getHeaderRow(worksheet)
          const results = XLSX.utils.sheet_to_json(worksheet)
          this.generateData({ header, results })
          this.loading = false
          resolve()
        }
        reader.readAsArrayBuffer(rawFile)
      })
    },

    getHeaderRow(sheet) {
      const headers = []
      const range = XLSX.utils.decode_range(sheet['!ref'])
      let C
      const R = range.s.r
      /* start in the first row */
      for (C = range.s.c; C <= range.e.c; ++C) { /* walk every column in the range */
        const cell = sheet[XLSX.utils.encode_cell({ c: C, r: R })]
        /* find the cell in the first row */
        let hdr = 'UNKNOWN ' + C // <-- replace with your desired default
        if (cell && cell.t) hdr = XLSX.utils.format_cell(cell)
        headers.push(hdr)
      }
      return headers
    },
    isExcel(file) {
      return /\.(xlsx|xls|csv)$/.test(file.name)
    },

    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    },
    getSortClass: function(key) {
      const sort = this.listQuery.sort
      return sort === `+${key}` ? 'ascending' : 'descending'
    }
  }
}
</script>
