<template>
  <div class="dashboard-container">
    <div class="header">
      <div class="header-title">{{ algorithm_name }}</div>
    </div>
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :xs="24" :sm="24" :lg="16">
        <div class="main-step-header">
          <el-select
            v-model="selectdata"
            placeholder="选择实验数据"
            style="margin-left: 20px"
          >
            <el-option
              v-for="item in tableData"
              :key="item.index"
              :label="item.name"
              :value="item.index"
            ></el-option>
          </el-select>
          <el-button
            v-if="selectdata != null"
            type="primary"
            @click="ColSelect"
            style="margin-left: 10px"
            >参数选择</el-button
          >
        </div>
        <div class="main-step-content">
          <el-steps direction="vertical" :active="1">
            <el-step
              v-for="item in modellist"
              :key="item.id"
              :title="item.name"
            >
              <template slot="description">
                <div class="detail-card">
                  <div class="detail-card-container">
                    <div class="detail-img">
                      <el-image
                        :src="item.pic_url"
                        style="width: 100%; height: 100%"
                        :preview-src-list="[item.pic_url]"
                      ></el-image>
                    </div>
                    <div class="detail-title">
                      <span class="detail-title-1">{{ item.name }}</span>
                      <div class="divider"></div>
                      <span class="detail-title-2">{{ item.description }}</span>
                    </div>
                    <div class="vertical-divider"></div>
                    <div class="status-box">
                      <span class="status-title">模型运行状态</span>
                      <div class="status-label">
                        <el-tag type="primary">{{ item.status }}</el-tag>
                      </div>
                      <div class="status-panel">
                          <el-button type="text" size="mini" @click="Refresh">刷新状态</el-button>
                          <el-button type="text" size="mini" @click="seeResult(item.id)">查看结果</el-button>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
            </el-step>
          </el-steps>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="table-box">
          <div class="box-title">
            <span class="box-title-span">实验数据上传</span>
          </div>
          <el-upload
            class="upload-demo"
            action="http://127.0.0.1:8000/api/uploadfile"
            :file-list="fileList"
            :on-error="handleError"
            :on-success="handleSuccess"
          >
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">
              上传数据文件，仅限excel文件
            </div>
          </el-upload>
          <div class="box-title" style="margin-top: 10px">
            <span class="box-title-span">数据上传历史</span>
          </div>
          <el-date-picker
            v-model="filedate"
            type="date"
            placeholder="选择筛选日期"
          >
          </el-date-picker>
          <el-table
            :data="tableData"
            v-loading="table_loading"
            border
            style="margin-top: 20px"
          >
            <el-table-column
              label="日期"
              width="150"
              prop="time"
            ></el-table-column>
            <el-table-column label="文件名" prop="name"></el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
              <template slot-scope="scope">
                <el-button
                  @click="handleDownload(scope.row)"
                  type="text"
                  size="small"
                  >下载</el-button
                >
                <el-button
                  @click="handleDelete(scope.index)"
                  type="text"
                  size="small"
                  >删除</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-col>
    </el-row>
    <el-dialog
      :before-close="handleClose"
      :visible.sync="note_dialog"
      title="提示信息"
    >
      <span>请从编辑算法页面点击"开始实验"按钮进入本页面！</span>
      <div slot="footer">
        <el-button type="primary" @click="handleClose">确定</el-button>
      </div>
    </el-dialog>
    <el-dialog
      title="参数选择"
      :visible.sync="col_dialog"
      custom-class="col_dialog"
    >
      <div class="col_dialog">
        <span>选择需要进行关联分析的特征</span>
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
        <span>选择关联分析参考数据</span>
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
        <span>选取相关性前多少个特征作为预测数据</span>
        <el-input
          type="number"
          v-model="relative_max"
          placeholder="请输入特征数"
          style="width: 25%; margin-top: 20px"
        ></el-input>
      </div>
      <template slot="footer">
        <el-button @click="col_dialog = false">取消</el-button>
        <el-button type="primary" @click="ColSelectConfirm">确定</el-button>
      </template>
    </el-dialog>
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
  </div>
</template>

