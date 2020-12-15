import request from '@/utils/request'
import da from 'element-ui/src/locale/lang/da'
import { expr } from 'jquery'

export function getmodel() {
  return request({
    url: '/getmodel',
    method: 'get'
  })
}

export function fetchmodel(data) {
  return request({
    url: '/fetchmodel',
    method: 'get',
    params: data
  })
}

export function amendmodel(data) {
  return request({
    url: '/amendmodel',
    method: 'post',
    data
  })
}

export function deletemodel(data) {
  return request({
    url: '/deletemodel',
    method: 'get',
    params: data
  })
}

export function addmodel(data) {
  return request({
    url: '/addmodel',
    method: 'get',
    params: data
  })
}
// 批量导入城市
export function addcity(data) {
  return request({
    url: '/add_city',
    method: 'post',
    data
  })
}
// 批量导入街区
export function adddistrict(data) {
  return request({
    url: '/adddistrict',
    method: 'post',
    data
  })
}
// 批量导入城镇
export function addtown(data) {
  return request({
    url: '/addtown',
    method: 'post',
    data
  })
}
// 批量导入无害化处理厂信息
export function addcitygarbagedeal(data) {
  return request({
    url: '/addcitygarbagedeal',
    method: 'post',
    data
  })
}
//批量导入处理厂具体信息
export function addfacorylist(data){
  return request({
    url: '/addcityfactorylist',
    method: 'post',
    data
  })
}
// 单独添加无害化处理厂信息
export function addfactorylistbyrow(data){
  return request({
    url: '/addfactorylist',
    method: 'post',
    data
  })
}
// 获取无害化处理厂具体信息表
export function getfactorylist(){
  return request({
    url: '/getfactorylist',
    method: 'get'
  })
}
// 删除无害化处理厂信息
export function deletefactorylist(data){
  return request({
    url: '/deletefactorylist',
    method: 'post',
    data
  })
}
export function amendfactorylist(data){
  return request({
    url: '/amendfactorylist',
    method: 'post',
    data
  })
}
// 批量导入中转站信息表
export function addtransferfactory(data){
  return request({
    url: '/addtransferfactory',
    method: 'post',
    data
  })
}
// 获取中转站信息
export function gettransferfactory(){
  return request({
    url: '/gettransferfactory',
    method: 'get'
  })
}
// 修改中转站信息
export function amendtransferfactory(data){
  return request({
    url: '/amendtransferfactory',
    method: 'post',
    data
  })
}
// 删除中转站信息
export function deletetransferfactory(data){
  return request({
    url: '/deletetransferfactory',
    method: 'post',
    data
  })
}
// 添加中转站信息
export function addtransferfactorybyrow(data){
  return request({
    url: '/addtransferbyrow',
    method: 'post',
    data
  })
}
// 批量导入收集点信息
export function addcollectfactory(data){
  return request({
    url: '/addcollectfactory',
    method: 'post',
    data
  })
}
// 获取指定区域收集点信息
export function getcollectfactorybyarea(data){
  return request({
    url: '/getcollectfactorybyarea',
    method: 'get',
    params: data
  })
}
// 批量导入无害化处理能力信息
export function addcitygarbagecapacity(data) {
  return request({
    url: '/addcitygarbagecapacity',
    method: 'post',
    data
  })
}
// 批量导入无害化处理量信息
export function addcitygarbagevolume(data) {
  return request({
    url: '/addcitygarbagevolume',
    method: 'post',
    data
  })
}
// 批量导入城市经济信息
export function addcityeconomydata(data) {
  return request({
    url: '/addcityeconomy',
    method: 'post',
    data
  })
}

// 批量导入城市生活垃圾信息
export function addgarbagecity(data) {
  return request({
    url: '/addbatchgarbagecity',
    method: 'post',
    data
  })
}

