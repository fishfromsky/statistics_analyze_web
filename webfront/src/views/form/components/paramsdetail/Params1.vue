<template>
    <div class="container">
      <div class="title">模型参数调整控制面板</div>
        <div class="time-choose">
          <span class="span-title">日期选择：</span>
          <el-select clearable class="option-box" placeholder="选择数据日期" v-model="time">
            <el-option v-for="item in time_option" :value="item" :label="item" :key="item"></el-option>
          </el-select>
        </div>
        <div class="channel-choose">
          <span class="span-title">指标选择：</span>
          <el-input type="text" class="channel-input" v-model="channel" placeholder="输入评价指标"></el-input>
        </div>
        <div class="value-choose">
          <span class="span-title">参数调整：</span>
          <el-input type="number" class="channel-input" v-model="number" placeholder="输入参数值"></el-input>
        </div>
        <div class="btn-list">
          <el-button type="primary" class="btn" @click="handleClick">开始测试</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Params1",
        data(){
            return{
                time:'',
                time_option:['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday'],
                channel:'',
                number:'',
            }
        },
        methods:{
          getIndex:function(arr,item){
              for(let i=0; i<arr.length; i++){
                  if(arr[i] === item){
                    return i;
                  }
              }
          },
          handleClick:function () {
            if (this.time === ''){
              this.$message.error('日期输入不能为空')
            }
            else if (this.channel === ''){
              this.$message.error('指标选择不能为空')
            }
            else if ((this.channel.length !== 2 && this.channel.length !== 3) ||
              (this.channel[this.channel.length-1] !== 'p' && this.channel[this.channel.length-1] !== 'a')){
              this.$message.error('输入正确指标')
            }
            else if (this.number === ''){
              this.$message.error('参数值不能为空')
            }
            else{
              let y;
              let x = this.getIndex(this.time_option, this.time);
              if (this.channel[this.channel.length-1] === 'a'){
                y = parseInt(this.channel.slice(0, this.channel.length-1))%12;
              }
              let z = parseInt(this.number);
              let data = [x, y, z];
              this.$emit('event1', data)
            }
          }
        }
    }
</script>

<style scoped>
   .title{
    font-size: 20px;
    color: #666;
    font-weight: bold;
    letter-spacing: 2px;
    margin-left: 10px;
  }
  .time-choose{
    margin-top: 32px;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 32px;
  }
  .span-title{
    font-size: 15px;
    font-weight: bold;
    color: #333;
    margin-left: 10px;
  }
  .option-box{
    float: left;
    margin-left: 20px;
  }
  .channel-choose{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 32px;
  }
  .channel-input{
    width: 200px;
    float: left;
    margin-left: 20px;
  }
  .value-choose{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 32px;
  }
  .btn-list{
    margin-bottom: 32px;
    width: 100%;
    height: 60px;
  }
  .btn{
    float: right;
    margin-right: 30px;
  }
</style>
