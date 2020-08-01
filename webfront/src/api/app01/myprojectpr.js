import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/myprojectpr/list',
    method: 'get',
    params: query
  })
}

export function fetchmyprojectpr(id) {
  return request({
    url: '/api/myprojectpr/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/myprojectpr/pv',
    method: 'get',
    params: { pv }
  })
}

export function createmyprojectpr(data) {
  return request({
    url: '/api/myprojectpr/create',
    method: 'post',
    data
  })
}

export function updatemyprojectpr(data) {
  return request({
    url: '/api/myprojectpr/update',
    method: 'post',
    data
  })
}
export function deletemyprojectpr(data) {
  return request({
    url: '/api/myprojectpr/delete',
    method: 'post',
    data
  })
}

export function downloadmyprojectpr(query) {
  return request({
    url: '/api/myprojectpr/download',
    method: 'get',
    params: query
  })
}

export function uploadmyprojectpr(data) {
  return request({
    url: '/api/myprojectpr/upload',
    method: 'post',
    data
  })
}

export function clearmyprojectpr(query) {
  return request({
    url: '/api/myprojectpr/clear',
    method: 'post',
    params: query
  })
}