// 批量导入城市人口信息
export function addcitypopulationdata(data) {
  return request({
    url: '/addcitypopulation',
    method: 'post',
    data
  })
}
// 请求城市经济表
export function getcityeconomydata() {
  return request({
    url: '/geteconomycity',
    method: 'get'
  })
}
// 请求城市人口表
export function getcitypopulationdata() {
  return request({
    url: '/getpopulationcity',
    method: 'get'
  })
}
// 请求城市生活垃圾表
export function getcitygarbagedata() {
  return request({
    url: '/getgarbagecity',
    method: 'get'
  })
}
// 请求城市无害化处理厂表
export function getcitygarbagedealdata() {
  return request({
    url: '/getgarbagedealcity',
    method: 'get'
  })
}
// 请求城市无害化处理能力表
export function getcitygarbagecapacitydata() {
  return request({
    url: '/getgarbagecapacitycity',
    method: 'get'
  })
}
// 请求城市无害化处理量表
export function getcitygarbagevolumdata() {
  return request({
    url: '/getgarbagevolumecity',
    method: 'get'
  })
}

// 修改城市经济信息
export function amendcityeconomydata(data) {
  return request({
    url: '/amendcityeconomydata',
    method: 'post',
    data
  })
}

// 删除城市经济信息
export function deletecityeconomydata(data) {
  return request({
    url: '/deletecityeconomydata',
    method: 'post',
    data
  })
}
// 修改城市人口信息
export function amendcitypopulationdata(data) {
  return request({
    url: '/amendcitypopulationdata',
    method: 'post',
    data
  })
}
// 删除城市人口信息
export function deletecitypopulationdata(data) {
  return request({
    url: '/deletecitypopulationdata',
    method: 'post',
    data
  })
}
// 修改城市生活垃圾信息
export function amendcitygarbagedata(data) {
  return request({
    url: '/amendcitygarbagedata',
    method: 'post',
    data
  })
}
// 删除城市生活垃圾信息
export function deletecitygarbagedata(data) {
  return request({
    url: '/deletecitygarbagedata',
    method: 'post',
    data
  })
}
// 修改城市无害化处理厂信息
export function amendcitygarbagedealdata(data) {
  return request({
    url: '/amendcitygarbagedealdata',
    method: 'post',
    data
  })
}
// 删除城市无害化处理厂信息
export function deletecitygarbagedealdata(data) {
  return request({
    url: '/deletecitygarbagedealdata',
    method: 'post',
    data
  })
}
// 修改城市无害化处理能力信息
export function amendcitygarbagecapacitydata(data) {
  return request({
    url: '/amendcitygarbagecapacitydata',
    method: 'post',
    data
  })
}
// 删除城市无害化处理能力信息
export function deletecitygarbagecapacitydata(data) {
  return request({
    url: '/deletecitygarbagecapacitydata',
    method: 'post',
    data
  })
}
// 修改城市无害化处理量信息
export function amendcitygarbagevolumedata(data) {
  return request({
    url: '/amendcitygarbagevolumedata',
    method: 'post',
    data
  })
}
// 删除城市无害化处理量信息
export function deletecitygarbagevolumedata(data) {
  return request({
    url: '/deletecitygarbagevolumedata',
    method: 'post',
    data
  })
}

