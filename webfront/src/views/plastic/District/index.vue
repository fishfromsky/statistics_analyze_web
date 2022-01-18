<template>
  <div class="population-container">
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper1">
          <population_-map :chart-data="population_data.density" style="height: 100vh"></population_-map>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import Population_Map from "./components/Population_Map";

export default {
  name: "index",
  components: {
    Population_Map
  },
  data() {
    return {
      population_data: {
        density: [
          {name: '黄浦区', value: 1385.78},
          {name: '徐汇区', value: 3426.28},
          {name: '长宁区', value: 2225.08},
          {name: '静安区', value: 2416.28},
          {name: '普陀区', value: 3651.67},
          {name: '虹口区', value: 2057},
          {name: '杨浦区', value: 3435.05},
          {name: '浦东新区', value: 12866.79},
          {name: '闵行区', value: 5728.23},
          {name: '宝山区', value: 4951.58},
          {name: '嘉定区', value: 3699.51},
          {name: '金山区', value: 1844.28},
          {name: '松江区', value: 4282.26},
          {name: '青浦区', value: 2764.28},
          {name: '奉贤区', value: 2859.65},
          {name: '崇明区', value: 1742.17}

        ]
      }
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  mounted() {
    var that = this
  }
}
</script>

<style scoped>
.population-container {
  width: 95%;
  margin: 0 auto;
}

.chart-wrapper1 {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}

.chart-wrapper {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
</style>
