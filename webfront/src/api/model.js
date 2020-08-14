import request from '@/utils/request'
import da from 'element-ui/src/locale/lang/da'

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
    url: '/getplotlocation',
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
//LSTM项目模型实验
export function LstmProjectStart(data) {
  return request({
    url: '/lstmprojectstart',
    method: 'post',
    data
  })
}


