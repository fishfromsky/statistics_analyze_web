<template>
  <div>
    <el-table
      v-loading="table_loading"
      :key="tablekey"
      :data="page_data"
      border
      fit
      highlight-current-row
      style="width: 100%; margin-top: 20px"
    >
      <el-table-column label="结果文件">
        <template slot-scope="{ row }">
          <span>{{ row.file_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="数据操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="primary"
            @click="Visualization(scope.$index)"
            >可视化</el-button
          >
          <el-button size="mini" type="primary" @click="Download(scope.$index)"
            >下载</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="DeleteExcel(scope.$index)"
            >删除</el-button
          >
          <el-button size="mini" type="success" @click="makePrediction(scope.$index)">预测</el-button>
          <el-button size="mini" type="warning" @click="excelPrediction(scope.$index)">表格预测</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-drawer :visible.sync="drawer_dialog" direction="rtl" size="50%">
      <el-scrollbar style="height: 100vh">
        <div class="drawer-container">
          <div class="drawer-title">导入表格预测数值</div>
          <div class="divider" style="margin-top: 10px"></div>
          <div class="drawer-vice-title">1  导入实验数据文件</div>
          <el-upload
            class="upload-demo"
            action="http://101.133.238.216:8000/api/uploadtestfile"
            :file-list="fileList"
            :on-error="handleError"
            :on-success="handleSuccess"
            style="margin-top: 20px">
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">
              上传数据文件，仅限excel文件
            </div>
          </el-upload>
          <div class="divider" style="margin-top: 20px"></div>
          <div class="drawer-vice-title">2  选择实验数据文件</div>
          <el-table v-loading="table_loading_predict" :key="tablekey_predict"
          :data="page_data_predict" border fit highlight-current-row style="width: 100%; margin-top: 20px">
            <el-table-column label="上传日期" align="center">
              <template slot-scope="{row}">
                <span>{{row.time}}</span>
              </template>
            </el-table-column>
            <el-table-column label="文件名" align="center">
              <template slot-scope="{row}">
                <span>{{row.name}}</span>
              </template>
            </el-table-column>
            <el-table-column label="操作" align="center">
              <template slot-scope="scope">
                <el-button type="success" size="mini" @click="startPredictfromExcel(scope.$index)">预测</el-button>
                <el-button type="danger" size="mini" @click="deletePredictfromExcel(scope.$index)">删除</el-button>
                <el-button type="primary" size="mini" @click="seePredictfromExcel">结果</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-pagination
            @size-change="handleSizeChangePreidct"
            @current-change="handleCurrentChangePredict"
            :current-page="currentPage_predict"
            :page-sizes="[10, 20, 30, 40, 50]"
            :page-size="page_size_predict"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total_size_predict"
            style="margin-top: 20px"
          />
        </div>
      </el-scrollbar>
    </el-drawer>
    <el-dialog :visible.sync="result_dialog" title="批量预测结果">
      <el-table :data="predictResult" border style="margin-top: 20px">
        <el-table-column label="运行结果文件" prop="file_name"></el-table-column>
        <el-table-column fixed="right" label="操作" width="100">
          <template slot-scope="{ row }">
            <a style="color: #1890FF; font-size: 12px" :href="row.url">下载</a>
            <el-button
              @click="DeletePredictionResult(row.path)"
              type="text"
              size="small"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog :visible.sync="chart_dialog">
      <chartresult :chart-data="graph_data" style="height: 35vh"></chartresult>
      <div class="report">
        <div class="report-item">
          <div class="report-title">预测指标:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.choose_data }}
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">参考指标:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.choose_col }}
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">回归公式:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.formula }}
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">R方指数:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.r_square }}
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">MSE指数:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.mse }}
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">RMSE指数:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.rmse }}
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">MAE指数:</div>
          <div class="report-title" style="margin-left: 10px">
            {{ report.mae }}
          </div>
        </div>
      </div>
    </el-dialog>
    <el-dialog title="数值预测" :visible.sync="predict_dialog">
      <div class="report">
        <div class="report-item">
          <div class="report-title">选择指标：</div>
          <div>{{predict_form.choose_col}}</div>
        </div>
        <div class="report-item">
          <div class="report-title">回归公式：</div>
          <div class="report-title">{{predict_form.formula}}</div>
        </div>
        <div class="report-item">
          <div class="report-title">填写参数：</div>
          <div class="input-container">
            <div v-for="item in predict_form.coef.length" :key="item">
              <el-input v-model="formula_params[item-1]" size="mini" style="width: 50px; margin-left: 10px; margin-bottom: 5px; float: left"></el-input>
            </div>
          </div>
        </div>
        <div class="report-item">
          <div class="report-title">预测结果</div>
          <div class="predict-result">{{predict_result}}</div>
        </div>
      </div>
      <div slot="footer">
        <el-button type="success" @click="startPrediction">开始预测</el-button>
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
      style="margin-top: 20px"
    >
    </el-pagination>
  </div>
</template>

