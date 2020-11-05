<template>
    <div>
        <div class="select-box">
            <el-input type="number" placeholder="输入p值" v-model="selectP"></el-input>
            <el-input placeholder="输入集散厂" v-model="selectRRC" style="margin-top: 20px"></el-input>
            <el-button class="confirm-btn" @click="selectConfirm">确定</el-button>
        </div>
        <div id="map" style="width: 100%; height: 95vh"></div>
    </div>
</template>

<script>
import echarts from 'echarts'
import shanghai from './mapdata/shanghai.json'
echarts.registerMap('shanghai', shanghai)
import { fetchall_list } from '@/api/app01/utputallocation'
export default {
    data(){
        return{
            project_id: 'p001',
            chinaGeoCoordMap: {},
            chinaDatas: [],
            series: [],
            centrl_geo: [121.477665,31.226048],
            zoom: 1.2,
            selectP: '',
            selectRRC: '',
            chart: null
        }
    },
    computed:{
        option:function(){
            return {
                tooltip: {
                    trigger: 'item',
                    backgroundColor: ' rgba(0, 161, 255, 0.4)',
                    borderColor: '#00faff',
                    showDelay: 0,
                    hideDelay: 0,
                    enterable: true,
                    transitionDuration: 0,
                    extraCssText: 'z-index:100',
                    formatter: function(params, ticket, callback) {
                        //根据业务自己拓展要显示的内容
                        var res = "";
                        if (params.componentSubType === 'effectScatter'){
                            var name = params.data.name;
                            var value = params.data.value[2];
                            res = "<span style='color:#fff;'>" + name + "</span><br/>数据：" + value;
                        }
                        else{
                            var value = params.data.value
                            res = "<span style='color:#fff;'>p值" + value + "</span>"
                        }
                        return res;
                    }
                },
                backgroundColor:"#013954",
                visualMap: { //图例值控制
                    min: 6,
                    max: 27,
                    calculable: true,
                    show: true,
                    color: ['#f44336', '#fc9700', '#ffde00', '#ffde00', '#00eaff'],
                    textStyle: {
                        color: '#fff'
                    }
                },
                geo: {
                    map: 'shanghai',
                    zoom: this.zoom,
                    center: this.centrl_geo,
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    roam: true, //是否允许缩放
                    itemStyle: {
                        normal: {
                            color: 'rgba(51, 69, 89, .5)', //地图背景色
                            borderColor: '#516a89', //省市边界线00fcff 516a89
                            borderWidth: 1
                        },
                        emphasis: {
                            color: 'rgba(37, 43, 61, .5)' //悬浮背景
                        }
                    }
                },
                series: this.series
            }
        }
    },
    methods:{
        controlSeries:function(centrl, centrl_geo){
            let that = this;
            [[centrl, that.chinaDatas]].forEach(function(item, i) {
                that.series.push({
                        type: 'lines',
                        zlevel: 2,
                        effect: {
                            show: true,
                            period: 4, //箭头指向速度，值越小速度越快
                            trailLength: 0.02, //特效尾迹长度[0,1]值越大，尾迹越长重
                            symbol: 'arrow', //箭头图标
                            symbolSize: 5, //图标大小
                        },
                        lineStyle: {
                            normal: {
                                width: 1, //尾迹线条宽度
                                opacity: 1, //尾迹线条透明度
                                curveness: .3 //尾迹线条曲直度
                            }
                        },
                        data: that.convertData(item[1], centrl_geo)
                    }, {
                        type: 'effectScatter',
                        coordinateSystem: 'geo',
                        zlevel: 2,
                        rippleEffect: { //涟漪特效
                            period: 4, //动画时间，值越小速度越快
                            brushType: 'stroke', //波纹绘制方式 stroke, fill
                            scale: 4 //波纹圆环最大限制，值越大波纹越大
                        },
                        label: {
                            normal: {
                                show: true,
                                position: 'right', //显示位置
                                offset: [5, 0], //偏移设置
                                formatter: function(params){//圆环显示文字
                                    return params.data.name;
                                },
                                fontSize: 13
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        symbol: 'circle',
                        symbolSize: function(val) {
                            return 3; //圆环大小
                        },
                        itemStyle: {
                            normal: {
                                show: false,
                                color: '#f00'
                            }
                        },
                        data: item[1].map(function(dataItem) {
                            return {
                                //在这里定义你所要展示的数据
                                name: dataItem[0].name,
                                value: that.chinaGeoCoordMap[dataItem[0].name].concat([dataItem[0].value])
                            };
                        }),
                    },
                );
            });
        },
        selectConfirm:function(){
            this.chinaGeoCoordMap = {}
            this.chinaDatas = []
            this.series = []
            let that = this
            let data = {}
            data['project_id'] = this.project_id
            data['p_value'] = this.selectP
            data['rrc'] = this.selectRRC
            fetchall_list(data).then(res=>{
                if (res.code === 20000){
                    let data = res.data
                    for (let i=0; i<data.length; i++){
                        that.chinaGeoCoordMap[data[i].ts] = [data[i].ts_lng, data[i].ts_lat]
                        that.chinaDatas.push([{name: data[i].ts, value: data[i].p_value}])
                    }
                    that.chinaGeoCoordMap[data[0].rrc] = [data[0].rrc_lng, data[0].rrc_lat]
                    that.chinaDatas.push([{name: data[0].rrc, value: data[0].p_value}])
                    that.controlSeries(this.selectRRC, [data[0].rrc_lng, data[0].rrc_lat])
                    that.centrl_geo = [data[0].rrc_lng, data[0].rrc_lat]
                    that.zoom = 8
                    that.chart.setOption(that.option)
                }
                else if (res.code === 50000){
                    this.$message.error(res.message)
                }
            })
        },
        getList:function(){
            let data = {}
            data['project_id'] = this.project_id
            fetchall_list(data).then(res=>{
                console.log(res)
            })
        },
        convertData:function(data, center) {
            var res = [];
            for(var i = 0; i < data.length; i++) {
                var dataItem = data[i];
                var fromCoord = this.chinaGeoCoordMap[dataItem[0].name];
                var toCoord = center;              //中心点地理坐标
                if(fromCoord && toCoord) {
                    res.push([{
                        coord: fromCoord,
                        value: dataItem[0].value
                    }, {
                        coord: toCoord,
                    }]);
                }
            }
            return res;
        }
    },
    mounted(){
        // this.getList()
        this.chart = echarts.init(document.getElementById('map'))
        this.chart.setOption(this.option)
    }
}
</script>

<style scoped lang="scss">
    .select-box{
        position: absolute;
        z-index: 100;
        width: 200px;
        height: 250px;
        border: #00faff solid 1px;
        margin-left: 20px;
        margin-top: 20px;
        padding: 10px
    }
    /deep/ .el-input__inner{
        background-color: rgba(0, 161, 255, 0.2);
        border: #00a1ff 1px solid;
        color: #00faff
    }
    .confirm-btn{
        margin-top: 20px;
        background: rgba(0, 161, 255, 0.2);
        color: #00faff;
        border: #00a1ff 1px solid;
    }
</style>