export function getcitygarbage() {
  return request({
    url: '/getgarbagecity',
    method: 'get'
  })
}
// 添加一条城市经济表数据
export function addsinglerowdata(data) {
  return request({
    url: '/addsinglerowdata',
    method: 'post',
    data
  })
}
// 添加一条城市人口表数据
export function addsinglepopulation(data) {
  return request({
    url: '/addsinglepopulation',
    method: 'post',
    data
  })
}
// 添加一条城市生活垃圾表数据
export function addsinglegarbage(data) {
  return request({
    url: '/addsinglegarbage',
    method: 'post',
    data
  })
}
// 添加一条城市无害化处理厂信息
export function addsingledealgarbage(data) {
  return request({
    url: '/addsingledealgarbage',
    method: 'post',
    data
  })
}
// 添加一条城市无害化处理能力表数据
export function addsinglecapacitygarbage(data) {
  return request({
    url: '/addsinglecapacitygarbage',
    method: 'post',
    data
  })
}
// 添加一条城市无害化处理量表数据
export function addsinglevolumegarbage(data) {
  return request({
    url: '/addsinglevolumegarbage',
    method: 'post',
    data
  })
}
// 添加一个p_median项目
export function addpmedianproject(data) {
  return request({
    url: '/addpmedianproject',
    method: 'post',
    data
  })
}
// 导入basic表
export function addbasic(data) {
  return request({
    url: '/addbasic',
    method: 'post',
    data
  })
}
// 导入ts表
export function addts(data) {
  return request({
    url: '/addts',
    method: 'post',
    data
  })
}
// 导入rrc表
export function addrrc(data) {
  return request({
    url: '/addrrc',
    method: 'post',
    data
  })
}
// 导入cost_matrix表
export function addcostmatrix(data) {
  return request({
    url: '/addcostmatrix',
    method: 'post',
    data
  })
}
// 请求p_median项目
export function getpmedianproject() {
  return request({
    url: '/getpmedianproject',
    method: 'get'
  })
}
// 修改p_median项目
export function amendpmedianproject(data) {
  return request({
    url: '/amendpmedianproject',
    method: 'post',
    data
  })
}
// 集散厂优化
export function getplotlocation(data) {
  return request({
    url: '/startpmedianproject',
    method: 'post',
    data
  })
}
// 爬取国内空气污染数据
export function getnationpm(data) {
  return request({
    url: '/getnationpm',
    method: 'post',
    data
  })
}
// 爬取国内水体污染数据
export function getnationwaterpollution(data) {
  return request({
    url: '/getnationwaterpollution',
    method: 'post',
    data
  })
}
// 爬取国内固体废弃物数据
export function getnationsolidpollution(data){
  return request({
    url: '/getnationsolidpollution',
    method: 'post',
    data
  })
}
// 爬取世界空气污染数据
export function getworldpm(data){
  return request({
    url: '/getworldpm',
    method: 'post',
    data
  })
}
//获取爬虫爬取记录
export function getCrawlDataRecord(type) {
  return request({
    url:'/getcrawlrecord',
    method: 'get',
    params: { type }
  })
}
//删除已爬取文件
export function deleteCrawlData(id) {
  return request({
    url:'/deletecrawldata',
    method:'get',
    params: { id }
  })
}
//筛选爬虫历史记录
export function selectCrawlRecord(query) {
  return request({
    url: '/getcrawl_select',
    method: 'get',
    params: query
  })
}
//获取LSTM项目
export function getLstmProject() {
  return request({
    url: '/getlstmproject',
    method: 'get',

  })
}
//添加LSTM项目
export function addLstmProject(data) {
  return request({
    url: '/addlstmproject',
    method: 'POST',
    data
  })
}

//修改LSTM项目
export function amendLstmProject(data) {
  return request({
    url: '/amendlstmproject',
    method:'post',
    data
  })
}

//LSTM项目开始模型实验
export function LstmProjectStart(data) {
  return request({
    url: '/experiment_lstm_start',
    method: 'post',
    data
  })
}

// 获取lstm项目编号
export function lstmprojectid() {
  return request({
    url: '/lstm_project_id',
    method: 'get'
  })
}

// 获取lstm参数表
export function getlstmparameter(data){
  return request({
    url: '/get_parameter_lstm',
    method: 'get',
    params: data
  })
}

// 批量导入lstm数据
export function inputlstmparameter(data){
  return request({
    url: '/input_parameter_lstm',
    method: 'post',
    data
  })
}

// 获取lstm实验结果
export function getlstmresult(data){
  return request({
    url: '/get_lstm_result',
    method: 'get',
    params: data
  })
}

// 获取多元回归项目
export function getregression(){
  return request({
    url: '/get_regression',
    method: 'get'
  })
}

// 添加多元回归项目
export function addregression(data){
  return request({
    url: '/add_regression',
    method: 'post',
    data
  })
}

// 修改多元回归模型
export function amendregression(data){
  return request({
    url: '/amend_regression',
    method: 'post',
    data
  })
}

