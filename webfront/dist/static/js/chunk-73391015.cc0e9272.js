(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-73391015"],{"0df1":function(t,e,n){"use strict";var a=n("e1b5"),r=n.n(a);r.a},1:function(t,e){},2:function(t,e){},"20f3":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("column",{on:{"child-event":t.handle_dialog,"id-event":t.handle_id}}),t._v(" "),n("datatable",{attrs:{parentmsg:t.table_transfer_id}}),t._v(" "),n("el-dialog",{attrs:{title:"上传数据",visible:t.upload_dialog,width:"80%"},on:{"update:visible":function(e){t.upload_dialog=e}}},[n("div",{staticClass:"btn-column"},[n("el-button",{on:{click:t.cancelInput}},[t._v("取消")]),t._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:t.InputParameter}},[t._v("上传")]),t._v(" "),n("el-select",{staticClass:"project_id",attrs:{placeholder:"项目编号"},model:{value:t.project_id,callback:function(e){t.project_id=e},expression:"project_id"}},t._l(t.id_list,(function(t){return n("el-option",{key:t.project_id,attrs:{label:t.project_id,value:t.project_id}})})),1)],1),t._v(" "),t.hasData?t._e():n("uploadexcel",{staticStyle:{"margin-top":"20px"},attrs:{"on-success":t.handleSuccess,"before-upload":t.beforeUpload}}),t._v(" "),n("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.table_loading,expression:"table_loading"}],staticStyle:{width:"100%","margin-top":"20px"},attrs:{data:t.tableData,border:"","highlight-current-row":""}},t._l(t.tableHeader,(function(t){return n("el-table-column",{key:t,attrs:{prop:t,label:t}})})),1)],1)],1)},r=[],o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("div",{staticClass:"column_list"},[n("el-select",{staticClass:"project_id",attrs:{placeholder:"项目编号"},model:{value:t.project_id,callback:function(e){t.project_id=e},expression:"project_id"}},t._l(t.id_list,(function(t){return n("el-option",{key:t.project_id,attrs:{label:t.project_id,value:t.project_id}})})),1),t._v(" "),n("el-button",{staticClass:"search-btn",attrs:{type:"primary",icon:"el-icon-search"},on:{click:t.get_data}},[t._v("搜索数据")]),t._v(" "),n("div",{staticClass:"divider"}),t._v(" "),n("el-button",{staticClass:"input-btn",attrs:{type:"primary",icon:"el-icon-upload2"},on:{click:t.input_data}},[t._v("上传数据")])],1)])},u=[],i=n("6400"),c=(n("3fd3"),{data:function(){return{project_id:"",id_list:[]}},methods:{get_project_id:function(){var t=this;Object(i["gb"])().then((function(e){for(var n=e.data,a=0;a<n.length;a++)t.id_list.push(n[a])}))},get_data:function(){this.$emit("id-event",this.project_id)},input_data:function(){this.$emit("child-event","true")}},mounted:function(){this.get_project_id()}}),l=c,d=(n("0df1"),n("2877")),s=Object(d["a"])(l,o,u,!1,null,null,null),f=s.exports,p=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.table_loading,expression:"table_loading"}],key:t.tablekey,staticStyle:{width:"95%",margin:"0 auto"},attrs:{data:t.page_data,border:"",fit:"","highlight-current-row":""}},[n("el-table-column",{attrs:{label:"项目编号",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.project_id))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"人口(10,000)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.resident_population))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"人口密度(p/sq km)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.population_of_density))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"住户数(10,000)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.number_of_households))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"平均每户人口(p)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.average_population_per_household))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"人均可支配收入(元)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.urban_residents_per_capita_disposable_income))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"人均消费支出(元)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.consumer_expenditure))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"公共支出(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.general_public_expenditure))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"基础设施投资(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.investment_in_urban_infrastructure))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"城市人口密度(p/sq km)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.urban_population_density))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"绿植覆盖率(%)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.greening_coverage))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"本地生产总值(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.gross_local_product))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"人均GDP(元)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.gross_domestic_product_per_capita))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"第一产业产值(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.gross_domestic_product_of_the_first_industry))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"第二产业产值(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.gross_value_of_secondary_industry))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"第三产业产值(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.investment_in_environmental_protection))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"第三产业产值(十亿)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.investment_in_environmental_protection))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"环保投资(百万)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.investment_in_environmental_protection))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"大学生数(10,000)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.number_of_college_students))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"员工受教育程度(%)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.level_of_education))])]}}])}),t._v(" "),n("el-table-column",{attrs:{label:"垃圾产量(10,000吨)",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){var a=e.row;return[n("span",[t._v(t._s(a.municial_household_garbage))])]}}])})],1),t._v(" "),n("el-pagination",{staticStyle:{"margin-top":"20px","margin-left":"2.5%"},attrs:{"current-page":t.currentPage,"page-sizes":[10,20,30,40,50],"page-size":t.page_size,layout:"total, sizes, prev, pager, next, jumper",total:t.total_size},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}})],1)},_=[],b={props:{parentmsg:{type:String,required:!0}},data:function(){return{project_id:null,table_loading:!1,tablekey:0,tableData:[],page_data:[],total_size:0,currentPage:1,page_size:10}},watch:{parentmsg:function(t,e){this.project_id=t;this.tableData=[],this.page_data=[],this.getData()}},methods:{getData:function(){var t={},e=this;t["project_id"]=this.project_id,Object(i["ob"])(t).then((function(t){if(2e4===t.code){e.table_loading=!1,e.tableData=t.data;for(var n=e.page_size,a=e.currentPage-1,r=a*n;r<(a+1)*n;r++){if(r==t.data.length)break;e.page_data.push(t.data[r])}e.total_size=t.data.length}}))},handleSizeChange:function(t){this.table_loading=!0,this.page_size=t,this.currentPage=1,this.page_data=[],this.getData()},handleCurrentChange:function(t){this.currentPage=t,this.page_data=[],this.getData()}}},g=b,h=Object(d["a"])(g,p,_,!1,null,null,null),m=h.exports,v=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("input",{ref:"excel-upload-input",staticClass:"excel-upload-input",attrs:{type:"file",accept:".xlsx, .xls"},on:{change:t.handleClick}}),t._v(" "),n("div",{staticClass:"drop",on:{drop:t.handleDrop,dragover:t.handleDragover,dragenter:t.handleDragover,click:t.handleUpload}},[n("i",{staticClass:"el-icon-upload"}),t._v(" "),n("span",[t._v("将模型文件拖曳至此或者点击此处选择文件(仅限Excel)")])])])},j=[],y=(n("7f7f"),n("1146")),O=n.n(y),k={props:{beforeUpload:Function,onSuccess:Function},data:function(){return{loading:!1,excelData:{header:null,results:null}}},methods:{generateData:function(t){var e=t.header,n=t.results;this.excelData.header=e,this.excelData.results=n,this.onSuccess&&this.onSuccess(this.excelData)},handleDrop:function(t){if(t.stopPropagation(),t.preventDefault(),!this.loading){var e=t.dataTransfer.files;if(1===e.length){var n=e[0];if(!this.isExcel(n))return this.$message.error("Only supports upload .xlsx, .xls, .csv suffix files"),!1;this.upload(n),t.stopPropagation(),t.preventDefault()}else this.$message.error("Only support uploading one file!")}},handleDragover:function(t){t.stopPropagation(),t.preventDefault(),t.dataTransfer.dropEffect="copy"},handleUpload:function(){this.$refs["excel-upload-input"].click()},handleClick:function(t){var e=t.target.files,n=e[0];n&&this.upload(n)},upload:function(t){if(this.$refs["excel-upload-input"].value=null,this.beforeUpload){var e=this.beforeUpload(t);e&&this.readerData(t)}else this.readerData(t)},readerData:function(t){var e=this;return this.loading=!0,new Promise((function(n,a){var r=new FileReader;r.onload=function(t){var a=t.target.result,r=O.a.read(a,{type:"array"}),o=r.SheetNames[0],u=r.Sheets[o],i=e.getHeaderRow(u),c=O.a.utils.sheet_to_json(u);e.generateData({header:i,results:c}),e.loading=!1,n()},r.readAsArrayBuffer(t)}))},getHeaderRow:function(t){var e,n=[],a=O.a.utils.decode_range(t["!ref"]),r=a.s.r;for(e=a.s.c;e<=a.e.c;++e){var o=t[O.a.utils.encode_cell({c:e,r:r})],u="UNKNOWN "+e;o&&o.t&&(u=O.a.utils.format_cell(o)),n.push(u)}return n},isExcel:function(t){return/\.(xlsx|xls|csv)$/.test(t.name)}}},w=k,D=(n("6fb2"),Object(d["a"])(w,v,j,!1,null,"14c0001c",null)),x=D.exports,S={name:"index",components:{column:f,datatable:m,uploadexcel:x},data:function(){return{table_loading:!1,upload_dialog:!1,hasData:!1,tableData:[],tableHeader:[],project_id:"",id_list:[],table_transfer_id:""}},methods:{get_project_id:function(){var t=this;Object(i["gb"])().then((function(e){for(var n=e.data,a=0;a<n.length;a++)t.id_list.push(n[a])}))},handle_dialog:function(t){this.upload_dialog=!0},handle_id:function(t){""!==t&&(this.table_transfer_id=t)},beforeUpload:function(t){var e=t.size/1024/1024<1;return!!e||(this.$message({message:"Please do not upload files larger than 1m in size.",type:"warning"}),!1)},handleSuccess:function(t){var e=t.results,n=t.header;this.tableData=e,this.tableHeader=n,this.hasData=!0},cancelInput:function(){this.tableData=[],this.tableHeader=[],this.upload_dialog=!1,this.hasData=!1},DataInput:function(t){var e=this;if(""===this.project_id)this.$message.error("请选择项目编号");else{var n=this;this.table_loading=!0;for(var a=[],r=0;r<this.tableData.length;r++)a.push(this.tableData[r]);var o={};o["data"]=a,o["project_id"]=this.project_id,t(o).then((function(t){n.table_loading=!1,2e4===t.code?e.$message({type:"success",message:"导入数据成功"}):(e.$message.error(t.message),n.table_loading=!1),n.tableData=[],n.tableHeader=[],n.hasData=!1})).catch((function(t){console.log(t),n.table_loading=!1,n.tableData=[],n.tableHeader=[],n.hasData=!1}))}},InputParameter:function(){this.DataInput(i["zb"])}},mounted:function(){this.get_project_id()}},C=S,z=(n("89cd"),Object(d["a"])(C,a,r,!1,null,"1013fb60",null));e["default"]=z.exports},3:function(t,e){},"504a":function(t,e,n){},6400:function(t,e,n){"use strict";n.d(e,"f",(function(){return r})),n.d(e,"j",(function(){return o})),n.d(e,"k",(function(){return u})),n.d(e,"fb",(function(){return i})),n.d(e,"T",(function(){return c})),n.d(e,"F",(function(){return l})),n.d(e,"w",(function(){return d})),n.d(e,"vb",(function(){return s})),n.d(e,"K",(function(){return f})),n.d(e,"U",(function(){return p})),n.d(e,"x",(function(){return _})),n.d(e,"i",(function(){return b})),n.d(e,"e",(function(){return g})),n.d(e,"g",(function(){return h})),n.d(e,"d",(function(){return m})),n.d(e,"l",(function(){return v})),n.d(e,"h",(function(){return j})),n.d(e,"Y",(function(){return y})),n.d(e,"eb",(function(){return O})),n.d(e,"bb",(function(){return k})),n.d(e,"cb",(function(){return w})),n.d(e,"ab",(function(){return D})),n.d(e,"db",(function(){return x})),n.d(e,"z",(function(){return S})),n.d(e,"N",(function(){return C})),n.d(e,"E",(function(){return z})),n.d(e,"S",(function(){return P})),n.d(e,"B",(function(){return $})),n.d(e,"P",(function(){return E})),n.d(e,"C",(function(){return H})),n.d(e,"Q",(function(){return U})),n.d(e,"A",(function(){return I})),n.d(e,"O",(function(){return N})),n.d(e,"D",(function(){return q})),n.d(e,"R",(function(){return A})),n.d(e,"Z",(function(){return F})),n.d(e,"u",(function(){return R})),n.d(e,"t",(function(){return T})),n.d(e,"s",(function(){return B})),n.d(e,"r",(function(){return J})),n.d(e,"q",(function(){return G})),n.d(e,"v",(function(){return K})),n.d(e,"n",(function(){return W})),n.d(e,"qb",(function(){return L})),n.d(e,"H",(function(){return M})),n.d(e,"pb",(function(){return Q})),n.d(e,"lb",(function(){return V})),n.d(e,"nb",(function(){return X})),n.d(e,"mb",(function(){return Y})),n.d(e,"V",(function(){return Z})),n.d(e,"L",(function(){return tt})),n.d(e,"Bb",(function(){return et})),n.d(e,"W",(function(){return nt})),n.d(e,"b",(function(){return at})),n.d(e,"y",(function(){return rt})),n.d(e,"a",(function(){return ot})),n.d(e,"yb",(function(){return ut})),n.d(e,"jb",(function(){return it})),n.d(e,"wb",(function(){return ct})),n.d(e,"kb",(function(){return lt})),n.d(e,"rb",(function(){return dt})),n.d(e,"o",(function(){return st})),n.d(e,"I",(function(){return ft})),n.d(e,"Ab",(function(){return pt})),n.d(e,"xb",(function(){return _t})),n.d(e,"sb",(function(){return bt})),n.d(e,"Db",(function(){return gt})),n.d(e,"tb",(function(){return ht})),n.d(e,"m",(function(){return mt})),n.d(e,"ib",(function(){return vt})),n.d(e,"G",(function(){return jt})),n.d(e,"Cb",(function(){return yt})),n.d(e,"hb",(function(){return Ot})),n.d(e,"gb",(function(){return kt})),n.d(e,"zb",(function(){return wt})),n.d(e,"ob",(function(){return Dt})),n.d(e,"X",(function(){return xt})),n.d(e,"c",(function(){return St})),n.d(e,"M",(function(){return Ct})),n.d(e,"p",(function(){return zt})),n.d(e,"ub",(function(){return Pt})),n.d(e,"J",(function(){return $t}));var a=n("b775");n("3fd3");function r(t){return Object(a["a"])({url:"/addcitygarbagedeal",method:"post",data:t})}function o(t){return Object(a["a"])({url:"/addcityfactorylist",method:"post",data:t})}function u(t){return Object(a["a"])({url:"/addfactorylist",method:"post",data:t})}function i(){return Object(a["a"])({url:"/getfactorylist",method:"get"})}function c(t){return Object(a["a"])({url:"/deletefactorylist",method:"post",data:t})}function l(t){return Object(a["a"])({url:"/amendfactorylist",method:"post",data:t})}function d(t){return Object(a["a"])({url:"/addtransferfactory",method:"post",data:t})}function s(){return Object(a["a"])({url:"/gettransferfactory",method:"get"})}function f(t){return Object(a["a"])({url:"/amendtransferfactory",method:"post",data:t})}function p(t){return Object(a["a"])({url:"/deletetransferfactory",method:"post",data:t})}function _(t){return Object(a["a"])({url:"/addtransferbyrow",method:"post",data:t})}function b(t){return Object(a["a"])({url:"/addcollectfactory",method:"post",data:t})}function g(t){return Object(a["a"])({url:"/addcitygarbagecapacity",method:"post",data:t})}function h(t){return Object(a["a"])({url:"/addcitygarbagevolume",method:"post",data:t})}function m(t){return Object(a["a"])({url:"/addcityeconomy",method:"post",data:t})}function v(t){return Object(a["a"])({url:"/addbatchgarbagecity",method:"post",data:t})}function j(t){return Object(a["a"])({url:"/addcitypopulation",method:"post",data:t})}function y(){return Object(a["a"])({url:"/geteconomycity",method:"get"})}function O(){return Object(a["a"])({url:"/getpopulationcity",method:"get"})}function k(){return Object(a["a"])({url:"/getgarbagecity",method:"get"})}function w(){return Object(a["a"])({url:"/getgarbagedealcity",method:"get"})}function D(){return Object(a["a"])({url:"/getgarbagecapacitycity",method:"get"})}function x(){return Object(a["a"])({url:"/getgarbagevolumecity",method:"get"})}function S(t){return Object(a["a"])({url:"/amendcityeconomydata",method:"post",data:t})}function C(t){return Object(a["a"])({url:"/deletecityeconomydata",method:"post",data:t})}function z(t){return Object(a["a"])({url:"/amendcitypopulationdata",method:"post",data:t})}function P(t){return Object(a["a"])({url:"/deletecitypopulationdata",method:"post",data:t})}function $(t){return Object(a["a"])({url:"/amendcitygarbagedata",method:"post",data:t})}function E(t){return Object(a["a"])({url:"/deletecitygarbagedata",method:"post",data:t})}function H(t){return Object(a["a"])({url:"/amendcitygarbagedealdata",method:"post",data:t})}function U(t){return Object(a["a"])({url:"/deletecitygarbagedealdata",method:"post",data:t})}function I(t){return Object(a["a"])({url:"/amendcitygarbagecapacitydata",method:"post",data:t})}function N(t){return Object(a["a"])({url:"/deletecitygarbagecapacitydata",method:"post",data:t})}function q(t){return Object(a["a"])({url:"/amendcitygarbagevolumedata",method:"post",data:t})}function A(t){return Object(a["a"])({url:"/deletecitygarbagevolumedata",method:"post",data:t})}function F(){return Object(a["a"])({url:"/getgarbagecity",method:"get"})}function R(t){return Object(a["a"])({url:"/addsinglerowdata",method:"post",data:t})}function T(t){return Object(a["a"])({url:"/addsinglepopulation",method:"post",data:t})}function B(t){return Object(a["a"])({url:"/addsinglegarbage",method:"post",data:t})}function J(t){return Object(a["a"])({url:"/addsingledealgarbage",method:"post",data:t})}function G(t){return Object(a["a"])({url:"/addsinglecapacitygarbage",method:"post",data:t})}function K(t){return Object(a["a"])({url:"/addsinglevolumegarbage",method:"post",data:t})}function W(t){return Object(a["a"])({url:"/addpmedianproject",method:"post",data:t})}function L(){return Object(a["a"])({url:"/getpmedianproject",method:"get"})}function M(t){return Object(a["a"])({url:"/amendpmedianproject",method:"post",data:t})}function Q(t){return Object(a["a"])({url:"/startpmedianproject",method:"post",data:t})}function V(t){return Object(a["a"])({url:"/getnationpm",method:"post",data:t})}function X(t){return Object(a["a"])({url:"/getnationwaterpollution",method:"post",data:t})}function Y(t){return Object(a["a"])({url:"/getnationsolidpollution",method:"post",data:t})}function Z(t){return Object(a["a"])({url:"/getcrawlrecord",method:"get",params:{type:t}})}function tt(t){return Object(a["a"])({url:"/deletecrawldata",method:"get",params:{id:t}})}function et(t){return Object(a["a"])({url:"/getcrawl_select",method:"get",params:t})}function nt(){return Object(a["a"])({url:"/getlstmproject",method:"get"})}function at(t){return Object(a["a"])({url:"/addlstmproject",method:"POST",data:t})}function rt(t){return Object(a["a"])({url:"/amendlstmproject",method:"post",data:t})}function ot(t){return Object(a["a"])({url:"/experiment_lstm_start",method:"post",data:t})}function ut(){return Object(a["a"])({url:"/lstm_project_id",method:"get"})}function it(t){return Object(a["a"])({url:"/get_parameter_lstm",method:"get",params:t})}function ct(t){return Object(a["a"])({url:"/input_parameter_lstm",method:"post",data:t})}function lt(t){return Object(a["a"])({url:"/get_lstm_result",method:"get",params:t})}function dt(){return Object(a["a"])({url:"/get_regression",method:"get"})}function st(t){return Object(a["a"])({url:"/add_regression",method:"post",data:t})}function ft(t){return Object(a["a"])({url:"/amend_regression",method:"post",data:t})}function pt(){return Object(a["a"])({url:"/get_id_regression",method:"get"})}function _t(t){return Object(a["a"])({url:"/add_parameter_regression",method:"post",data:t})}function bt(t){return Object(a["a"])({url:"/get_parameter_regression",method:"get",params:t})}function gt(t){return Object(a["a"])({url:"/start_regression_experiment",method:"post",data:t})}function ht(t){return Object(a["a"])({url:"/get_result_regression",method:"get",params:t})}function mt(t){return Object(a["a"])({url:"/add_kmeans_project",method:"post",data:t})}function vt(){return Object(a["a"])({url:"/get_kmeans_project",method:"get"})}function jt(t){return Object(a["a"])({url:"/amend_kmeans_project",method:"post",data:t})}function yt(t){return Object(a["a"])({url:"/start_kmeans",method:"post",data:t})}function Ot(t){return Object(a["a"])({url:"/get_result_kmeans",method:"get",params:t})}function kt(){return Object(a["a"])({url:"/get_id_kmeans",method:"get"})}function wt(t){return Object(a["a"])({url:"/input_parameter_kmeans",method:"post",data:t})}function Dt(){return Object(a["a"])({url:"/get_parameter_kmeans",method:"get"})}function xt(){return Object(a["a"])({url:"/get_algorithm_list",method:"get"})}function St(t){return Object(a["a"])({url:"/add_algorithm_list",method:"post",data:t})}function Ct(t){return Object(a["a"])({url:"/delete_algorithm_list",method:"post",data:t})}function zt(t){return Object(a["a"])({url:"/add_relation_project",method:"post",data:t})}function Pt(){return Object(a["a"])({url:"/get_relation_project",method:"get"})}function $t(t){return Object(a["a"])({url:"/amend_relation_project",method:"post",data:t})}},"6fb2":function(t,e,n){"use strict";var a=n("d067"),r=n.n(a);r.a},"89cd":function(t,e,n){"use strict";var a=n("504a"),r=n.n(a);r.a},d067:function(t,e,n){},e1b5:function(t,e,n){}}]);