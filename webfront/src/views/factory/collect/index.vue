<template>
    <div class="map_container">
        <el-row>
        <el-col :xs="24" :sm="24" :lg="24">
            <div class="map-wrapper">
                <mymap></mymap>
            </div>
        </el-col>
        </el-row>
    </div>
</template>

<script>
import mymap from './components/map'
export default {
    name: 'index',
    components: {
        mymap
    }
}
</script>

<style lang="less" scoped>
    .dashboard {
        &-container {
        margin: 30px;
        }
        &-text {
        font-size: 30px;
        line-height: 46px;
        }
    }
    .map-wrapper{
        width: 100%;
        margin: 0 auto;
        background: #fff;
        padding: 0;
        box-shadow: 0 0 10px 5px rgba(153,153,153,0.1);
    }
</style>