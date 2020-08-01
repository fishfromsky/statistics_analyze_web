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
      </div>
      <div v-if="excel_download == true" style="text-align:center;margin-top:20px;margin-bottom:20px;">
        <a style="text-decoration:underline;font-style:italic;color:blue" :href="excel_url">点击下载表格</a>
      </div>
    </div>
  </div>
</template>

<script>
import {getnationpm, getnationwaterpollution, getnationsolidpollution, getworldpm } from '@/api/model'
export default {
  components: {
  },
  data() {
    return {
      level: '',
      kind: '',
      year: '',
      input_key_word: '',
      count: '',
      excel_url: '',
      startYear: '',
      endYear: '',
      district: '',
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
          label: '国内固体废弃物数据'
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

