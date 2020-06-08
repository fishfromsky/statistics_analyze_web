import request from '@/utils/request'
import da from "element-ui/src/locale/lang/da";

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

export function addcityeconomydata(data) {
  return request({
    url: '/addcityeconomy',
    method: 'post',
    data
  })
}

export function addcitypopulationdata(data){
  return request({
    url: '/addcitypopulation',
    method: 'post',
    data
  })
}

export function getcityeconomydata(){
  return request({
    url: '/geteconomycity',
    method: 'get'
  })
}


export function getcitypopulationdata(){
  return request({
    url: '/getpopulationcity',
    method: 'get'
  })
}

export function amendcityeconomydata(data){
  return request({
    url: '/amendcityeconomydata',
    method: 'post',
    data
  })
}

export function deletecityeconomydata(data){
  return request({
    url: '/deletecityeconomydata',
    method: 'post',
    data
  })
}

export function addgarbagecity(data){
  return request({
    url: '/addbatchgarbagecity',
    method: 'post',
    data
  })
}

export function getcitygarbage(){
  return request({
    url: '/getgarbagecity',
    method: 'get'
  })
}