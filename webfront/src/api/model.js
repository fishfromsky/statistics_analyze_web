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