<script>
import {
  algorithmtestinfo,
  getexcelinfo,
  getfilelist,
  grouptestrelation,
  getrelationexcelresult,
  deleterelationexcelresult,
  getlstmexcelresult
} from "@/api/model";
export default {
  data() {
    return {
      result_dialog: false,
      selectdata: null,
      note_dialog: false,
      algorithm_name: "",
      algorithm_Id: null,
      username: "",
      time: "",
      modellist: [],
      fileList: [],
      filedate: "",
      selectfilePath: "",
      tableData: [],
      table_loading: false,
      rule: [],
      select_cols: [],
      checkList: [],
      select_cols_num: 0,
      reference_col: null,
      col_dialog: false,
      relative_max: null,
      excelList: [],
    };
  },
  watch: {
    selectdata(val) {
      let that = this;
      let data = {};
      data["url"] = this.tableData[val].path;
      this.selectfilePath = this.tableData[val].path;
      getexcelinfo(data).then((res) => {
        if (res.code === 20000) {
          that.select_cols = res.cols;
          that.select_cols_num = res.col_num;
        }
      });
    },
  },
  methods: {
      Refresh:function(){
          this.getWholeInfo()
      },
      seeResult:function(index){
          this.excelList = []
          this.result_dialog = true;
          if (index==16){
            this.getExcelResult(getrelationexcelresult);
          }
          else if (index==13){
            this.getExcelResult(getlstmexcelresult)
          }
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
    getIndex: function (arr, item) {
      for (let i = 0; i < arr.length; i++) {
        if (arr[i] == item) {
          return i;
        }
      }
    },
    ColSelectConfirm: function () {
      if (
        this.checkList.length === 0 ||
        this.reference_col === null ||
        this.relative_max === null
      ) {
        this.$message.error("填写信息必须完整");
      } else {
        let index_list = [];
        for (let i = 0; i < this.checkList.length; i++) {
          index_list.push(this.getIndex(this.select_cols, this.checkList[i]));
        }
        let index_select = this.getIndex(this.select_cols, this.reference_col);
        let flag = true;
        for (let i = 0; i < index_list.length; i++) {
          if (index_list[i] == index_select) {
            this.$message.error("参考列和实验列不能相同");
            flag = false;
            break;
          }
        }
        if (flag) {
          let data = {};
          let Idlist = []
          for (let i=0; i<this.modellist.length; i++){
            Idlist.push(this.modellist[i].id)
          }
          Idlist.shift()
          data["name"] = this.getCookie("environment_name");
          data["algorithm_id"] = this.algorithm_Id;
          data["model_id"] = this.modellist[0].id;
          data["path"] = this.selectfilePath;
          data["relative_max"] = this.relative_max;
          data["select_list"] = index_list.toString();
          data['next_list'] = Idlist.toString();
          data["choose_col"] = index_select;
          data["test_type"] = this.rule[1]
          grouptestrelation(data).then((res) => {
            if (res.code === 20000) {
              this.$message({
                type: "success",
                message: "运行成功",
              });
            }
          });
        }
      }
    },
    ColSelect: function () {
      this.col_dialog = true;
    },
    handleDownload: function (index) {},
    handleDelete: function (index) {},
    DownloadRelationExcel: function (index) {},
    DeleteRelationExcel: function (index) {
      let data = {};
      data["url"] = index;
      deleterelationexcelresult(data).then((res) => {
        if (res.code === 20000) {
          this.$message({
            type: "success",
            message: "删除成功",
          });
        }
      });
    },
    handleSuccess: function () {
      this.getFileList();
    },
    getExcelResult(func) {
      let that = this;
      let username = this.getCookie("environment_name");
      let data = {};
      this.excelList = []
      data["user"] = username;
      func(data).then((res) => {
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
    getFileList: function () {
      let that = this;
      this.tableData = [];
      this.table_loading = true;
      getfilelist().then((res) => {
        if (res.code === 20000) {
          let data = res.data;
          that.table_loading = false;
          for (let i = 0; i < data.length; i++) {
            let dict = {};
            dict["index"] = i;
            dict["name"] = data[i].name;
            dict["path"] = data[i].url;
            let splttime = data[i].url.split("\\");
            dict["time"] =
              splttime[splttime.length - 4] +
              "年" +
              splttime[splttime.length - 3] +
              "月" +
              splttime[splttime.length - 2] +
              "日";
            that.tableData.push(dict);
          }
        }
      });
    },
    handleError: function () {
      this.$message.error("上传文件失败");
    },
    handleClose: function () {
      this.$router.push({
        path: "/project/select",
      });
    },
    isEmptyObject: function (obj) {
      for (var key in obj) {
        return false;
      }
      return true;
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
    getmodelList: function () {
      let data = {};
      data["name"] = this.username;
      data["algorithm_id"] = this.algorithm_Id;
    },
    getWholeInfo:function(){
        let that = this
        let data = {}
        data['name'] = this.username
        data['algorithm_id'] = this.algorithm_Id
        algorithmtestinfo(data).then(res=>{
            if (res.code === 20000){
                let data = res.data[0];
                let algorithm = data.algorithm;
                that.modellist = data.model;
                that.algorithm_name = algorithm.name;
                that.algorithm_Id = algorithm.project_id;
                that.time = algorithm.add_time;
            }
        })
    }
  },
  created() {
    let that = this;
    let params = this.$route.query;
    if (this.isEmptyObject(params)) {
      this.note_dialog = true;
    } else {
      let data = {};
      data["name"] = params.username;
      this.username = params.username;
      this.rule = params.rule;
      data["algorithm_id"] = params.algorithm_Id;
      algorithmtestinfo(data).then((res) => {
        if (res.code === 20000) {
          let data = res.data[0];
          let algorithm = data.algorithm;
          that.modellist = data.model;
          that.algorithm_name = algorithm.name;
          that.algorithm_Id = algorithm.project_id;
          that.time = algorithm.add_time;
        }
      });
    }
  },
  mounted() {
    this.getFileList();
  },
};
</script>

<style scoped lang="scss">
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.header {
  width: 100%;
  height: 50px;
  background: #3A71A8;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
  display: flex;
  flex-direction: row;
  align-items: center;
  &-title {
    margin-left: 20px;
    font-size: 20px;
    font-weight: bold;
    color: #fff;
  }
}
.main-step-content {
  width: 100%;
  min-height: 400px;
  padding: 20px;
  overflow-y: auto;
  /deep/ .el-step__description {
    padding-right: 0%;
    margin-top: 10px;
    margin-bottom: 10px;
    font-size: 12px;
    line-height: 20px;
    font-weight: normal;
  }
}
.detail-card {
  width: 100%;
  min-height: 120px;
  background: #fff;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
.detail-img {
  width: 20%;
  height: 80px;
}
.detail-title {
  width: 50%;
  min-height: 120px;
  display: flex;
  flex-direction: column;
  margin-left: 10px;
  &-1 {
    font-size: 20px;
    font-weight: bold;
    color: #3A71A8;
    margin-bottom: 10px;
    margin-top: 10px;
  }
  &-2 {
    font-size: 12px;
    color: #333;
    margin-top: 10px;
  }
}
.divider {
  width: 100%;
  height: 0;
  border: 2px solid #409EFF;
}
.table-box {
  width: 100%;
  min-height: 400px;
  background: #fff;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
  padding: 10px;
}
.box-title {
  width: 100%;
  height: 40px;
  &-span {
    color: #4AB7BD;
    font-size: 20px;
    font-weight: bold;
  }
}
.vertical-divider {
  width: 0;
  height: 90px;
  border-left: #999 1px solid;
  margin-left: 20px;
}
.status-box {
  width: 30%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.status-title {
  color: #4ab7bd;
  font-size: 18px;
  font-weight: bold;
  margin-left: 20px;
}
.status-label {
  width: 100%;
  height: 80px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.main-step-header {
  width: 100%;
  height: 60px;
  background: #fff;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
  display: flex;
  flex-direction: row;
  align-items: center;
}
.col_dialog {
  width: 100%;
  min-height: 100px;
  display: flex;
  flex-direction: column;
}
.detail-card-container {
  width: 100%;
  min-height: 120px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 10px;
}
.row-divider {
  width: 90%;
  margin-left: 5%;
  border-top: #999 1px solid;
}
.detail-card-result {
  width: 100%;
  height: 100%;
  padding: 20px;
}
.status-panel{
    width: 100%;
    height: 50px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
}
</style>