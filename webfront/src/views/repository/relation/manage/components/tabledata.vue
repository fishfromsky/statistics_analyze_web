<template>
  <div>
    <el-table
      v-show="tableshow"
      v-loading="table_loading"
      :key="tablekey"
      :data="page_data"
      border
      fit
      highlight-current-row
      style="width: 100%; margin-top: 20px"
    >
      <el-table-column label="项目ID" align="center" width="50">
        <template slot-scope="{ row }">
          <span>{{ row.project_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="项目名称" align="center" min-width="80">
        <template slot-scope="{ row }">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="运行类型" align="center" min-width="50">
        <template slot-scope="{ row }">
          <el-tag>{{ row.tag }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="运行状态" align="center" min-width="50">
        <template slot-scope="scope">
          <el-tag
            :type="
              scope.row.status == '未运行'
                ? 'info'
                : scope.row.status == '正在运行'
                ? 'success'
                : 'danger'
            "
            >{{ scope.row.status }}</el-tag
          >
          <el-button
            size="mini"
            @click="Refresh"
            type="primary"
            style="margin-top: 5px"
            >刷新</el-button
          >
        </template>
      </el-table-column>
      <el-table-column label="数据操作" align="center">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="primary"
            @click="AmendData(scope.$index)"
            style="margin-bottom: 5px"
            >修改</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="Experiment(scope.$index)"
            style="margin-bottom: 5px"
            >实验</el-button
          >
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
      style="margin-top: 20px"
    >
    </el-pagination>
    <el-dialog
      :visible.sync="choose_data_dialog"
      title="实验数据文件选择"
      width="30%"
    >
      <div class="option-header">
        <el-select
          v-model="selectdata"
          placeholder="选择实验数据"
          style="margin-left: 20px"
        >
          <el-option
            v-for="item in fileData"
            :key="item.index"
            :label="item.name"
            :value="item.index"
          ></el-option>
        </el-select>
        <el-button type="primary" @click="chooseData" style="margin-left: 20px"
          >确定</el-button
        >
      </div>
    </el-dialog>
    <el-dialog
      :visible.sync="choose_col_dialog"
      title="选择实验参数"
      custom-class="col_dialog"
    >
      <div class="col_dialog">
        <span>选择关联分析参考指标</span>
        <el-radio-group
          v-model="reference_col"
          style="margin-top: 20px; margin-bottom: 20px"
        >
          <el-radio
            v-for="item in select_cols"
            :label="item"
            :key="item"
          ></el-radio>
        </el-radio-group>
        <span>选择需要关联分析的指标</span>
        <el-checkbox-group
          v-model="checkList"
          style="margin-top: 20px; margin-bottom: 20px"
        >
          <el-checkbox
            v-for="item in select_cols"
            :label="item"
            :key="item"
          ></el-checkbox>
        </el-checkbox-group>
      </div>
        <div slot="footer">
            <el-button @click="choose_col_dialog=false">取消</el-button>
            <el-button type="primary" @click="startExperiment">确定</el-button>
        </div>
    </el-dialog>
    <el-dialog :visible.sync="amend_dialog" title="修改数据" width="40%">
      <el-form :model="form">
          <el-form-item label="项目名称">
              <el-input v-model="form.name" auto-complete="off"></el-input>
          </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
          <el-button @click="amend_dialog = false">取 消</el-button>
          <el-button type="primary" @click="AmendDataConfirm">确 定</el-button>
      </div>
    </el-dialog>
    <el-dialog :visible.sync="add_dialog" title="添加数据">
        <el-form :model="add_form">
            <el-form-item label="项目ID">
                <el-input v-model="add_form.project_id" placeholder="请输入项目ID" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="项目名称">
                <el-input v-model="add_form.name" placeholder="请输入项目名称" auto-complete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer">
            <el-button @click="add_dialog=false">取消</el-button>
            <el-button @click="addDataConfirm" type="primary">确定</el-button>
        </div>
    </el-dialog>
    <el-dialog :visible.sync="choose_dialog" title="选择关联分析算法" width="30%">
        <el-select v-model="choose_value" placeholder="请选择想要进行的算法">
            <el-option v-for="item in choose_item" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
        <div slot="footer">
            <el-button @click="choose_dialog=false">取消</el-button>
            <el-button @click="ExperimentConfirm" type="primary">确定</el-button>
        </div>
    </el-dialog>
  </div>
</template>

<script>
import { getrelationfilelist, getrelationproject, getexcelinfo, startrelation, addrelationproject, amendrelationproject } from "@/api/model";
export default {
  data() {
    return {
      tableshow: true,
      table_loading: false,
      tablekey: 0,
      tableData: [],
      page_data: [],
      total_size: 0,
      currentPage: 1,
      page_size: 10,
      fileData: [],
      choose_data_dialog: false,
      selectdata: null,
      selected_project_index: null,
      selectfilePath: null,
      select_cols: null,
      select_cols_num: null,
      choose_col_dialog: false,
      reference_col: null,
      checkList: [],
      add_form: {},
      add_dialog: false,
      form: {},
      amend_dialog: false,
      choose_dialog: false,
      choose_value: null,
      choose_item: [
        { value: '1', label: '相关矩阵'},
        { value: '2', label: '随机森林'},
        { value: '3', label: '灰度分析'},
        { value: '4', label: '皮尔逊系数'}
      ],
    };
  },
  watch: {
    selectdata(val) {
      let that = this;
      let data = {};
      data["url"] = this.fileData[val].path;
      this.selectfilePath = this.fileData[val].path;
      getexcelinfo(data).then((res) => {
        if (res.code === 20000) {
          that.select_cols = res.cols;
          that.select_cols_num = res.col_num;
        }
      });
    },
  },
  methods: {
    isInArray(arr, item){
      for (let i=0; i<arr.length; i++){
        if (arr[i] === item){
          return true
        }
      }
      return false
    },
    AmendData(index){
        this.form = this.page_data[index]
        this.amend_dialog = true
    },
    AmendDataConfirm:function(){
      let that = this
      amendrelationproject(this.form).then(res=>{
        if (res.code === 20000){
          this.$message({
            type: 'success',
            message: '修改成功'
          })
          that.amend_dialog = false
          that.table_loading = true;
          that.page_data = [];
          that.tableData = [];
          that.getData();
        }
      })
    },
    addPrograme:function(){
      this.add_dialog = true
    },
    addDataConfirm:function(){
      let data = this.add_form
      if (this.add_form.project_id === ''){
          this.$message.error('请输入项目ID')
      }
      else if (this.add_form.name === ''){
          this.$message.error('请输入项目名称')
      }
      else{
        let that = this
        addrelationproject(this.add_form).then(res=>{
          if (res.code === 20000){
            this.$message({
              type: 'success',
              message: '添加成功'
            })
            that.add_dialog = false
            that.table_loading = true;
            that.page_data = [];
            that.tableData = [];
            that.getData();
          }
        })
      }
    },
    Select_Index: function (arr_main, arr_child) {
      let index = [];
      let flag = true;
      for (let i = 0; i < arr_main.length; i++) {
        flag = true;
        for (let j = 0; j < arr_child.length; j++) {
          if (arr_main[i] === arr_child[j]) {
            flag = false;
            break;
          }
        }
        if (flag) {
          index.push(i);
        }
      }
      return index;
    },
    getIndex:function(arr, item){
        for (let i=0; i<arr.length; i++){
            if (arr[i] === item){
                return i
            }
        }
    },
    getCookie:function(name){
        var strcookie = document.cookie;
        var arrcookie = strcookie.split("; ");
        for ( var i = 0; i < arrcookie.length; i++) {
            var arr = arrcookie[i].split("=");
            if (arr[0] == name){
                return arr[1];
            }
        }
        return "";
    },
    startExperiment:function(){
        this.choose_dialog = true
    },
    ExperimentConfirm:function(){
      let that = this
        if (this.reference_col === null){
            this.$message.error('请选择关联分析参考指标')
        }
        else if (this.checkList.length === 0){
            this.$message.error('请选择需要关联分析的指标')
        }
        else if (this.choose_value === null){
          this.$message.error('请选择关联分析算法')
        }
        else if (this.isInArray(this.checkList, this.reference_col)){
          this.$message.error('参考指标和实验指标不能重叠')
        }
        else{
          this.choose_col_dialog = false
          this.choose_data_dialog = false
          let data = {}
          data['project_id'] = this.page_data[this.selected_project_index].project_id
          let index_list = this.Select_Index(this.select_cols, this.checkList)
          data['drop_col'] = index_list
          data['special'] = this.getIndex(this.select_cols, this.reference_col)
          data['path'] = this.selectfilePath
          data['name'] = this.getCookie('environment_name')
          data['algorithm'] = this.choose_value
          startrelation(data).then(res=>{
            if (res.code === 20000){
              this.$message({
                  type: 'success',
                  message: '运行成功'
              })
              that.table_loading = true;
              that.page_data = [];
              that.tableData = [];
              that.getData();
              that.choose_dialog = false
            }
          })
        }
    },
    chooseData:function(){
        this.choose_col_dialog = true
    },
    Refresh: function () {
      this.table_loading = true;
      this.page_data = [];
      this.tableData = [];
      this.getData()
    },
    Experiment: function (val) {
      this.selected_project_index = val;
      this.choose_data_dialog = true;
    },
    getData: function () {
      let that = this;
      getrelationproject().then((res) => {
        if (res.code === 20000) {
          that.table_loading = false;
          that.tableData = res.data;
          let size = that.page_size;
          let index = that.currentPage - 1;
          for (let i = index * size; i < (index + 1) * size; i++) {
            if (i == res.data.length) {
              break;
            }
            res.data[i].tag = "未选择";
            that.page_data.push(res.data[i]);
          }
          that.total_size = res.data.length;
        }
      });
    },
    getFileList: function () {
      let that = this;
      this.fileData = [];
      getrelationfilelist().then((res) => {
        if (res.code === 20000) {
          let data = res.data;
          for (let i = 0; i < data.length; i++) {
            let dict = {};
            dict["index"] = i;
            dict["name"] = data[i].name;
            dict["path"] = data[i].url;
            that.fileData.push(dict);
          }
        }
      });
    },
    handleSizeChange(val) {
      this.table_loading = true;
      this.page_size = val;
      this.currentPage = 1;
      this.page_data = [];
      this.getData();
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.page_data = [];
      this.getData();
    },
  },
  mounted() {
    this.getData();
    this.getFileList();
  },
};
</script>

<style scoped>
.option-header {
  width: 100%;
  display: flex;
  flex-direction: row;
}
.col_dialog {
  width: 100%;
  min-height: 100px;
  display: flex;
  flex-direction: column;
}
</style>