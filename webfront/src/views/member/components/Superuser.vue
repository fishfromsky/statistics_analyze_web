<template>
  <div class="user-container">
    <div class="card-box">
      <el-input type="text" placeholder="搜索姓名关键字" v-model="search_name" class="search_input"></el-input>
      <el-button type="primary" icon="el-icon-search" class="search-btn" @click="handleSearch">搜索账号</el-button>
      <div class="divider"></div>
      <el-button type="warning" icon="el-icon-circle-plus-outline" class="add_superuser" @click="addSuperuser">增加账号</el-button>
    </div>
    <div class="main-content">
      <el-table v-loading="loading" :key="tableKey" :data="listQuery" border fit highlight-current-row style="width: 100%">
        <el-table-column label="编号" align="center" min-width="50">
          <template slot-scope="{row}">
            <span>{{row.id}}</span>
          </template>
        </el-table-column>
        <el-table-column label="用户名" align="center" min-width="80">
          <template slot-scope="{row}">
            <span>{{row.username}}</span>
          </template>
        </el-table-column>
        <el-table-column label="密码" align="center" min-width="80">
          <template slot-scope="{row}">
            <span>{{row.password}}</span>
          </template>
        </el-table-column>
        <el-table-column label="邮箱" align="center" min-width="130">
          <template slot-scope="{row}">
            <span>{{row.email}}</span>
          </template>
        </el-table-column>
        <el-table-column label="电话" align="center" min-width="100">
          <template slot-scope="{row}">
            <span>{{row.phone_number}}</span>
          </template>
        </el-table-column>
        <el-table-column label="创建时间" align="center" min-width="100">
          <template slot-scope="{row}">
            <span>{{row.date_joined}}</span>
          </template>
        </el-table-column>
        <el-table-column width="250" label="操作" align="center">
          <template slot-scope="{row, $index}">
            <el-button type="primary" size="mini" icon="el-icon-edit">
              编辑
            </el-button>
            <el-button type="danger" size="mini" icon="el-icon-delete" @click="deleteDialog(row.id)">
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination class="pagination" hide-on-single-page background @size-change="handleSizeChange" @current-change="handleCurrentChange"
                     :current-page="currentPage" :page-sizes="[10,20,40,50]" :page-size="10"
                     layout="total, sizes, prev, pager, next, jumper" :total="total"></el-pagination>
    </div>
    <el-dialog title="增加超级管理员" :visible.sync="add_dialog" width="40%">
      <el-form :model="form">
        <el-form-item label="账号名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" placeholder="输入账号名称"></el-input>
        </el-form-item>
        <el-form-item label="账号密码" :label-width="formLabelWidth">
          <el-input v-model="form.password" placeholder="输入账号密码"></el-input>
        </el-form-item>
        <el-form-item label="联系电话" :label-width="formLabelWidth">
          <el-input v-model="form.phone" placeholder="输入联系电话号码"></el-input>
        </el-form-item>
        <el-form-item label="联系邮箱" :label-width="formLabelWidth">
          <el-input v-model="form.email" placeholder="输入账号联系邮箱"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="add_dialog = false">取 消</el-button>
        <el-button type="primary" @click="addConfirm">确 定</el-button>
      </div>
    </el-dialog>
    <el-dialog
      title="删除超级用户"
      :visible.sync="delete_dialog"
      width="30%">
      <span>确定删除该账户信息吗？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="delete_dialog = false">取 消</el-button>
        <el-button type="danger" @click="deleteSuperuser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
    import { getsuperuser, fetchsuperuser, addsuperuser } from '@/api/user'
    import {deletesuperuser} from "../../../api/user";

    export default {
        name: 'Superuser',
        data(){
            return {
                search_name: '',
                tableKey: 0,
                currentPage: 0,
                total:1,
                listQuery: [],
                loading: false,
                add_dialog: false,
                delete_dialog: false,
                form: {
                    name: '',
                    password: '',
                    email: '',
                    phone: ''
                },
                formLabelWidth: '100px',
                deleteId: null
            }
        },
        methods: {
            handleSearch:function(){
                var that = this;
                that.loading = true;
                setTimeout(function () {
                    that.loading = false
                }, 1000)
                let dict = {};
                dict['name'] = this.search_name;
                fetchsuperuser(dict).then(response => {
                    that.listQuery = response.data
                })
            },
            handleSizeChange:function(){

            },
            handleCurrentChange:function(){

            },
            getData:function() {
                var that = this
                that.loading = true;
                setTimeout(function () {
                    that.loading = false
                }, 1000)
                getsuperuser().then(response => {
                    that.listQuery = response.data
                })
            },
            addSuperuser:function () {
                this.add_dialog = true
            },
            addConfirm:function () {
              var that = this;
              if (this.form.name === '' || this.form.password === '' || this.form.email === '' || this.form.phone === ''){
                  this.$message.error('请输入完整数据')
              }
              else{
                  addsuperuser(this.form).then(res=>{
                      if (res.code === 20000){
                          this.$message({
                              message: '添加成功',
                              type:'success'
                          })
                          that.add_dialog = false
                          that.form.name = ''
                          that.form.password = ''
                          that.form.email = ''
                          that.form.phone = ''
                          that.getData()
                      }
                  })
              }
            },
            deleteDialog:function (id) {
              this.deleteId = id
              this.delete_dialog = true
            },
            deleteSuperuser:function () {
                var that = this;
                let data = {}
                data['id'] = this.deleteId
                deletesuperuser(data).then(res=>{
                    if (res.code === 20000){
                        this.$message({
                            message: '删除成功',
                            type:'success'
                        })
                        that.deleteId = null
                        that.delete_dialog = false
                        that.getData()
                    }
                })
            }
        },
        mounted() {
            this.getData()
        }
    }
</script>

<style scoped>
  .card-box{
    width: 90%;
    height: 80px;
    background: #fff;
    margin: 0 auto;
    margin-top: 40px;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .search_input{
    width: 200px;
    float: left;
    margin-left: 20px;
  }
  .search-btn{
    float: left;
    margin-left: 20px;
  }
  .divider{
    height: 50px;
    width: 0;
    border-left: #ddd 1px solid;
    float: left;
    margin-left: 20px;
  }
  .main-content{
    width: 90%;
    margin: 0 auto;
    min-height: 300px;
    background: #fff;
    margin-top: 40px;
  }
  .pagination{
    margin-top: 50px;
  }
  .add_superuser{
    float: left;
    margin-left: 20px;
  }
</style>
