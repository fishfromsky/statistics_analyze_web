<template>
  <div class="production-container">
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :xs="24" :sm="240" :lg="2000">
        <el-row>
          <el-col :xs="24" :sm="240" :lg="2000">
            <div class="chart-wrapper">
              <production :chart-data="production_data.production" style="height: 70vh ;width:200vh"></production>
            </div>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import production from './components/production'
import {getcitygarbageproductiondata} from '@/api/model'

export default {
  name: 'index',
  components: {
    production
  },
  data() {
    return {
      production_data: {
        production: {
          data: [],
          year: []
        }
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
    getcitygarbageproductiondata().then(res => {
      if (res.code === 20000) {
        console.log("res.data:",res)
        console.log("res.data:",res)
        let result = res.data
        result.sort(function(a, b) {
          return parseInt(a.year) > parseInt(b.year) ? 1 : -1
        })
        for (let i = 0; i < result.length; i++) {
          that.production_data.production.data.push(Math.round(parseFloat(result[i]['production'])*47.20498)/100)
          that.production_data.production.year.push(result[i]['year'])
        }
      }
    })
  }
}
</script>

<style scoped>
.production-container {
  width: 95%;
  margin: 0 auto;
}

.chart-wrapper {
  background: #fff;
  padding: 16px 16px 0;
  margin-bottom: 32px;
  box-shadow: 0 0 10px 5px rgba(153, 153, 153, 0.1);
}
</style>
