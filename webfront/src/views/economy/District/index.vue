<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="24" :lg="12">
        <el-select v-model="district_choose">
          <el-option
            v-for="item in district_options"
            :key="item.label"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
        <div class="chart-wrapper">
          <gdp :chartData="BasicInfo.GDPData" style="height: 35vh"></gdp>
        </div>
        <div class="chart-wrapper">
          <gdpfirstindustry
            :chartData="BasicInfo.GDP_First_Industry"
            style="height: 35vh"
          ></gdpfirstindustry>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper" style="margin-top: 60px">
          <gdpsecondindustry
            :chartData="BasicInfo.GDP_Second_Industry"
            style="height: 35vh"
          ></gdpsecondindustry>
        </div>
        <div class="chart-wrapper">
          <gdpthirdindustry
            :chartData="BasicInfo.GDP_Third_Industry"
            style="height: 35vh"
          ></gdpthirdindustry>
        </div>
      </el-col>
    </el-row>
    <div class="divider"></div>
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :xs="24" :sm="24" :lg="12">
        <el-select v-model="district_choose_two">
          <el-option
            v-for="item in district_options"
            :key="item.label"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
        <el-select v-model="choose_year_two">
          <el-option
            v-for="item in BasicInfo.GDPData.year"
            :key="item"
            :label="item"
            :value="item"
          ></el-option>
        </el-select>
        <div class="chart-wrapper">
          <piedata :chartData="PieInfo" style="height: 35vh"></piedata>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <el-select v-model="choose_year_one">
          <el-option
            v-for="item in total_year"
            :key="item"
            :label="item"
            :value="item"
          ></el-option>
        </el-select>
        <div class="chart-wrapper">
          <bardata :chartData="BarInfo" style="height: 35vh"></bardata>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {
  filtereconomydistrict,
  filterpieeconomydistrict,
  geteconomydistrict,
  filterbareconomydistrict,
} from "@/api/model";
import gdp from "./components/gdp";
import gdpfirstindustry from "./components/gdp_first_industry";
import gdpsecondindustry from "./components/gdp_second_industry";
import gdpthirdindustry from "./components/gdp_third_industry";
import piedata from "./components/piedata";
import bardata from "./components/bardata";
export default {
  name: "index",
  components: {
    gdp,
    gdpfirstindustry,
    gdpsecondindustry,
    gdpthirdindustry,
    piedata,
    bardata,
  },
  data() {
    return {
      total_year: [],
      choose_year_one: "2017",
      district_choose_two: "浦东新区",
      choose_year_two: "2017",
      district_choose: "浦东新区",
      district_options: [
        { label: "黄浦区", value: "黄浦区" },
        { label: "普陀区", value: "普陀区" },
        { label: "静安区", value: "静安区" },
        { label: "长宁区", value: "长宁区" },
        { label: "徐汇区", value: "徐汇区" },
        { label: "虹口区", value: "虹口区" },
        { label: "杨浦区", value: "杨浦区" },
        { label: "宝山区", value: "宝山区" },
        { label: "嘉定区", value: "嘉定区" },
        { label: "闵行区", value: "闵行区" },
        { label: "浦东新区", value: "浦东新区" },
        { label: "金山区", value: "金山区" },
        { label: "松江区", value: "松江区" },
        { label: "青浦区", value: "青浦区" },
        { label: "崇明区", value: "崇明区" },
        { label: "奉贤区", value: "奉贤区" },
      ],
      BasicInfo: {
        GDPData: {
          year: [],
          gdp: [],
          district: "",
        },
        GDP_First_Industry: {
          year: [],
          gdp: [],
          district: "",
        },
        GDP_Second_Industry: {
          year: [],
          gdp: [],
          district: "",
        },
        GDP_Third_Industry: {
          year: [],
          gdp: [],
          district: "",
        },
      },
      PieInfo: {
        data: [],
        district: "",
        year: "",
      },
      BarInfo: {
        district: [],
        gdp: [],
        gdp_first_industry: [],
        gdp_second_industry: [],
        gdp_third_industry: [],
      },
    };
  },
  watch: {
    district_choose(val) {
      this.getGDPData(val);
    },
    district_choose_two(val) {
      this.getPieData();
    },
    choose_year_two(val) {
      this.getPieData();
    },
    choose_year_one(val) {
      this.getBarData();
    },
  },
  methods: {
    isInArray: function (arr, value) {
      for (var i = 0; i < arr.length; i++) {
        if (value === arr[i]) {
          return true;
        }
      }
      return false;
    },
    getGDPData: function (place) {
      let that = this;
      this.total_year = [];
      if (this.BasicInfo.GDPData.year.length != 0) {
        this.BasicInfo.GDPData.year = [];
      }
      if (this.BasicInfo.GDPData.gdp.length != 0) {
        this.BasicInfo.GDPData.gdp = [];
      }
      if (this.BasicInfo.GDP_First_Industry.year.length != 0) {
        this.BasicInfo.GDP_First_Industry.year = [];
      }
      if (this.BasicInfo.GDP_First_Industry.gdp.length != 0) {
        this.BasicInfo.GDP_First_Industry.gdp = [];
      }
      if (this.BasicInfo.GDP_Second_Industry.year.length != 0) {
        this.BasicInfo.GDP_Second_Industry.year = [];
      }
      if (this.BasicInfo.GDP_Second_Industry.gdp.length != 0) {
        this.BasicInfo.GDP_Second_Industry.gdp = [];
      }
      if (this.BasicInfo.GDP_Third_Industry.year.length != 0) {
        this.BasicInfo.GDP_Third_Industry.year = [];
      }
      if (this.BasicInfo.GDP_Third_Industry.gdp.length != 0) {
        this.BasicInfo.GDP_Third_Industry.gdp = [];
      }
      let data = {};
      data["district"] = place;
      filtereconomydistrict(data).then((res) => {
        if (res.code === 20000) {
          let result = res.data;
          result.sort(function (a, b) {
            return parseInt(a.year) > parseInt(b.year) ? 1 : -1;
          });
          for (let i = 0; i < result.length; i++) {
            if (!that.isInArray(that.total_year, result[i]["year"])) {
              that.total_year.push(result[i]["year"]);
            }
            that.BasicInfo.GDPData.year.push(parseFloat(result[i]["year"]));
            that.BasicInfo.GDPData.gdp.push(parseFloat(result[i]["gdp"]));
            that.BasicInfo.GDPData.district = that.district_choose;
            that.BasicInfo.GDP_First_Industry.year.push(
              parseFloat(result[i]["year"])
            );
            that.BasicInfo.GDP_First_Industry.gdp.push(
              parseFloat(result[i]["gdp_first_industry"])
            );
            that.BasicInfo.GDP_First_Industry.district = that.district_choose;
            that.BasicInfo.GDP_Second_Industry.year.push(
              parseFloat(result[i]["year"])
            );
            that.BasicInfo.GDP_Second_Industry.gdp.push(
              parseFloat(result[i]["gdp_second_industry"])
            );
            that.BasicInfo.GDP_Second_Industry.district = that.district_choose;
            that.BasicInfo.GDP_Third_Industry.year.push(
              parseFloat(result[i]["year"])
            );
            that.BasicInfo.GDP_Third_Industry.gdp.push(
              parseFloat(result[i]["gdp_third_industry"])
            );
            that.BasicInfo.GDP_Third_Industry.district = that.district_choose;
          }
        }
      });
    },
    getPieData: function () {
      let that = this;
      let year = this.choose_year_two;
      let district = this.district_choose_two;
      let data = {};
      if (this.PieInfo.data.length != 0) {
        this.PieInfo.data = [];
      }
      data["district"] = district;
      data["year"] = year;
      filterpieeconomydistrict(data).then((res) => {
        if (res.code === 20000) {
          let result = res.data[0];
          that.PieInfo.data.push({
            value: parseFloat(result["gdp_first_industry"]),
            name: "第一产业",
          });
          that.PieInfo.data.push({
            value: parseFloat(result["gdp_second_industry"]),
            name: "第二产业",
          });
          that.PieInfo.data.push({
            value: parseFloat(result["gdp_third_industry"]),
            name: "第三产业",
          });
          that.PieInfo.district = result["district"];
          that.PieInfo.year = result["year"];
        }
      });
    },
    getData: function () {
      let that = this;
      geteconomydistrict().then((res) => {
        if (res.code === 20000) {
          let result = res.data;
          for (let i = 0; i < result.length; i++) {
            if (!that.isInArray(that.total_year, result[i]["year"])) {
              that.total_year.push(result[i]["year"]);
            }
          }
        }
      });
    },
    getBarData: function () {
      let that = this;
      if (this.BarInfo.district.length != 0) {
        this.BarInfo.district = [];
      }
      if (this.BarInfo.gdp.length != 0) {
        this.BarInfo.gdp = [];
      }
      if (this.BarInfo.gdp_first_industry.length != 0) {
        this.BarInfo.gdp_first_industry = [];
      }
      if (this.BarInfo.gdp_second_industry.length != 0) {
        this.BarInfo.gdp_second_industry = [];
      }
      if (this.BarInfo.gdp_third_industry.length != 0) {
        this.BarInfo.gdp_third_industry = [];
      }
      let data = {};
      data["year"] = this.choose_year_one;
      filterbareconomydistrict(data).then((res) => {
        if (res.code === 20000) {
          let result = res.data;
          for (let i = 0; i < result.length; i++) {
            that.BarInfo.district.push(result[i]["district"]);
            that.BarInfo.gdp.push(parseFloat(result[i]["gdp"]));
            that.BarInfo.gdp_first_industry.push(
              parseFloat(result[i]["gdp_first_industry"])
            );
            that.BarInfo.gdp_second_industry.push(
              parseFloat(result[i]["gdp_second_industry"])
            );
            that.BarInfo.gdp_third_industry.push(
              parseFloat(result[i]["gdp_third_industry"])
            );
          }
        }
      });
    },
  },
  mounted() {
    this.getGDPData(this.district_choose);
    this.getPieData();
    this.getData();
    this.getBarData();
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
.chart-wrapper {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
  margin-top: 20px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
.divider {
  width: 100%;
  height: 2px;
  background: #5c95d6;
}
</style>
