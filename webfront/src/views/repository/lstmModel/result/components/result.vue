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
          <el-button size="mini" type="success" @click="getPrediction">查看预测结果</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog :visible.sync="result_dialog" title="实验结果历史记录">
      <el-table :data="excelList" border style="margin-top: 20px">
        <el-table-column label="运行结果文件" prop="name"></el-table-column>
        <el-table-column fixed="right" label="操作" width="100">
          <template slot-scope="{ row }">
            <a style="color: #1890FF; font-size: 12px" :href="row.url">下载</a>
            <el-button
              @click="DeleteRelationExcel(row.url)"
              type="text"
              size="small"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog title="数值预测" :visible.sync="predict_dialog">
      <div class="report">
        <div class="report-item">
          <div class="report-title">输入预测年数：</div>
          <el-input type="number" v-model="predictDay" style="margin-left: 20px; width: 120px"></el-input>
        </div>
      </div>
      <div slot="footer">
        <el-button type="success" @click="startPrediction">开始预测</el-button>
      </div>
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
import {
  getlstmmodelresult,
  getlstmresult,
  getlstmreport,
  deleterelationexcelresult,
  LstmProjectStart,
  getdatapathfromresult,
  getexcelinfo,
  makepredictionLSTM,
  getlstmpredictionresult
} from "@/api/model";
import chartresult from "./components/resultchart";
export default {
  components: {
    chartresult,
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
        choose_col: "",
        choose_data: "",
        r_square: "",
        mse: "",
        rmse: "",
        mae: "",
      },
      predictDay: '',
      predict_dialog: false,
      predictFilePath: '',
      result_dialog: false,
      excelList: []
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
    getPrediction:function(){
      this.result_dialog = true
      this.getExcelResult()
    },
    getExcelResult() {
      let that = this;
      let username = this.getCookie("environment_name");
      let data = {};
      this.excelList = []
      data["user"] = username;
      data['project_id'] = this.project_id
      getlstmpredictionresult(data).then((res) => {
        if (res.code === 20000) {
          let result = res.data;
          for (let i = 0; i < result.length; i++) {
            let dict = {};
            dict["url"] = result[i];
            let name = result[i].split("/");
            dict["name"] = name[name.length - 1];
            that.excelList.push(dict);
          }
        }
      });
    },
    DeleteRelationExcel: function (index) {
      let that = this
      let data = {};
      data["url"] = index;
      deleterelationexcelresult(data).then((res) => {
        if (res.code === 20000) {
          that.result_dialog = false
          this.$message({
            type: "success",
            message: "删除成功",
          });
          this.getExcelResult()
        }
      });
    },
    DeleteExcel: function (val) {
      let that = this;
      let data = {};
      data["url"] = this.tableData[val].url;
      deleterelationexcelresult(data).then((res) => {
        if (res.code === 20000) {
          let weight_data = {};
          weight_data["url"] = this.weightData[val];
          deleterelationexcelresult(weight_data).then((res) => {
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
      getlstmmodelresult(data).then((res) => {
        if (res.code === 20000) {
          that.table_loading = false;
          let result = res.data;
          let result_data = [];
          for (let i = 0; i < result.length; i++) {
            let dict = {};
            let pre_split = result[i].split(".");
            let split_list = result[i].split("/");
            let path = "";
            for (let j = 3; j < split_list.length; j++) {
              if (j != split_list.length - 1) {
                path = path + split_list[j] + "/";
              } else {
                path = path + split_list[j];
              }
            }
            if (pre_split[pre_split.length - 1] === "xlsx") {
              dict["url"] = result[i];
              dict["file_name"] = split_list[split_list.length - 1];
              dict["path"] = path;
              result_data.push(dict);
            } else {
              that.weightData.push(path);
            }
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
    makePrediction:function(val){
      this.predict_dialog = true
      this.predictFilePath = this.page_data[val].path
    },
    startPrediction:function(){
      if (this.predictDay <= 0){
        this.$message.error('输入年数必须大于0')
      }
      else if (this.predictDay > 10){
        this.$message.error('输入年数必须小于10')
      }
      else{
        let data = {}
        data['path'] = this.predictFilePath
        data["project_id"] = this.project_id;
        data["user"] = this.getCookie("environment_name");
        data['days'] = this.predictDay
        makepredictionLSTM(data).then(res=>{
          if (res.code === 20000){
            this.$message.success('正在预测中')
            this.predict_dialog = false
          }
        })
      }
    },
    Visualization(val) {
      let that = this;
      let data = {};
      data["path"] = this.page_data[val].path;
      getlstmresult(data).then((res) => {
        if (res.code === 20000) {
          that.graph_data.pred = res.pred;
          that.graph_data.real = res.fact;
          that.report.choose_col = res.choose_col;
          that.report.choose_data = res.choose_data;
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
  mounted() {},
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
</style>