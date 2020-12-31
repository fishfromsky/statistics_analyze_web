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
    <el-dialog :visible.sync="chart_dialog" width="60%">
      <chartresult :chart-data="graph_data" style="height: 60vh"></chartresult>
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
  getpearsonrmodelresult,
  getpearsonrelationresult,
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
        label: [],
        p_value: [],
        relate: []
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
      getpearsonrmodelresult(data).then((res) => {
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
      let data = {};
      data["path"] = this.page_data[val].path;
      getpearsonrelationresult(data).then((res) => {
        if (res.code === 20000) {
            this.graph_data.label = res.label
            this.graph_data.p_value = res.p_value
            this.graph_data.relate = res.relate
            this.chart_dialog = true
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