<template>
  <div>
      <div class="column_list">
          <el-select placeholder="项目编号" v-model="project_id" class="project_id">
              <el-option v-for="item in id_list" :key="item.project_id" :label="item.project_id" :value="item.project_id"></el-option>
          </el-select>
          <el-button type="primary" @click="get_data" icon="el-icon-search" class="search-btn">搜索数据</el-button>
          <div class="divider"></div>
          <el-button type="primary" @click="input_data" icon="el-icon-upload2" class="input-btn">上传数据</el-button>
          <div class="divider"></div>
          <el-button type="primary" @click="download_data" icon="el-icon-download" style="margin-left: 20px">下载数据</el-button>
      </div>
  </div>
</template>

<script>
import { getidrelation } from '@/api/model'
import da from 'element-ui/src/locale/lang/da'
export default {
    data(){
        return {
            project_id: '',
            id_list: []
        }
    },
    methods: {
        get_project_id:function(){
            var that = this
            getidrelation().then(res=>{
                let data = res.data
                for (let i=0; i<data.length; i++){
                    that.id_list.push(data[i])
                }
            })
        },
        get_data:function(){
            this.$emit('id-event', this.project_id)
        },
        input_data(){
            this.$emit('child-event', 'true')
        },
        download_data(){
            this.$emit('download-event', 'true')
        }
    },
    mounted(){
        this.get_project_id()
    }
}
</script>

<style>
    .column_list{
        width: 95%;
        height: 80px;
        background: #fff;
        margin: 0 auto;
        margin-top: 20px;
        box-shadow: 0 0 10px 10px rgba(153, 153, 153, 0.1);
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .project_id{
        width: 150px;
        height: 30px;
        margin-left: 20px;
        margin-top: -8px;
    }
    .search-btn{
        margin-left: 20px;
    }
    .input-btn{
        margin-left: 20px;
    }
    .divider{
        width: 0;
        height: 40px;
        border-left: 1px solid #ccc;
        margin-left: 20px;
    }
</style>