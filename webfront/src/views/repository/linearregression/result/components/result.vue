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
        </template>
      </el-table-column>
    </el-table>
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
  getlinearregressionmodelresult,
  getlinearregressionresult,
  deleterelationexcelresult,
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
        formula: "",
        choose_col: "",
        choose_data: "",
        r_square: "",
        mse: "",
        rmse: "",
        mae: "",
      },
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
    DeleteExcel: function (val) {
      let that = this;
      let data = {};
      data["url"] = this.tableData[val].url;
      deleterelationexcelresult(data).then((res) => {
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