// 获得多元回归项目编号
export function regressionid(){
  return request({
    url: '/get_id_regression',
    method: 'get'
  })
}

// 批量导入多元回归参数
export function inputregressionparameter(data){
  return request({
    url: '/add_parameter_regression',
    method: 'post',
    data
  })
}

// 获得多元回归参数列表
export function getregressionpara(data){
  return request({
    url: '/get_parameter_regression',
    method: 'get',
    params: data
  })
}

// 开始多元回归实验
export function  startregression(data) {
  return request({
    url: '/start_regression_experiment',
    method: 'post',
    data
  })
}

// 获取多元回归实验结果
export function getregressionresult(data){
  return request({
    url: '/get_result_regression',
    method: 'get',
    params: data
  })
}

// 添加kmeans算法模型
export function addkmeansproject(data){
  return request({
    url: '/add_kmeans_project',
    method: 'post',
    data
  })
}

// 获得kmeans模型
export function getkmeansrpoject(){
  return request({
    url: '/get_kmeans_project',
    method: 'get'
  })
}

// 修改kmeans模型
export function amendkmeansproject(data){
  return request({
    url: '/amend_kmeans_project',
    method: 'post',
    data
  })
}

// 开始kmeans试验
export function startkmeans(data){
  return request({
    url: '/start_kmeans',
    method: 'post',
    data
  })
}

// 获得kmeans实验结果
export function getkmeansresult(data){
  return request({
    url: '/get_result_kmeans',
    method: 'get',
    params: data
  })
}

// 获得kmeans实验项目编号
export function getidlistkmeans(){
  return request({
    url: '/get_id_kmeans',
    method: 'get'
  })
}

// 输入kmeans实验数据
export function parameterkmeans(data){
  return request({
    url: '/input_parameter_kmeans',
    method: 'post',
    data
  })
}

export function getparameterkmeans(data){
  return request({
    url: '/get_parameter_kmeans',
    method: 'get',
    params: data
  })
}

// 获取算法模型列表
export function getalgorithmlist(data){
  return request({
    url: '/get_algorithm_list',
    method: 'get',
    params: data
  })
}

// 添加算法模型列表
export function addalgorithmlist(data){
  return request({
    url: '/add_algorithm_list',
    method: 'post',
    data
  })
}

// 删除算法模型列表
export function deletealgorithmlist(data){
  return request({
    url: '/delete_algorithm_list',
    method: 'post',
    data
  })
}

// 添加关联分析模型
export function addrelationproject(data){
  return request({
    url: '/add_relation_project',
    method: 'post',
    data
  })
}

// 获得关联分析模型
export function getrelationproject(){
  return request({
    url: '/get_relation_project',
    method: 'get'
  })
}

// 修改关联分析项目信息
export function amendrelationproject(data){
  return request({
    url: '/amend_relation_project',
    method: 'post',
    data
  })
}

// 获取关联分析项目编号
export function getidrelation(){
  return request({
    url: '/get_id_relation',
    method: 'get'
  })
}

// 获取关联分析项目参数
export function getparameterrelation(){
  return request({
    url: '/get_relation_parameter',
    method: 'get'
  })
}

// 导入关联分析参数
export function inputrelationparameter(data){
  return request({
    url: '/input_relation_parameter',
    method: 'post',
    data
  })
}

// 开始运行关联分析模型
export function startrelation(data){
  return request({
    url: '/start_relation',
    method: 'post',
    data
  })
}

// 获取关联分析混淆矩阵
export function getrelationhotmatrix(data){
  return request({
    url: '/get_relation_hot_matrix_result',
    method: 'get',
    params: data
  })
}

// 获得关联分析随机森林结果
export function getrelationrf(data){
  return request({
    url: '/get_relation_rf_result',
    method: 'get',
    params: data
  })
}

// 批量导入垃圾成分表
export function addelementgarbage(data){
  return request({
    url: '/add_element_garbage',
    method: 'post',
    data
  })
}

// 获取垃圾成分表数据
export function getgarbageelement(){
  return request({
    url: '/get_element_garbage',
    method: 'get'
  })
}

