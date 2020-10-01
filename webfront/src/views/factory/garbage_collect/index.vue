<template>
  <div class="dashboard-container">
    <el-row>
      <el-col :xs="24" :sm="24" :lg="24">
        <div class="chart-wrapper">
          <!-- 放置mymap并将Data传入 -->
          <mymap :chart-data="Data" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Location from './components/mapdata/location_data.json' // 读取要标记的垃圾收集点
import mymap from './components/map'
export default {
  name: 'Index',
  components: {
    mymap
  },
  data() {
    return {
      Data: Location // 将location传给Data
    }
  }
}
</script>

// <style lang="less" scoped>
// .dashboard {
//   &-container {
//     margin: 30px;
//   }
//   &-text {
//     font-size: 30px;
//     line-height: 46px;
//   }
// }
// .map-wrapper {
//   width: 100%;
// //   height: 100%;
//   margin: 0 auto;
//   background: #fff;
//   padding: 0;
//   box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
// }
// </style>
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
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
</style>
