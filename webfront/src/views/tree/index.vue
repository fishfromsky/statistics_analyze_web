<template>
  <div class="app-container">
    <div class="main-content">
      <div class="input-content">
        <el-select v-model="level" placeholder="请选择数据级别" class="input-item">
          <el-option v-for="item in level_option"  :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <el-select v-model="kind" placeholder="请选择数据表类型" class="input-item">
          <el-option v-for="item in kind_option" :key="item.value" :label="item.label" :value="item.value">
          </el-option>
        </el-select>
        <div class="divider"></div>
        <el-button type="primary" icon="el-icon-download" @click="Download" class="input-item">导出数据</el-button>
        <el-button  type="info" icon="el-icon-upload2" @click="addData" style="text-align: center" plain>添加数据</el-button>
      </div>
      <cityeconomy v-if="level == '1' && kind == '1'" ref="economy"></cityeconomy>
      <citypopulation v-if="level == '1' && kind == '2'" ref="population"></citypopulation>
      <citygarbage v-if="level == '1' && kind == '3'" ref="garbage"></citygarbage>
      <citygarbagedeal v-if="level == '1' && kind == '4'" ref="deal"></citygarbagedeal>
      <citygarbagecapacity v-if="level == '1' && kind == '5'" ref="capacity"></citygarbagecapacity>
      <citygarbagevolume v-if="level == '1' && kind == '6'" ref="volume"></citygarbagevolume>
      <factorylist v-if="level == '1' && kind == '7'" ref="factorylist"></factorylist>
      <transfer v-if="level == '1' && kind == '8'" ref="transfer"></transfer>
      <garbageelement v-if="level=='1' && kind == '9'" ref="garbageelement"></garbageelement>
      <dangerous v-if="level=='1' && kind == '10'" ref="dangerous"></dangerous>
      <garbageclearperday v-if="level=='1' && kind=='11'" ref="garbageclear"></garbageclearperday>
      <countrygarbage v-if="level=='3' && kind=='12'" ref="countrygarbage"></countrygarbage>
      <economydistrict v-if="level=='2' && kind=='1'" ref="districteconomy"></economydistrict>
      <populationdistrict v-if="level=='2' && kind=='2'" ref="districtpopulation"></populationdistrict>
    </div>
  </div>
</template>

