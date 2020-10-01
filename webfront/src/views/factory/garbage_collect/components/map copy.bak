<template>
    <div>
        <div ref="map" class="map-container"></div>
        <div class="control-panel">
            <div class="button-list">
                <span>是否显示标签：</span>
                <el-select v-model="district" placeholder="请选择">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
            </div>
        </div>
    </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/extension/bmap/bmap'
import { getcollectfactorybyarea } from '@/api/model'
export default {
    data(){
        return {
            chart: echarts.ECharts,
            data: [],
            geoCoordMap: {},
            district: '',
            options: [
                {
                    value: '1',
                    label: '宝山区'
                }, 
            ],
        }
    },
    methods: {
        getData(){
            var that = this
        }
    }
}
</script>

<style lang="less" scoped>
    .map-container{
        position: relative;
        z-index: 10;
        width: 100%;
        height: 95vh;
    }
    .control-panel{
        width: 250px;
        height: 60px;
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 100
    }
    .button-list{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    .button-list span{
        font-size: 15px;
        color: #fff;
    }
</style>