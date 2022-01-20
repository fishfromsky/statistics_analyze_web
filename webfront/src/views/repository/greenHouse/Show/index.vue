<template>
  <div class="dashboard-container">
    <el-row :gutter="0">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <shemid
            :chart-data="BasicInfo.emission"
            datastyle="height: 100vh"
          ></shemid>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <shemio datastyle="height: 100vh"></shemio>
        </div>
      </el-col>
    </el-row>
    <input @change="getUploadFile" type="file" class="inputDevice" />
  </div>
</template>

<script>
import XLSX from 'xlsx'
import { mapGetters } from 'vuex'
import { getcityeconomydata } from '@/api/model'
import emission from './components/emission'
import emissionOut from './components/emissionOut'
import { parse } from 'path-to-regexp'
import shemid from './components/SHEmiD.vue'
import shemio from './components/SHEmiO.vue'

export default {
  name: "index",
  components: {
    emission,
    emissionOut,
    shemid,
    shemio,
  },
  data() {
    return {
      BasicInfo: {

        emission: {
          burndata: {},
          biosdata: {},
          burydata: {},
          totaldata: {},
        }
      }
    }
  },
  methods: {
    getUploadFile(e) {
      console.log('数据改变', e);
      let fileName = e.target.files[0]
      let reader = new FileReader();
      reader.readAsBinaryString(fileName)
      //onload在文件被读取时自动触发
      reader.onload = (e) => {
        let workbook = XLSX.read(e.target.result, { type: 'binary' })
        console.log(workbook);
        let startData = workbook.Sheets
        let sheetList = workbook.SheetNames
        //存放json数组格式的表格数据
        sheetList.forEach(item => {
          let worksheet = workbook.Sheets[item]
          let json = XLSX.utils.sheet_to_json(workbook.Sheets[item])
          this.resultJson = json
        });
        console.log("resultJson", this.resultJson);
        var b = {};
        var bur = {};
        var bio = {};
        var total = {};
        var offsetCO2 = {};
        for (var item of this.resultJson) {
          print(item);
          for (var key in item) {
            
            //填埋排放

            //CO2抵消
            if (key == 'e15' || key == 'e19' || key == 'e20') {
              if (offsetCO2[item['a2_sjtu_year']])
                offsetCO2[item['a2_sjtu_year']] += item[key]
              else offsetCO2[item['a2_sjtu_year']] = item[key]
            }
            //CH4抵消
            if (key == 'e11' || key == 'e16' || key == 'e18') {
              if (bio[item['a2_sjtu_year']])
                bio[item['a2_sjtu_year']] += item[key]
              else bio[item['a2_sjtu_year']] = item[key]
            }
            //N2O
            if (key == 'e13' || key == 'e17') {
              if (b[item['a2_sjtu_year']])
                b[item['a2_sjtu_year']] += item[key]
              else b[item['a2_sjtu_year']] = item[key]
            }

          }
        }
        for (var item in bio) {
          bio[item] = Number(bio[item] * 25).toFixed(3)
        }
        for (var item in b) {
          b[item] = Number(b[item] * 298).toFixed(3)
        }
        this.burydata = b
        this.biosdata = bio
        this.burndata = bur
        this.totaldata = total
        console.log("填埋排放", this.burydata)
        console.log("CH4", this.biosdata)
        console.log("CO2", this.burndata)
        console.log("totaldata", this.totaldata)
        console.log("offsetCO2", offsetCO2)

      }
    },


  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  mounted() {
    let that = this;
  }
}
</script>

<style scoped lang="scss">
.dashboard {
  &-container {
    width: 100%;
    height: 100vh;
    background-color: rgb(8, 15, 62);
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.chart-wrapper {
  background: rgb(8, 15, 62);
   width: 90%;
    border: 3px solid #185FAE;
    border-radius:10px;
    box-sizing: border-box;
    position: relative;
    box-shadow: -8px 0px 10px #034c6a inset,
    8px 0px 10px #034c6a inset;
    height: 100%;
    margin: 60px auto;

}

</style>
