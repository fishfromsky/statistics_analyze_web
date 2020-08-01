<template>

  <div class="app-container">
    <div class="filter-container">

      <el-input v-model="listQuery.point_no" placeholder="回收点编号" style="width: 100px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.point_name" placeholder="回收点名称" style="width: 100px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.village_name" placeholder="所属小区" style="width: 100px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.service_person" placeholder="回收人员" style="width: 100px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.manager" placeholder="负责人" style="width: 100px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.street_town_name" placeholder="所属街镇" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in street_town_nameOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.point_style" placeholder="回收点类型" clearable style="width: 100px" class="filter-item">
        <el-option v-for="item in point_styleOptions" :key="item" :label="item" :value="item" />
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
      <el-button v-waves :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">
        下载
      </el-button>
      <el-button v-waves :loading="uploadloadLoading" class="filter-item" type="primary" icon="el-icon-upload2" @click="showHandleUpload">
        上传
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

      <el-button v-waves :loading="uploadloadLoading" class="filter-item" type="primary" icon="el-icon-delete-solid" @click="showHandleClear">
        清空
      </el-button>
      <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisibleclear">
        <p>确认清空数据吗？</p>
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

      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80" :class-name="getSortClass('id')">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="所属街镇" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.street_town_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="回收点编号" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.point_no }}</span>
        </template>
      </el-table-column>
      <el-table-column label="回收点名称" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.point_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="回收点图片" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.point_figure }}</span>
        </template>
      </el-table-column>
      <el-table-column label="所属小区" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.village_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="所属居委" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.housing_committee }}</span>
        </template>
      </el-table-column>
      <el-table-column label="回收点类型" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.point_style }}</span>
        </template>
      </el-table-column>
      <el-table-column label="可回收物品种" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.recycling_style }}</span>
        </template>
      </el-table-column>
      <el-table-column label="详细地址" width="100.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.detail_location }}</span>
        </template>
      </el-table-column>
      <el-table-column label="服务日期" width="50.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.service_day }}</span>
        </template>
      </el-table-column>
      <el-table-column label="服务时间" width="50.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.service_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="回收人员" width="50.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.service_person }}</span>
        </template>
      </el-table-column>
      <el-table-column label="产权单位" width="50.0px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.property_unit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="负责人" width="nanpx" align="center">
        <template slot-scope="{row}">
          <span>{{ row.manager }}</span>
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
        <el-form-item label="所属街镇">
          <el-input v-model="temp.street_town_name" type="忽略" placeholder="输入所属街镇" />
        </el-form-item>
        <el-form-item label="回收点编号">
          <el-input v-model="temp.point_no" type="忽略" placeholder="输入编号" />
        </el-form-item>
        <el-form-item label="回收点名称">
          <el-input v-model="temp.point_name" type="忽略" placeholder="输入名称" />
        </el-form-item>
        <el-form-item label="回收点图片">
          <el-input v-model="temp.point_figure" type="忽略" placeholder="输入图片" />
        </el-form-item>
        <el-form-item label="所属小区">
          <el-input v-model="temp.village_name" type="忽略" placeholder="输入小区" />
        </el-form-item>
        <el-form-item label="所属居委">
          <el-input v-model="temp.housing_committee" type="忽略" placeholder="输入居委" />
        </el-form-item>
        <el-form-item label="回收点类型">
          <el-input v-model="temp.point_style" type="忽略" placeholder="输入类型" />
        </el-form-item>
        <el-form-item label="可回收物品种">
          <el-input v-model="temp.recycling_style" type="忽略" placeholder="输入可回收物品种" />
        </el-form-item>
        <el-form-item label="详细地址">
          <el-input v-model="temp.detail_location" type="忽略" placeholder="输入详细地址" />
        </el-form-item>
        <el-form-item label="回收点经度">
          <el-input v-model="temp.longitude" type="number" placeholder="输入数字" />
        </el-form-item>
        <el-form-item label="回收点纬度">
          <el-input v-model="temp.latitude" type="number" placeholder="输入数字" />
        </el-form-item>
        <el-form-item label="设计日回收量（吨）">
          <el-input v-model="temp.design_load" type="number" placeholder="输入数字（吨）" />
        </el-form-item>
        <el-form-item label="服务户数">
          <el-input v-model="temp.household_served" type="number" placeholder="输入户数" />
        </el-form-item>
        <el-form-item label="服务日期">
          <el-input v-model="temp.service_day" type="忽略" placeholder="输入服务日期" />
        </el-form-item>
        <el-form-item label="服务时间">
          <el-input v-model="temp.service_time" type="忽略" placeholder="输入服务时间" />
        </el-form-item>
        <el-form-item label="回收人员">
          <el-input v-model="temp.service_person" type="忽略" placeholder="输入回收人员" />
        </el-form-item>
        <el-form-item label="回收人电话">
          <el-input v-model="temp.service_person_phone" type="忽略" placeholder="输入电话" />
        </el-form-item>
        <el-form-item label="产权单位">
          <el-input v-model="temp.property_unit" type="忽略" placeholder="输入产权单位" />
        </el-form-item>
        <el-form-item label="运营单位">
          <el-input v-model="temp.operation_unit" type="忽略" placeholder="输入运营单位" />
        </el-form-item>
        <el-form-item label="负责人">
          <el-input v-model="temp.manager" type="忽略" placeholder="输入负责人" />
        </el-form-item>
        <el-form-item label="负责人电话">
          <el-input v-model="temp.manager_phone" type="忽略" placeholder="输入负责人电话" />
        </el-form-item>
        <el-form-item label="开始运营时间">
          <el-input v-model="temp.starting_running_time" type="忽略" placeholder="输入开始运营时间" />
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
import { fetchList, fetchPv, createtianrecy1, updatetianrecy1, deletetianrecy1, downloadtianrecy1, uploadtianrecy1, cleartianrecy1 } from '@/api/app01/tianrecy1'
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
      listQuery: {
        page: 1,
        limit: 20,
        street_town_name: undefined,
        point_no: undefined,
        point_name: undefined,
        village_name: undefined,
        point_style: undefined,
        service_person: undefined,
        manager: undefined,

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
      },
      downloadLoading: false
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

        this.street_town_nameOptions = response.data.unique_street_town_name
        this.point_styleOptions = response.data.unique_point_style

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
          createtianrecy1(this.temp).then(() => {
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
          updatetianrecy1(tempData).then(() => {
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
      deletetianrecy1(row.id).then(() => {
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
      downloadtianrecy1(this.listQuery).then(response => {
        // response = response.json();
        this.list = response.data.items
        // console.log('data.................', data)
        const tHeader = ['id', '所属街镇', '回收点编号', '回收点名称', '回收点图片', '所属小区', '所属居委', '回收点类型', '可回收物品种', '详细地址', '回收点经度', '回收点纬度', '设计日回收量（吨）', '服务户数', '服务日期', '服务时间', '回收人员', '回收人电话', '产权单位', '运营单位', '负责人', '负责人电话', '开始运营时间']
        const filterVal = ['id', 'street_town_name', 'point_no', 'point_name', 'point_figure', 'village_name', 'housing_committee', 'point_style', 'recycling_style', 'detail_location', 'longitude', 'latitude', 'design_load', 'household_served', 'service_day', 'service_time', 'service_person', 'service_person_phone', 'property_unit', 'operation_unit', 'manager', 'manager_phone', 'starting_running_time']
        const data = this.formatJson(filterVal)

        import('@/vendor/Export2Excel').then(excel => {
          excel.export_json_to_excel({
            header: tHeader,
            data,
            filename: '两网融合详细信息'
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
      location.reload() // 刷新页面
    },
    hideHandleClear() {
      this.dialogFormVisibleclear = false
    },

    handleClear() {
      this.dialogFormVisibleclear = false
      const data = { 'project_id': 1 }
      cleartianrecy1(data).then(() => {
        this.$notify({
          title: 'Success',
          message: '清空成功',
          type: 'success',
          duration: 2000
        })
      })
      location.reload() // 刷新页面
    },

    handleUpload() {
      this.dialogFormVisibleupload = false
      console.log('handleUpload..................')
      console.log('this.tableData', this.tableData)
      uploadtianrecy1(this.tableData).then(() => {
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