// 新增一条垃圾成分信息
export function addelementbyrow(data){
  return request({
    url: '/insert_element_garbage',
    method: 'post',
    data
  })
}

// 删除一条垃圾成分信息
export function deleteelementgarbage(data){
  return request({
    url: '/delete_element_garbage',
    method: 'post',
    data
  })
}

// 修改一条垃圾成分信息
export function amendelementgarbage(data){
  return request({
    url: '/amend_element_garbage',
    method: 'post',
    data
  })
}

// 获取算法ID列表
export function algorithmlidlist(data){
  return request({
    url: '/get_idlist_algorithm',
    method: 'post',
    data
  })
}

// 根据ID获取算法模型
export function getbyidalgorithm(data){
  return request({
    url: '/getbyid_algorithm',
    method: 'post',
    data
  })
}

// 获取所有模型列表
export function getallmodels(){
  return request({
    url: '/getallmodels',
    method: 'get'
  })
}

// 保存模型
export function savemodels(data){
  return request({
    url: '/savemodel',
    method: 'post',
    data
  })
}

// 根据类型筛选模型
export function filtermodels(data){
  return request({
    url: '/filtermodels',
    method: 'post',
    data
  })
}

// 获取特定用户和算法下的模型列表
export function getmodelconstruction(data){
  return request({
    url: '/get_model_construction',
    method: 'get',
    params: data
  })
}

// 获取指定模型信息
export function getinfomodel(data){
  return request({
    url: '/model_message',
    method: 'get',
    params: data
  })
}

// 增加特定算法中的模型
export function addselectmodel(data){
  return request({
    url: '/select_model_add',
    method: 'post',
    data
  })
}

// 删除特定算法中的模型
export function deleteselectmodel(data){
  return request({
    url: '/select_model_delete',
    method: 'post',
    data
  })
}

// 获取算法实验数据
export function algorithmtestinfo(data){
  return request({
    url: '/algorithmtest',
    method: 'post',
    data
  })
}

// 获取算法文件列表
export function getfilelist(data){
  return request({
    url: '/getdatafilelist',
    method: 'get'
  })
}

// 获取excel表信息
export function getexcelinfo(data){
  return request({
    url: '/getexceldetail',
    method: 'get',
    params: data
  })
}

// 组合模型关联分析处理
export function grouptestrelation(data){
  return request({
    url: '/grouptest_relation',
    method: 'post',
    data
  })
}

// 批量导入危险垃圾处置表
export function adddangerousgarbage(data){
  return request({
    url: '/adddangerousgarbagecity',
    method: 'post',
    data
  })
}

// 获取危险垃圾处置表信息
export function getdangerousgarbage(){
  return request({
    url: '/getdangerousgarbage',
    method: 'get'
  })
}

// 修改危险垃圾处置表信息
export function amenddangerousgarbage(data){
  return request({
    url: '/amenddangerousgarbage',
    method: 'post',
    data
  })
}

// 删除危险垃圾处置信息
export function deletedangeroudgarbage(data){
  return request({
    url: '/deletedangerousgarbage',
    method: 'post',
    data
  })
}

// 添加危险垃圾处置信息
export function addbyrowdangerousgarbage(data){
  return request({
    url: '/addbyrow_dangerousgarbage',
    method: 'post',
    data
  })
}

// 批量导入垃圾日均清运量信息
export function addgarbageclearperday(data){
  return request({
    url: '/addgarbageclear',
    method: 'post',
    data
  })
}

// 获取到所有垃圾日均清运量信息
export function getgarbageclearperday(){
  return request({
    url: '/getgarbageclearperday',
    method: 'get'
  })
}

// 修改垃圾日均清运量
export function amendgarbageclearperday(data){
  return request({
    url: '/amendgarbageclearperday',
    method: 'post',
    data
  })
}

// 删除垃圾日均清运量
export function deletegarbageclearperday(data){
  return request({
    url: '/deletegarbageclearperday',
    method: 'post',
    data
  })
}

