(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1f024d52"],{1:function(e,a){},2:function(e,a){},3:function(e,a){},"585e":function(e,a,t){},6400:function(e,a,t){"use strict";t.d(a,"f",(function(){return n})),t.d(a,"e",(function(){return s})),t.d(a,"c",(function(){return r})),t.d(a,"d",(function(){return o})),t.d(a,"a",(function(){return i})),t.d(a,"b",(function(){return c}));var l=t("b775");t("3fd3");function n(){return Object(l["a"])({url:"/getmodel",method:"get"})}function s(e){return Object(l["a"])({url:"/fetchmodel",method:"get",params:e})}function r(e){return Object(l["a"])({url:"/amendmodel",method:"post",data:e})}function o(e){return Object(l["a"])({url:"/deletemodel",method:"get",params:e})}function i(e){return Object(l["a"])({url:"/addcityeconomy",method:"post",data:e})}function c(e){return Object(l["a"])({url:"/addcitypopulation",method:"post",data:e})}},"6a50":function(e,a,t){"use strict";var l=t("585e"),n=t.n(l);n.a},"90fe":function(e,a,t){"use strict";t.r(a);var l=function(){var e=this,a=e.$createElement,t=e._self._c||a;return t("div",{staticClass:"app-container"},[e.hasData?t("div",{staticClass:"save-list"},[t("div",{staticClass:"data-list"},[t("div",{staticClass:"model-name"},[t("span",{staticClass:"name-span"},[e._v("数据级别")]),e._v(" "),t("el-select",{staticClass:"name-input",attrs:{placeholder:"选择数据级别"},model:{value:e.area,callback:function(a){e.area=a},expression:"area"}},e._l(e.level_list,(function(e){return t("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})})),1)],1),e._v(" "),t("div",{staticClass:"model-name"},[t("span",{staticClass:"name-span"},[e._v("数据类型")]),e._v(" "),t("el-select",{staticClass:"rate",attrs:{placeholder:"请输入具体表项类型"},model:{value:e.kind,callback:function(a){e.kind=a},expression:"kind"}},e._l(e.kind_list,(function(e){return t("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})})),1)],1),e._v(" "),t("el-button",{staticClass:"addmodel-btn",attrs:{type:"primary",icon:"el-icon-document-add"},on:{click:e.AddModel}},[e._v("导入数据")])],1)]):t("upload-excel-component",{attrs:{"on-success":e.handleSuccess,"before-upload":e.beforeUpload}}),e._v(" "),t("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.table_loading,expression:"table_loading"}],staticStyle:{width:"100%","margin-top":"20px"},attrs:{data:e.tableData,border:"","highlight-current-row":""}},e._l(e.tableHeader,(function(e){return t("el-table-column",{key:e,attrs:{prop:e,label:e}})})),1)],1)},n=[],s=function(){var e=this,a=e.$createElement,t=e._self._c||a;return t("div",[t("input",{ref:"excel-upload-input",staticClass:"excel-upload-input",attrs:{type:"file",accept:".xlsx, .xls"},on:{change:e.handleClick}}),e._v(" "),t("div",{staticClass:"drop",on:{drop:e.handleDrop,dragover:e.handleDragover,dragenter:e.handleDragover,click:e.handleUpload}},[t("i",{staticClass:"el-icon-upload"}),e._v(" "),t("span",[e._v("将模型文件拖曳至此或者点击此处选择文件(仅限Excel)")])])])},r=[],o=(t("7f7f"),t("1146")),i=t.n(o),c={props:{beforeUpload:Function,onSuccess:Function},data:function(){return{loading:!1,excelData:{header:null,results:null}}},methods:{generateData:function(e){var a=e.header,t=e.results;this.excelData.header=a,this.excelData.results=t,this.onSuccess&&this.onSuccess(this.excelData)},handleDrop:function(e){if(e.stopPropagation(),e.preventDefault(),!this.loading){var a=e.dataTransfer.files;if(1===a.length){var t=a[0];if(!this.isExcel(t))return this.$message.error("Only supports upload .xlsx, .xls, .csv suffix files"),!1;this.upload(t),e.stopPropagation(),e.preventDefault()}else this.$message.error("Only support uploading one file!")}},handleDragover:function(e){e.stopPropagation(),e.preventDefault(),e.dataTransfer.dropEffect="copy"},handleUpload:function(){this.$refs["excel-upload-input"].click()},handleClick:function(e){var a=e.target.files,t=a[0];t&&this.upload(t)},upload:function(e){if(this.$refs["excel-upload-input"].value=null,this.beforeUpload){var a=this.beforeUpload(e);a&&this.readerData(e)}else this.readerData(e)},readerData:function(e){var a=this;return this.loading=!0,new Promise((function(t,l){var n=new FileReader;n.onload=function(e){var l=e.target.result,n=i.a.read(l,{type:"array"}),s=n.SheetNames[0],r=n.Sheets[s],o=a.getHeaderRow(r),c=i.a.utils.sheet_to_json(r);a.generateData({header:o,results:c}),a.loading=!1,t()},n.readAsArrayBuffer(e)}))},getHeaderRow:function(e){var a,t=[],l=i.a.utils.decode_range(e["!ref"]),n=l.s.r;for(a=l.s.c;a<=l.e.c;++a){var s=e[i.a.utils.encode_cell({c:a,r:n})],r="UNKNOWN "+a;s&&s.t&&(r=i.a.utils.format_cell(s)),t.push(r)}return t},isExcel:function(e){return/\.(xlsx|xls|csv)$/.test(e.name)}}},u=c,d=(t("6a50"),t("2877")),f=Object(d["a"])(u,s,r,!1,null,"1ee19a4e",null),p=f.exports,h=(t("5f87"),t("6400")),v={name:"UploadExcel",components:{UploadExcelComponent:p},data:function(){return{tableData:[],tableHeader:[],hasData:!1,area:"",kind:"",level_list:[{value:"1",label:"市级"}],kind_list:[{value:"1",label:"经济数据"},{value:"2",label:"人口数据"},{value:"3",label:"生活垃圾处理"},{value:"4",label:"无害化处理厂数量"},{value:"5",label:"无害化处理能力"},{value:"6",label:"无害化处理量"}],star:null,table_loading:!1}},methods:{beforeUpload:function(e){var a=e.size/1024/1024<1;return!!a||(this.$message({message:"Please do not upload files larger than 1m in size.",type:"warning"}),!1)},handleSuccess:function(e){var a=e.results,t=e.header;this.tableData=a,this.tableHeader=t,this.hasData=!0,console.log(this.tableData)},AddModel:function(){var e=this,a=this;if(""===a.area)a.$message.error("数据级别不能为空");else if(""===a.kind)a.$message.error("数据表类型不能为空");else if("1"===a.area&&"1"===a.kind){this.table_loading=!0;for(var t=[],l=0;l<this.tableData.length;l++)t.push(this.tableData[l]);var n={};n["data"]=t,Object(h["a"])(n).then((function(t){a.table_loading=!1,2e4===t.code?e.$message({type:"success",message:"导入数据成功"}):e.$message.error(t.message)})).catch((function(e){a.table_loading=!1}))}else if("1"===a.area&&"2"===a.kind){this.table_loading=!0;for(var s=[],r=0;r<this.tableData.length;r++)s.push(this.tableData[r]);var o={};o["data"]=s,Object(h["b"])(o).then((function(t){a.table_loading=!1,2e4===t.code?e.$message({type:"success",message:"导入数据成功"}):e.$message.error(t.message)})).catch((function(e){a.table_loading=!1}))}}}},b=v,g=(t("ae7a"),Object(d["a"])(b,l,n,!1,null,"7300cbbf",null));a["default"]=g.exports},ae7a:function(e,a,t){"use strict";var l=t("b9b3"),n=t.n(l);n.a},b9b3:function(e,a,t){}}]);