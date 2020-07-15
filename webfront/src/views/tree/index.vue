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
        <el-button type="primary" icon="el-icon-download" class="input-item">导出数据</el-button>
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
    </div>
  </div>
</template>

<script>
import cityeconomy from './components/cityeconomy'
import citypopulation from './components/citypopulation'
import citygarbage from './components/citygarbage'
import citygarbagedeal from './components/citygarbagedeal'
import citygarbagecapacity from './components/citygarbagecapacity'
import citygarbagevolume from './components/citygarbagevolume'
import factorylist from './components/factorylist'
import transfer from './components/transfer'
export default {
  components: {
    cityeconomy,
    citypopulation,
    citygarbage,
    citygarbagedeal,
    citygarbagecapacity,
    citygarbagevolume,
    factorylist,
    transfer
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
        }
      ],
    }
  },
  watch: {

  },
  methods: {
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

