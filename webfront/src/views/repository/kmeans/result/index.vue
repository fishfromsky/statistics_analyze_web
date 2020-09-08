<template>
  <div>
    <div class="main-content">
      <span>项目编号：</span>
      <el-select placeholder="项目编号" v-model="project_id" class="project_id" style="width: 120px">
        <el-option v-for="item in id_list" :key="item.project_id" :label="item.project_id" :value="item.project_id"></el-option>
      </el-select>
      <div class="divider"></div>
      <el-button type="primary" icon="el-icon-download"  @click="handleDownload" style="margin-left:20px">下载数据</el-button>
      <div class="divider"></div>
      <el-select placeholder="选择实验编号" v-model="sort_id" style="margin-left: 20px">
        <el-option v-for="item in sort_list" :key="item.label" :label="item.label" :value="item.value"></el-option>
      </el-select>
      <el-button type="primary" icon="el-icon-data-line" style="margin-left: 20px" @click="showGraph">数据可视化</el-button>     
    </div>
    <div class="table-container">
      <result :projectId="project_id" ref="result" @child-event="handleChildEvent"></result>
    </div>
  </div>
</template>

<script>
import { getidlistkmeans } from '@/api/model'
import result from './components/result.vue'
export default {
  components: {
    result
  },
  data(){
    return{
      project_id: '',
      sort_id: null,
      id_list: [],
      sort_list: []
    }
  },
  methods:{
    init_projectId:function(){
      let that = this
      getidlistkmeans().then(res=>{
        let data = res.data
        for (let i=0; i<data.length; i++){
            that.id_list.push(data[i])
        }
      })
    },
    handleDownload:function(){
      this.$refs.result.download()
    },
    handleChildEvent:function(val){
      this.sort_list = []
      for (let i=0; i<val.length; i++){
        let dict = {}
        dict['value'] = val[i]
        dict['label'] = val[i]
        this.sort_list.push(dict)
      }
    },
    showGraph:function(){
      if (this.sort_id === null){
        this.$message.error('请选择实验编号')
      }
      else{
        this.$refs.result.showChart(this.sort_id)
      }
    }
  },
  mounted(){
    this.init_projectId()
  }
}
</script>

<style scoped>
  .main-content{
    width: 95%;
    height: 80px;
    margin: 0 auto;
    margin-top: 20px;
    background: #fff;
    box-shadow: 0 0 10px 10px rgba(153, 153, 153, 0.1);
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .main-content span{
    margin-left: 20px;
    color: #333;
  }
  .project_id{
    margin-left: 20px;
  }
  .table-container{
    width: 95%;
    margin: 0 auto;
  }
  .divider{
    width: 0;
    height: 40px;
    border-left: #ccc solid 1px;
    margin-left: 20px;
  }
</style>>