<script>
import CountTo from 'vue-count-to'
import {
  getlinearregressionmodelresult,
  getlinearregressionresult,
  deletemodelfile,
  makepredictionlinearregression,
  gettestfilelist,
  startlinearpredictionfromexcel,
  getlinearpredictionfromexcel
} from "@/api/model";
import chartresult from "./components/resultchart";
export default {
  components: {
    chartresult,
    CountTo
  },
  props: {
    projectId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      chart_dialog: false,
      table_loading: false,
      tablekey: 0,
      tableData: [],
      weightData: [],
      page_data: [],
      total_size: 0,
      currentPage: 1,
      page_size: 10,
      project_id: "",
      filename: "lstm_result",
      autoWidth: true,
      bookType: "xlsx",
      sort_list: [],
      graph_data: {
        real: [],
        pred: [],
      },
      report: {
        formula: "",
        choose_col: "",
        choose_data: "",
        r_square: "",
        mse: "",
        rmse: "",
        mae: "",
      },
      predict_dialog: false,
      predict_form: {
        choose_col: '',
        coef: [],
        intercept: [],
        formula: ''
      },
      formula_params: [],
      predict_result: 0,
      drawer_dialog: false,
      fileList: [],
      selectpredictdatafile: null,
      tablekey_predict: 0,
      tableData_predict: [],
      page_data_predict: [],
      total_size_predict: 0,
      currentPage_predict: 1,
      page_size_predict: 10,
      table_loading_predict: false,
      predictResult: [],
      result_dialog: false
    };
  },
  watch: {
    projectId: function (a, _) {
      this.project_id = a;
      this.page_data = [];
      this.tableData = [];
      this.sort_list = [];
      this.weightData = [];
      this.initTable(a);
    },
  },
  methods: {
    DeletePredictionResult:function(path){
      let data = {}
      data['url'] = path
      deletemodelfile(data).then(res=>{
        if (res.code === 20000){
          this.$message.success('删除成功')
          this.seePredictfromExcel()
        }
      })
    },
    seePredictfromExcel:function(){
      let data = {}
      data['user'] = this.getCookie('environment_name')
      data['project_id'] = this.project_id
      getlinearpredictionfromexcel(data).then(res=>{
        if (res.code === 20000){
          let result = res.data;
          let result_data = [];
          for (let i = 0; i < result.length; i++) {
            let dict = {};
            let split_list = result[i].split("/");
            let path = "";
            for (let j = 3; j < split_list.length; j++) {
              if (j != split_list.length - 1) {
                path = path + split_list[j] + "/";
              } else {
                path = path + split_list[j];
              }
            }
            dict["url"] = result[i];
            dict["file_name"] = split_list[split_list.length - 1];
            dict["path"] = path;
            result_data.push(dict)
          }
          this.predictResult = result_data
          this.result_dialog = true
        }
      })
    },
    handleSizeChangePreidct:function(val){
      this.table_loading_predict = true;
      this.page_size_predict = val;
      this.currentPage_predict = 1;
      this.page_data_predict = [];
      this.getTestFileList()
    },
    handleCurrentChangePredict:function(val){
      this.currentPage_predict = val;
      this.page_data_predict = [];
      this.getTestFileList()
    },
    deletePredictfromExcel:function(val){
      let data = {}
      data['url'] = this.page_data_predict[val].path
      deletemodelfile(data).then(res=>{
        if (res.code === 20000){
          this.$message.success('删除成功')
          this.tableData_predict = []
          this.page_data_predict = []
          this.getTestFileList()
        }
      })
    },
    startPredictfromExcel:function(val){
      let data = {}
      data['result'] = this.selectpredictdatafile
      data['data'] = this.page_data_predict[val].path
      data['user'] = this.getCookie('environment_name')
      data['project_id'] = this.project_id
      startlinearpredictionfromexcel(data).then(res=>{
        if (res.code === 20000){
          this.$message.success('正在预测中...')
        }
      })
    },
    handleSuccess:function(){
      this.$message.success('上传成功')
      this.getTestFileList()
    },
    handleError:function(){
      this.$message.error('上传失败')
    },
    excelPrediction:function(val){
      this.drawer_dialog = true
      this.selectpredictdatafile = this.page_data[val].path
    },
    getTestFileList:function(){
      this.page_data_predict = []
      this.tableData_predict = []
      this.table_loading_predict = true
      gettestfilelist().then(res=>{
        if (res.code === 20000){
          let data = res.data;
          let predictData = []
          this.table_loading_predict = false
          for (let i = 0; i < data.length; i++) {
            let dict = {}
            dict["name"] = data[i].name;
            dict["path"] = data[i].url;
            let splttime = data[i].url.split("/");
            dict["time"] =
              splttime[splttime.length - 4] +
              "年" +
              splttime[splttime.length - 3] +
              "月" +
              splttime[splttime.length - 2] +
              "日";
            predictData.push(dict);
          }
          this.tableData_predict = predictData
          let size = this.page_size_predict;
          let index = this.currentPage_predict - 1;
          for (let i = index * size; i < (index + 1) * size; i++) {
            if (i == predictData.length) {
              break;
            }
            this.page_data_predict.push(predictData[i]);
          }
          this.total_size_predict = predictData.length;
        }
      })
    },
    startPrediction:function(){
      let flag = true
      for (let i=0; i<this.formula_params.length; i++){
        if (this.formula_params[i] === ''){
          flag = false
          this.$message.error('请输入完整参数')
          break
        }
      }
      if (flag){
        let sum = 0;
        for (let i=0; i<this.formula_params.length; i++){
          sum = sum + this.predict_form.coef[i]*parseFloat(this.formula_params[i])
        }
        sum = sum+this.predict_form.intercept[0]
        this.predict_result = sum.toFixed(4)
      }
    },
    DeleteExcel: function (val) {
      let that = this;
      let data = {};
      data["url"] = this.page_data[val].path;
      deletemodelfile(data).then((res) => {
        if (res.code === 20000) {
            this.$message({
            type: "success",
            message: "删除成功",
            });
            that.table_loading = true;
            that.tableData = [];
            that.page_data = [];
            that.weightData = [];
            that.initTable(that.project_id);
        }
      });
    },
    getCookie: function (name) {
      var strcookie = document.cookie;
      var arrcookie = strcookie.split("; ");
      for (var i = 0; i < arrcookie.length; i++) {
        var arr = arrcookie[i].split("=");
        if (arr[0] == name) {
          return arr[1];
        }
      }
      return "";
    },
    initTable: function (project_id) {
      let that = this;
      let data = {};
      data["project_id"] = project_id;
      data["user"] = this.getCookie("environment_name");
      getlinearregressionmodelresult(data).then((res) => {
        if (res.code === 20000) {
          that.table_loading = false;
          let result = res.data;
          let result_data = [];
          for (let i = 0; i < result.length; i++) {
            let dict = {};
            let split_list = result[i].split("/");
            let path = "";
            for (let j = 3; j < split_list.length; j++) {
              if (j != split_list.length - 1) {
                path = path + split_list[j] + "/";
              } else {
                path = path + split_list[j];
              }
            }
            dict["url"] = result[i];
            dict["file_name"] = split_list[split_list.length - 1];
            dict["path"] = path;
            result_data.push(dict);
          }
          that.tableData = result_data;
          let size = that.page_size;
          let index = that.currentPage - 1;
          for (let i = index * size; i < (index + 1) * size; i++) {
            if (i == result_data.length) {
              break;
            }
            that.page_data.push(result_data[i]);
          }
          that.total_size = result_data.length;
        }
      });
    },
    makePrediction(val){
      let data = {}
      data['path'] = this.page_data[val].path
      makepredictionlinearregression(data).then(res=>{
        if (res.code === 20000){
          this.formula_params = []
          this.predict_form.choose_col = res.choose_col
          this.predict_form.coef = res.coef
          this.predict_form.intercept = res.intercept
          this.predict_form.formula = res.formula
          this.predict_dialog = true
          for (let i=0; i<res.coef.length; i++){
            this.formula_params.push('')
          }
        }
      })
    },
    Visualization(val) {
      let that = this;
      let data = {};
      data["path"] = this.page_data[val].path;
      getlinearregressionresult(data).then((res) => {
        if (res.code === 20000) {
          that.graph_data.pred = res.pred;
          that.graph_data.real = res.fact;
          that.report.choose_col = res.choose_col;
          that.report.choose_data = res.choose_data;
          that.report.formula = res.formula;
          that.report.mse = res.mse;
          that.report.rmse = res.rmse;
          that.report.r_square = res.r_square;
          that.report.mae = res.mae;
          that.chart_dialog = true;
        }
      });
    },
    Download: function (val) {
      let file_path = this.page_data[val].url;
      window.open(file_path);
    },
    handleSizeChange: function (val) {
      this.table_loading = true;
      this.page_size = val;
      this.currentPage = 1;
      this.page_data = [];
      this.initTable(this.project_id);
    },
    handleCurrentChange: function (val) {
      this.currentPage = val;
      this.page_data = [];
      this.initTable(this.project_id);
    },
  },
  mounted() {
    this.getTestFileList()
  },
};
</script>

<style scoped>
.report {
  width: 100%;
  min-height: 10vh;
  padding: 20px;
}
.report-item {
  margin-top: 10px;
  width: 100%;
  min-height: 20px;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.report-title {
  font-size: 15px;
}
.predict-result{
  font-size: 20px;
  margin-left: 20px;
  color: orangered;
}
.drawer-container{
  width: 100%;
  min-height: 400px;
  padding: 20px;
  margin-bottom: 10vh;
}
.drawer-title{
  color: dimgrey;
  font-size: 20px;
}
.drawer-vice-title{
  color: dimgray;
  font-size: 15px;
  margin-top: 20px;
}
.divider{
  width: 100%;
  height: 0;
  border-top: 1px solid #555;
}
.input-container{
  width: 100%;
  min-height: 40px;
}
</style>