<script>
import cityeconomy from './components/city/cityeconomy'
import citypopulation from './components/city/citypopulation'
import citygarbage from './components/city/citygarbage'
import citygarbagedeal from './components/city/citygarbagedeal'
import citygarbagecapacity from './components/city/citygarbagecapacity'
import citygarbagevolume from './components/city/citygarbagevolume'
import factorylist from './components/factorylist'
import transfer from './components/transfer'
import garbageelement from './components/garbageelement'
import dangerous from './components/dangerousgarbage'
import garbageclearperday from './components/garbageclearperday'
import countrygarbage from './components/countrygarbage'
import economydistrict from './components/district/districteconomy'
import populationdistrict from './components/district/districtpopulation'
export default {
  components: {
    cityeconomy,
    citypopulation,
    citygarbage,
    citygarbagedeal,
    citygarbagecapacity,
    citygarbagevolume,
    factorylist,
    transfer,
    garbageelement,
    dangerous,
    garbageclearperday,
    countrygarbage,
    economydistrict,
    populationdistrict
  },
  data() {
    return {
      level: '',
      kind: '',
      adddata_dialog: false,
      level_option: [
        {
          value: '1',
          label: '市级'
        },
        {
            value: '2',
            label: '区级'
        },
        {
            value: '3',
            label: '乡级'
        }
      ],
      kind_option: [
        {
          value: '1',
          label: '经济数据'
        },
        {
          value: '2',
          label: '人口数据'
        },
        {
          value: '3',
          label: '生活垃圾处理'
        },
        {
          value: '4',
          label: '无害化处理厂数量'
        },
        {
          value: '5',
          label: '无害化处理能力'
        },
        {
          value: '6',
          label: '无害化处理量'
        },
        {
          value: '7',
          label: '无害化处理厂信息'
        },
        {
          value: '8',
          label: '垃圾中转站信息'
        },
        {
          value: '9',
          label: '固废成分表'
        },
        {
          value: '10',
          label: '危险垃圾处置表'
        },
        {
          value: '11',
          label: '日均清运量'
        },
        {
          value: '12',
          label: '乡镇垃圾产量表'
        }
      ],
    }
  },
  watch: {

  },
  methods: {
    Download:function(){
      if (this.level === ''){
        this.$message.error('数据级别不能为空')
      }
      else if (this.kind === ''){
        this.$message.error('数据表类型不能为空')
      }
      else{
        if (this.level === '1' && this.kind === '1'){
          this.$refs.economy.DownLoad()
        }
        else if (this.level === '1' && this.kind === '2'){
          this.$refs.population.DownLoad()
        }
        else if (this.level === '1' && this.kind === '3'){
          this.$refs.garbage.DownLoad()
        }
        else if (this.level === '1' && this.kind === '4'){
          this.$refs.deal.DownLoad()
        }
        else if (this.level === '1' && this.kind === '5'){
          this.$refs.capacity.DownLoad()
        }
        else if (this.level === '1' && this.kind === '6'){
          this.$refs.volume.DownLoad()
        }
        else if (this.level === '1' && this.kind === '7'){
          this.$refs.factorylist.DownLoad()
        }
        else if (this.level === '1' && this.kind === '8'){
          this.$refs.transfer.DownLoad()
        }
        else if (this.level === '1' && this.kind === '9'){
          this.$refs.garbageelement.DownLoad()
        }
        else if (this.level === '1' && this.kind === '10'){
          this.$refs.dangerous.DownLoad()
        }
        else if (this.level === '1' && this.kind === '11'){
          this.$refs.garbageclear.DownLoad()
        }
        else if (this.level === '3' && this.kind === '12'){
          this.$refs.countrygarbage.DownLoad()
        }
        else if (this.level === '2' && this.kind === '1'){
          this.$refs.districteconomy.DownLoad()
        }
        else if (this.level === '2' && this.kind === '2'){
          this.$refs.districtpopulation.DownLoad()
        }
      }
    },
    addData() {
      var that = this
      if (that.level === '') {
        that.$message.error('数据级别不能为空')
      } else if (that.kind === '') {
        that.$message.error('数据表类型不能为空')
      } else {
        if (that.level === '1' && that.kind === '1') {
          this.$refs.economy.addData()
        } else if (that.level === '1' && that.kind === '2') {
          this.$refs.population.addData()
        } else if (that.level === '1' && that.kind === '3') {
          this.$refs.garbage.addData()
        } else if (that.level === '1' && that.kind === '4') {
          this.$refs.deal.addData()
        } else if (that.level === '1' && that.kind === '5') {
          this.$refs.capacity.addData()
        } else if (that.level === '1' && that.kind === '6') {
          this.$refs.volume.addData()
        }else if (that.level === '1' && that.kind === '7'){
          this.$refs.factorylist.addData()
        }else if (that.level === '1' && that.kind === '8'){
          this.$refs.transfer.addData()
        }else if (that.level === '1' && that.kind === '9'){
          this.$refs.garbageelement.addData()
        }else if (that.level === '1' && that.kind === '10'){
          this.$refs.dangerous.addData()
        }else if (that.level === '1' && that.kind === '11'){
          this.$refs.garbageclear.addData()
        }else if (that.level === '3' && that.kind === '12'){
          this.$refs.countrygarbage.addData()
        }else if (that.level === '2' && that.kind === '1'){
          this.$refs.districteconomy.addData()
        }else if (that.level === '2' && that.kind === '2'){
          this.$refs.districtpopulation.addData()
        }
      }
    }
  
  },
  mounted() {
   
  }
}
</script>
<style scoped>
  .main-content{
    position: relative;
    width: 98%;
    min-height: 100px;
    background: #fff;
    box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    margin: 0 auto;
    padding: 10px 10px;
  }
  .input-content{
    height: 40px;
    margin-top: 20px;
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center; 
  }
  .input-item{
    float: left;
    margin-left: 20px;
  }
  .divider{
    width: 0;
    height: 30px;
    border-left: #aaa 1px solid;
    margin-left: 35px;
  }
</style>