// 新增一条垃圾清运量数据
export function addgarbageclearbyrow(data){
  return request({
    url: '/addsinglerowforgarbageclear',
    method: 'post',
    data
  })
}

// 根据用户获取多元回归运行结果
export function getrelationexcelresult(data){
  return request({
    url: '/getrelationexcelresult',
    method: 'get',
    params: data
  })
}

// 删除多元回归运行结果文件
export function deleterelationexcelresult(data){
  return request({
    url: '/deleterelationexcel',
    method: 'post',
    data
  })
}

// 批量导入城镇垃圾产量表
export function inputgarbagecountry(data){
  return request({
    url: '/inputgarbagecountry',
    method: 'post',
    data
  })
}

// 获取城镇垃圾产量表
export function getgarbagecountry(data){
  return request({
    url: '/getgarbagecountry',
    method: 'get',
    params: data
  })
}

// 修改城镇垃圾产量表
export function amendgarbagecountry(data){
  return request({
    url: '/amendgarbagecountry',
    method: 'post',
    data
  })
}

// 删除城镇垃圾产量表
export function deletegarbagecountry(data){
  return request({
    url: '/deletegarbagecountry',
    method: 'post',
    data
  })
}

// 增加城镇垃圾产量表
export function addgarbagecountry(data){
  return request({
    url: '/addgarbagecountry',
    method: 'post',
    data
  })
}

// 获取LSTM组合模型运算excel列表
export function getlstmexcelresult(data){
  return request({
    url: '/getlstmexcelresult',
    method: 'get',
    params: data
  })
}

// 获取区级经济信息表
export function geteconomydistrict(){
  return request({
    url: '/geteconomydistrict',
    method: 'get',
  })
}

// 批量导入区级经济信息表
export function inputeconomydistrict(data){
  return request({
    url: '/inputeconomydistrict',
    method: 'post',
    data
  })
}

// 修改区级经济信息表
export function amendeconomydistrict(data){
  return request({
    url: '/amendeconomydistrict',
    method: 'post',
    data
  })
}

// 删除区域经济信息表
export function deleteeconomydistrict(data){
  return request({
    url: '/deleteeconomydistrict',
    method: 'post',
    data
  })
}

// 添加一条区域经济信息表
export function addeconomydistrict(data){
  return request({
    url: '/addeconomydistrict',
    method: 'post',
    data
  })
}

// 筛选区域经济信息表
export function filtereconomydistrict(data){
  return request({
    url: '/filtereconomydistrict',
    method: 'post',
    data
  })
}


// 根据区域和年份筛选区域经济信息表
export function filterpieeconomydistrict(data){
  return request({
    url: '/filterPieeconomydistrict',
    method: 'post',
    data
  })
}

// 根据年份筛选区域经济信息
export function filterbareconomydistrict(data){
  return request({
    url: '/filterBareconomydistrict',
    method: 'get',
    params: data
  })
}

// 获取区域人口信息
export function getdistrictpopulation(){
  return request({
    url: '/getpopulationdistrict',
    method: 'get'
  })
}

// 修改人口区域信息表
export function amenddistrictpopulation(data){
  return request({
    url: '/amendpopulationdistrict',
    method: 'post',
    data
  })
}

// 添加区域人口信息
export function adddistrictpopulation(data){
  return request({
    url: '/addpopulationdistrict',
    method: 'post',
    data
  })
}

// 批量导入区域人口信息表
export function inputdistrictpopulation(data){
  return request({
    url: '/inputpopulationdistrict',
    method: 'post',
    data
  })
}

// 删除人口区域信息表
export function deletedistrictpopulation(data){
  return request({
    url: '/deletepopulationdistrict',
    method: 'post',
    data
  })
}

// 根据地区筛选人口数据
export function filterlinepopulationdistrict(data){
  return request({
    url: '/filterlinepopulationdistrict',
    method: 'get',
    params: data
  })
}

// 根据年份筛选人口数据
export function filterbarpopulationdistrict(data){
  return request({
    url: '/filterbarpopulationdistrict',
    method: 'get',
    params: data
  })
}

