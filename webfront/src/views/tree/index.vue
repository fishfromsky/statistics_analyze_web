<template>
  <div class="app-container">
    <div class="main-content">
      <div class="input-content">
        <el-input v-model="searchContent" placeholder="请输入搜索关键字" class="search-item"></el-input>
        <el-select v-model="importance" placeholder="模型星数" clearable class="option-item">
          <el-option v-for="item in importantOptions" :key="item" :value="item" :label="item"></el-option>
        </el-select>
        <el-button type="primary" icon="el-icon-search" @click="SearchClick" class="search-btn">搜索模型</el-button>
        <router-link to="/example/table">
          <el-button type="primary" icon="el-icon-edit" class="search-btn" @click="EditClick">增加模型</el-button>
        </router-link>
        <el-button type="primary" icon="el-icon-download" class="search-btn" @click="LoadClick">导出表格</el-button>
      </div>

      <el-table :key="tableKey" :data="listQuery" border v-loading="loading"
                fit highlight-current-row style="width: 100%;" :default-sort = "{prop: 'star', order: null}">
        <el-table-column label="模型编号" align="center" width="90">
          <template slot-scope="{row}">
            <span>{{row.id}}</span>
          </template>
        </el-table-column>
        <el-table-column label="上传日期" width="180" align="center">
          <template slot-scope="{row}">
            <i class="el-icon-time"></i>
            <span>{{row.create_time}}</span>
          </template>
        </el-table-column>
        <el-table-column label="模型名称" min-width="150px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="handleUpdate(row)">{{row.modelname}}</span>
          </template>
        </el-table-column>
        <el-table-column label="上传作者" min-width="100" align="center">
          <template slot-scope="{row}">
            <i class="el-icon-user"></i>
            <span>{{row.author}}</span>
          </template>
        </el-table-column>
        <el-table-column label="引用次数" align="center" width="95">
          <template slot-scope="{row}">
            <span class="link-type">{{row.reference}}</span>
          </template>
        </el-table-column>
        <el-table-column label="模型评分" prop="star" sortable align="center" width="110">
          <template slot-scope="{row}">
            <i v-for="n in + row.star" :key="n" class="el-icon-star-on"></i>
          </template>
        </el-table-column>
        <el-table-column width="250" align="center" label="操作">
          <template slot-scope="{row, $index}">
            <el-button type="primary" size="mini" icon="el-icon-edit" @click="amenddialog(row.id)">
              编辑
            </el-button>
            <el-button type="danger" size="mini" icon="el-icon-delete" @click="deletedialog(row.id)">
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-pagination class="pagination" hide-on-single-page background @size-change="handleSizeChange" @current-change="handleCurrentChange"
       :current-page="currentPage" :page-sizes="[10,20,40,50]" :page-size="10"
                     layout="total, sizes, prev, pager, next, jumper" :total="total"></el-pagination>

      <el-dialog title="修改模型信息" :visible.sync="amendDialog" label-width="80px">
        <el-form :model="form">
          <el-form-item label="模型名称">
            <el-input v-model="form.name" placeholder="输入修改的模型名称"></el-input>
          </el-form-item>
          <el-form-item label="上传者姓名">
            <el-input v-model="form.author" placeholder="输入修改上传者"></el-input>
          </el-form-item>
          <el-form-item label="模型评分">
            <el-rate v-model="form.star" :max="5" style="margin-top: 10px"/>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="amendDialog = false">取 消</el-button>
          <el-button type="primary" @click="AmendModel">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="提示"
        :visible.sync="deleteDialog"
        width="30%">
        <span>确定删除该模型吗？</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="deleteDialog=false">取 消</el-button>
          <el-button type="danger" @click="DeleteModel">确 定</el-button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import { getmodel, fetchmodel, amendmodel, deletemodel } from "@/api/model";

export default {

  data() {
    return {
      searchContent:'',
      loading: false,
      importance: undefined,
      importantOptions:[1,2,3,4,5],
      listQuery:[],
      tableKey: 0,
      total:0,
      currentPage:1,
      amendDialog: false,
      deleteDialog: false,
      form: {
        id: null,
        name: '',
        author: '',
        star: null
      },
      deleteId: null,
    }
  },
  watch: {

  },
  methods: {
    amenddialog:function(id){
      this.amendDialog = true;
      this.form.id = id;
    },
    deletedialog:function(id){
      this.deleteId = id;
      this.deleteDialog = true
    },
    AmendModel:function(){
      var that = this;
      if (that.form.name === '' && that.form.author === '' && that.form.star === 0){
          that.$message.error('至少要填一个信息')
      }
      else{
          amendmodel(this.form).then(response=>{
              if (response.code === 20000){
                  that.$message({
                      message: '修改成功',
                      type: 'success'
                  });
                  that.form.id = null;
                  that.form.name = '';
                  that.form.author = '';
                  that.form.star = null;
                  that.amendDialog = false;
                  that.getAllModels()
              }
          })
      }
    },
    DeleteModel:function(){
      var that = this;
      let data = {};
      data['id'] = that.deleteId;
      deletemodel(data).then(response=>{
        if (response.code === 20000){
            that.$message({
                message: '删除成功',
                type: 'success'
            });
            that.deleteId = null;
            that.deleteDialog = false;
            that.getAllModels()
        }
      })
    },
    handleSizeChange:function(){

    },
    handleCurrentChange:function(){

    },
    SearchClick:function () {
      var that = this;
      let data = {};
      if (this.searchContent !== ''){
        data['title'] = this.searchContent
      }
      if (this.importance !== undefined && this.importance !== ''){
        data['star'] = this.importance
      }
      fetchmodel(data).then(response=>{
        that.listQuery = response.data
      })
    },
    EditClick:function () {

    },
    LoadClick:function () {

    },
    SortChange:function () {

    },
    getSortClass: function(key) {
      const sort = this.listQuery.sort;
      return sort === `+${key}` ? 'ascending' : 'descending'
    },
    getAllModels:function () {
      var that = this;
      that.loading = true;
      setTimeout(function () {
          that.loading = false
      }, 1000);
      getmodel().then(response=>{
        that.listQuery = response.data;
        this.total = response.data.length
      })
    }
  },
  mounted() {
    this.getAllModels()
  }
}
</script>
<style scoped>
  .main-content{
    position: relative;
    width: 98%;
    min-height: 700px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    margin: 0 auto;
    padding: 10px 10px;
  }
  .input-content{
    margin-top: 20px;
  }
  .search-item{
    width: 200px;
    float: left;
    margin-left: 20px;
    margin-bottom: 20px;
  }
  .option-item{
    float: left;
    margin-left: 20px;
    width: 150px;
    margin-bottom: 20px;
  }
  .search-btn{
    float: left;
    margin-left: 20px;
    margin-bottom: 20px;
  }
  .link-type{
    color: #36a3f7;cursor: pointer;
  }
  .pagination{
    margin-top: 50px
  }
</style>

