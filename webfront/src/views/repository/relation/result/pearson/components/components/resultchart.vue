<template>
  <div :class="className" :style="{ width: width, height: height }"></div>
</template>

<script>
import echarts from "echarts";
require("echarts/theme/westeros"); // echarts theme
import resize from "./mixins/resize";
export default {
  name: "pearson",
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: "chart",
    },
    width: {
      type: String,
      default: "100%",
    },
    height: {
      type: String,
      default: "250px",
    },
    autoResize: {
      type: Boolean,
      default: true,
    },
    chartData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      chart: null,
    };
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val);
      },
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart();
    });
  },
  beforeDestroy() {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, "westeros");
      this.setOptions(this.chartData);
    },
    setOptions(val) {
      var value = val.relate;
      var label = val.label;
      this.chart.setOption({
        title: {
          text: "皮尔逊相关系数排序",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            crossStyle: {
              color: "#999",
            },
          },
        },
        toolbox: {
          feature: {
            saveAsImage: { show: true },
          },
        },
        xAxis: [
          {
            type: "category",
            data: label,
            axisPointer: {
              type: "shadow",
            },
            axisLabel: {
              //坐标轴刻度标签的相关设置。
              interval: 0,
              rotate: "20",
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "重要指数",
            axisLabel: {
              formatter: "{value}",
            },
          },
        ],
        series: [
          {
            type: "bar",
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: "#83bff6" },
                { offset: 0.5, color: "#188df0" },
                { offset: 1, color: "#188df0" },
              ]),
            },
            emphasis: {
              itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "#2378f7" },
                  { offset: 0.7, color: "#2378f7" },
                  { offset: 1, color: "#83bff6" },
                ]),
              },
            },
            data: value,
          },
        ],
      });
    },
  },
};
</script>

<style scoped>
</style>
