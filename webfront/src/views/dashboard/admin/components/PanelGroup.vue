<template>
    <el-row :gutter="40" class="panel-group">
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-card">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-people">
            <svg-icon icon-class="peoples" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              今日访问数量
            </div>
            <count-to :start-val="0" :end-val="632" :duration="2600" class="card-panel-num" />
          </div>
        </div>
      </el-col>
      <!-- <el-col :xs="12" :sm="12" :lg="6" class="card-panel-card">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-eye">
            <svg-icon icon-class="eye-open" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              今日实验人数
            </div>
            <count-to :start-val="0" :end-val="128" :duration="2600" class="card-panel-num" />
          </div>
        </div>
      </el-col> -->
     
      <!-- <el-col :xs="12" :sm="12" :lg="6" class="card-panel-card">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-count">
            <svg-icon icon-class="shopping" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              今日模型使用个数
            </div>
            <count-to :start-val="0" :end-val="9" :duration="2600" class="card-panel-num" />
          </div>
        </div>
      </el-col> -->
    </el-row>
</template>

<script>
import CountTo from 'vue-count-to'
export default {
  name: 'PanelGroup',
  components:{
    CountTo
  }
}
</script>

<style lang="scss" scoped>
  .panel-group{
    margin-top: 18px;

  }
  .card-panel-col{
    margin-bottom: 32px;
  }
  .card-panel{
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
   // background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);

    &:hover{
      .card-panel-icon-wrapper{
        color: #fff;
      
      }
      .card-panel-num {
        font-size: 20px;
        color:#fff
      }
      .icon-people{
        background: #40c9c6;
      }
      .icon-eye {
        background: #36a3f7;
      }
      .icon-use{
        background: #f4516c;
      }
      .icon-count{
        background: #67C23A;
      }
      .card-panel-text{
        line-height: 18px;
        color: rgb(72, 202, 46);
        font-size: 16px;
        margin-bottom: 12px;
      }
    }

    .icon-people {
      color: #40c9c6;
    }

    .icon-eye{
      color: #36a3f7;
    }

    .icon-use{
      color: #f4516c;
    }
    .icon-count{
      color: #67C23A;
    }

    .card-panel-icon-wrapper {
    float: left;
    margin: 14px 0 0 14px;
    padding: 16px;
    transition: all 0.38s ease-out;
    width: 80px;
    height:80px;
    border: 1px solid #2b92d4;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    overflow: hidden;
    animation-timing-function: ease-in-out;
    animation-name: breathe;
    animation-duration: 1500ms;
    animation-iteration-count: infinite;
    animation-direction: alternate;
    }
@keyframes breathe {
    0% {
        opacity: .4;
        box-shadow: 0 1px 2px rgba(0, 147, 223, 0.4), 0 1px 1px rgba(0, 147, 223, 0.1) inset;
    }

    100% {
        opacity: 1;
        border: 1px solid rgba(59, 235, 235, 0.7);
        box-shadow: 0 1px 15px #0093df, 0 1px 10px #0093df inset;
    }
}
    .card-panel-icon {
      float: left;
      font-size: 48px;
    }
    .card-panel-description{
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        cursor: pointer;
        line-height: 18px;
        color: 	#1E90FF;
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }
  }
</style>
