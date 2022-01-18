<template>
  <div class="dashboard-container">
    <div>选择地区</div>
    <input v-model="districts" type="checkbox" value="黄浦区">黄浦区
    <input v-model="districts" type="checkbox" value="徐汇区">徐汇区
    <input v-model="districts" type="checkbox" value="长宁区">长宁区
    <input v-model="districts" type="checkbox" value="静安区">静安区
    <input v-model="districts" type="checkbox" value="普陀区">普陀区
    <input v-model="districts" type="checkbox" value="虹口区">虹口区
    <input v-model="districts" type="checkbox" value="杨浦区">杨浦区
    <input v-model="districts" type="checkbox" value="闵行区">闵行区
    <input v-model="districts" type="checkbox" value="宝山区">宝山区
    <input v-model="districts" type="checkbox" value="嘉定区">嘉定区
    <input v-model="districts" type="checkbox" value="浦东新区">浦东新区
    <input v-model="districts" type="checkbox" value="金山区">金山区
    <input v-model="districts" type="checkbox" value="松江区">松江区
    <input v-model="districts" type="checkbox" value="青浦区">青浦区
    <input v-model="districts" type="checkbox" value="奉贤区">奉贤区
    <input v-model="districts" type="checkbox" value="崇明区">崇明区
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
import mymap from './components/map'
import { getcollectfactorybyarea } from '@/api/model'

export default {
  name: 'Index',
  components: {
    mymap
  },
  data() {
    return {
      districts: [],
      Data: []
    }
  },

  watch: {
    districts(val) {
      this.getdata(val)
    }
  },

  methods: {
    getdata(district) {
      console.log(district)
      this.Data = []
      var that = this
      getcollectfactorybyarea({ 'district': JSON.stringify(district) }).then(res => {
        if (res.code === 20000) {
          const result = res.data
          for (let i = 0; i < result.length; i++) {
            that.Data.push(
              {
                'name': result[i]['address'],
                'value': [
                  result[i]['longitude'],
                  parseFloat(result[i]['latitude'])
                ]
              }
            )
          }
        }
      }
      )
    }
  }
}

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
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
</style>
