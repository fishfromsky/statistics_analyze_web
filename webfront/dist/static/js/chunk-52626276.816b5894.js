(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-52626276"],{"1ebd":function(t,e,a){},"28a8":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticClass:"main-content"},[a("span",[t._v("项目编号：")]),t._v(" "),a("el-select",{staticClass:"project_id",staticStyle:{width:"120px"},attrs:{placeholder:"项目编号"},model:{value:t.project_id,callback:function(e){t.project_id=e},expression:"project_id"}},t._l(t.id_list,(function(t){return a("el-option",{key:t.project_id,attrs:{label:t.project_id,value:t.project_id}})})),1),t._v(" "),a("div",{staticClass:"divider"}),t._v(" "),a("el-button",{staticStyle:{"margin-left":"20px"},attrs:{type:"primary",icon:"el-icon-download"},on:{click:t.handleDownload}},[t._v("下载数据")]),t._v(" "),a("div",{staticClass:"divider"}),t._v(" "),a("el-select",{staticStyle:{"margin-left":"20px"},attrs:{placeholder:"选择实验编号"},model:{value:t.sort_id,callback:function(e){t.sort_id=e},expression:"sort_id"}},t._l(t.sort_list,(function(t){return a("el-option",{key:t.label,attrs:{label:t.label,value:t.value}})})),1),t._v(" "),a("el-button",{staticStyle:{"margin-left":"20px"},attrs:{type:"primary",icon:"el-icon-data-line"},on:{click:t.showGraph}},[t._v("数据可视化")])],1),t._v(" "),a("div",{staticClass:"table-container"},[a("result",{ref:"result",attrs:{projectId:t.project_id},on:{"child-event":t.handleChildEvent}})],1)])},i=[],r=a("6400"),l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.table_loading,expression:"table_loading"}],key:t.tablekey,staticStyle:{width:"100%","margin-top":"20px"},attrs:{data:t.page_data,border:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{label:"标签",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.label))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"年份",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.year))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"生活垃圾清理量",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("i",{staticClass:"el-icon-time"}),t._v(" "),a("span",[t._v(t._s(n.garbage_clear))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"常住人口",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.population))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"城镇人口比",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.ratio_city_rural))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"户数",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.household))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"每户平均人口",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.people_per_capita))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"性别比例",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.ratio_sex))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"年龄构成(0-14)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.age_0_14))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"年龄构成(15-64)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.age_15_64))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"年龄构成(65以上)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.age_65))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"城市居民人均可支配收入",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.disposable_income))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"城市居民人均消费支出",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.consume_cost))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"一般公共财政支出",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.public_cost))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"国内生产总值",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.gdp))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"第一产业产值",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.gdp_first_industry))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"第二产业产值",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.gdp_second_industry))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"第三产业产值",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.gdp_third_industry))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"人均生产总值",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.gnp))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"受教育程度",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.education))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"实验时间",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.time))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"实验编号",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",[t._v(t._s(n.sort))])]}}])})],1),t._v(" "),a("el-dialog",{attrs:{visible:t.chart_dialog,width:"70%"},on:{"update:visible":function(e){t.chart_dialog=e}}},[a("div",{staticStyle:{width:"100%",height:"70vh"}},[a("chartresult",{staticStyle:{height:"80vh"},attrs:{"chart-data":t.graph_data}})],1)]),t._v(" "),a("el-pagination",{staticStyle:{"margin-top":"20px"},attrs:{"current-page":t.currentPage,"page-sizes":[10,20,30,40,50],"page-size":t.page_size,layout:"total, sizes, prev, pager, next, jumper",total:t.total_size},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}})],1)},s=[],o=(a("a481"),a("55dd"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{class:t.className,style:{width:t.width,height:t.height}})}),c=[],u=a("313e"),d=a.n(u),_=a("ed08"),h={data:function(){return{$_sidebarElm:null,$_resizeHandler:null}},mounted:function(){var t=this;this.$_resizeHandler=Object(_["a"])((function(){t.chart&&t.chart.resize()}),100),this.$_initResizeEvent(),this.$_initSidebarResizeEvent()},beforeDestroy:function(){this.$_destroyResizeEvent(),this.$_destroySidebarResizeEvent()},activated:function(){this.$_initResizeEvent(),this.$_initSidebarResizeEvent()},deactivated:function(){this.$_destroyResizeEvent(),this.$_destroySidebarResizeEvent()},methods:{$_initResizeEvent:function(){window.addEventListener("resize",this.$_resizeHandler)},$_destroyResizeEvent:function(){window.removeEventListener("resize",this.$_resizeHandler)},$_sidebarResizeHandler:function(t){"width"===t.propertyName&&this.$_resizeHandler()},$_initSidebarResizeEvent:function(){this.$_sidebarElm=document.getElementsByClassName("sidebar-container")[0],this.$_sidebarElm&&this.$_sidebarElm.addEventListener("transitionend",this.$_sidebarResizeHandler)},$_destroySidebarResizeEvent:function(){this.$_sidebarElm&&this.$_sidebarElm.removeEventListener("transitionend",this.$_sidebarResizeHandler)}}};a("7799");var p={mixins:[h],props:{className:{type:String,default:"chart"},width:{type:String,default:"100%"},height:{type:String,default:"250px"},autoResize:{type:Boolean,default:!0},chartData:{type:Object,required:!0}},data:function(){return{chart:null}},watch:{chartData:{deep:!0,handler:function(t){this.setOptions(t)}}},mounted:function(){var t=this;this.$nextTick((function(){t.initChart()}))},beforeDestroy:function(){this.chart&&(this.chart.dispose(),this.chart=null)},methods:{initChart:function(){this.chart=d.a.init(this.$el,"roma"),this.setOptions(this.chartData)},setOptions:function(t){this.chart.setOption({title:{text:"关联分析混淆矩阵",left:"center"},tooltip:{position:"top"},animation:!1,grid:{height:"50%",top:"10%",left:"70"},xAxis:{type:"category",data:t.label,axisLabel:{interval:0,rotate:"45"},splitArea:{show:!0}},yAxis:{type:"category",data:t.label,axisLabel:{interval:0,rotate:"60"},splitArea:{show:!0}},visualMap:{min:0,max:1,calculable:!0,orient:"horizontal",left:"center",bottom:"15%"},series:[{name:"相关系数",type:"heatmap",data:t.result,label:{show:!0},emphasis:{itemStyle:{shadowBlur:10,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]})}}},f=p,v=a("2877"),b=Object(v["a"])(f,o,c,!1,null,"35c3f9da",null),g=b.exports,m={components:{chartresult:g},props:{projectId:{type:String,required:!0}},data:function(){return{chart_dialog:!1,table_loading:!1,tablekey:0,tableData:[],page_data:[],total_size:0,currentPage:1,page_size:10,project_id:"",filename:"relation_result",autoWidth:!0,bookType:"xlsx",sort_list:[],graph_data:{reuslt:[],label:[]}}},watch:{projectId:function(t,e){this.project_id=t,this.initTable(t),this.page_data=[],this.tableData=[],this.sort_list=[]}},methods:{showChart:function(t){this.graph_data.result=[],this.graph_data.label=[],this.chart_dialog=!0;for(var e=this.tableData,a=0;a<e.length;a++)e[a].sort===t&&this.graph_data.label.push(e[a].label);for(var n=this.graph_data.label,i=0,r=0;r<e.length;r++)if(e[r].sort===t){for(var l=0;l<n.length;l++){var s=[i,l];s.push(e[r][n[l]].toFixed(2)),this.graph_data.result.push(s)}i++}},timeStamptoTime:function(t){var e=new Date(t),a=e.getFullYear()+"-",n=(e.getMonth()+1<10?"0"+(e.getMonth()+1):e.getMonth()+1)+"-",i=e.getDate()+" ",r=e.getHours()+":",l=e.getMinutes()+":",s=e.getSeconds();return a+n+i+r+l+s},handleSizeChange:function(t){this.table_loading=!0,this.page_size=t,this.currentPage=1,this.page_data=[],this.initTable(this.project_id)},handleCurrentChange:function(t){this.currentPage=t,this.page_data=[],this.initTable(this.project_id)},initTable:function(t){var e=this,a={};a["project_id"]=t,this.table_loading=!0,Object(r["Gb"])(a).then((function(t){e.table_loading=!1,e.tableData=t.data;for(var a=0;a<t.data.length;a++){var n=t.data[a].time;n=new Date(n.replace(/-/g,"/")).getTime()+288e5,t.data[a].time=e.timeStamptoTime(n)}for(var i=e.page_size,r=e.currentPage-1,l=r*i;l<(r+1)*i;l++){if(l==t.data.length)break;e.page_data.push(t.data[l])}e.total_size=t.data.length;for(var s=0;s<e.tableData.length;s++)e.isInArray(e.sort_list,e.tableData[s].sort)||e.sort_list.push(e.tableData[s].sort);e.$emit("child-event",e.sort_list)}))},isInArray:function(t,e){for(var a=0;a<t.length;a++)if(e===t[a])return!0;return!1},formatJson:function(t,e){return e.map((function(e){return t.map((function(t){return"timestamp"===t?parseTime(e[t]):e[t]}))}))},download:function(){var t=this;Promise.all([a.e("chunk-6e87ca78"),a.e("chunk-40dff864"),a.e("chunk-3f8a70b2")]).then(a.bind(null,"4bf8d")).then((function(e){var a=["Year","Garbage_clear","Population","Ratio_city_rural","Household","People_per_capita","Ratio_sex","Age_0_14","Age_15_64","Age_65","Disposable_income","Consume_cost","Public_cost","GDP","Gdp_first_industry","Gdp_second_industry","Gdp_third_industry","GNP","Education","Sort","Time"],n=["year","garbage_clear","population","ratio_city_rural","household","people_per_capita","ratio_sex","age_0_14","age_15_64","age_65","disposable_income","consume_cost","public_cost","gdp","gdp_first_industry","gdp_second_industry","gdp_third_industry","gnp","education","sort","time"],i=t.tableData,r=t.formatJson(n,i);e.export_json_to_excel({header:a,data:r,filename:t.filename,autoWidth:t.autoWidth,bookType:t.bookType})}))}},mounted:function(){}},y=m,w=Object(v["a"])(y,l,s,!1,null,"f1d1a370",null),S=w.exports,k={components:{result:S},data:function(){return{project_id:"",sort_id:null,id_list:[],sort_list:[]}},methods:{init_projectId:function(){var t=this;Object(r["rb"])().then((function(e){for(var a=e.data,n=0;n<a.length;n++)t.id_list.push(a[n])}))},handleDownload:function(){this.$refs.result.download()},handleChildEvent:function(t){this.sort_list=[];for(var e=0;e<t.length;e++){var a={};a["value"]=t[e],a["label"]=t[e],this.sort_list.push(a)}},showGraph:function(){null===this.sort_id?this.$message.error("请选择实验编号"):this.$refs.result.showChart(this.sort_id)}},mounted:function(){this.init_projectId()}},z=k,$=(a("5d41"),Object(v["a"])(z,n,i,!1,null,"4cd0d018",null));e["default"]=$.exports},"5d41":function(t,e,a){"use strict";var n=a("1ebd"),i=a.n(n);i.a}}]);