// 获取多元回归excel结果文件
export function getregressionexcelresult(data){
  return request({
    url: '/getregressionexcelresult',
    method:'get',
    params: data
  })
}

// 删除多元回归excel结果文件
export function deleteregressionexcelresult(data){
  return request({
    url: '/deleteregressionexcelresult',
    method: 'post',
    data
  })
}

// 开始kmeans算法
export function grouptestkmeans(data){
  return request({
    url: '/startgrouptestkmeans',
    method: 'post',
    data
  })
}

// 获取kmeansexcel结果
export function getkmeansexcelresult(data){
  return request({
    url: '/getkmeansexcelresult',
    method: 'get',
    params: data
  })
}

// 获取多元线性回归项目
export function getlinearregressionproject(){
  return request({
    url: '/getlinearregressionproject',
    method: 'get',
  })
}

// 添加多元线性回归项目
export function addlinearregressionproject(data){
  return request({
    url: '/addlinearregressionproject',
    method: 'post',
    data
  })
}

// 修改多元线性回归
export function amendlinearregressionproject(data){
  return request({
    url: '/amendlinearregressionproject',
    method: 'post',
    data
  })
}

// 获取多元线性回归Id
export function getlinearregressionidlist(){
  return request({
    url: '/getlinearregressionidlist',
    method: 'get'
  })
}

// 添加多元线性回归参数
export function addlinearregressionparameter(data){
  return request({
    url: '/addlinearregressionparameter',
    method: 'post',
    data
  })
}

// 获取多元线性回归参数
export function getlinearregressionparameter(data){
  return request({
    url: '/getlinearregressionparameter',
    method: 'get',
    params: data
  })
}

// 开始多元线性回归实验
export function startlinearregressionexperiment(data){
  return request({
    url: '/startlinearregressionexperiment',
    method: 'post',
    data
  })
}

// 获取多元线性回归结果
export function getlinearregressionresult(data){
  return request({
    url: '/getlinearregressionresult',
    method: 'get',
    params: data
  })
}

// 获取关联分析灰色关联度结果
export function getgreyrelationresult(data){
  return request({
    url: '/get_grey_relation_result',
    method: 'get',
    params: data
  })
}

// 获取皮尔逊系数结果
export function getpearsonrelationresult(data){
  return request({
    url: '/get_pearson_result',
    method: 'get',
    params: data
  })
}

// 获取相关指标
export function getlinearregressiontestreport(data){
  return request({
    url: '/getlinearregressiontestreport',
    method: 'get',
    params: data
  })
}

// 获取多元非线性模型指标
export function getregressionreport(data){
  return request({
    url: '/getregressionreport',
    method: 'get',
    params: data
  })
}

// 获取sltm模型实验报告
export function getlstmreport(data){
  return request({
    url: '/getlstmreport',
    method: 'get',
    params: data
  })
}

// 批量导入区域固废信息表
export function inputgarbagedistrict(data){
  return request({
    url: '/add_garbage_district',
    method: 'post',
    data
  })
}

// 获取区域固废信息表
export function getgarbagedistrict(data){
  return request({
    url: '/get_garbage_district',
    method: 'get',
    params: data
  })
}

// 修改区域固废信息表
export function amendgarbagedistrict(data){
  return request({
    url: '/amendgarbagedistrict',
    method: 'post',
    data
  })
}

// 添加单行区域固废信息
export function addbyrowgarbagedistrict(data){
  return request({
    url: '/addbyrowgarbagedistrict',
    method: 'post',
    data
  })
}

// 删除区域固废信息
export function deletegarbagedistrict(data){
  return request({
    url: '/deletegarbagedistrict',
    method: 'post',
    data
  })
}

// 根据年份筛选区域固废信息
export function filtergarbagedistrictbyyear(data){
  return request({
    url: '/filtergarbagedistrictbyyear',
    method: 'get',
    params: data
  })
}

// 获取kmeans聚类报告
export function getkmenastestreport(data){
  return request({
    url: '/get_kmeans_testreport',
    method: 'get',
    params: data
  })
}