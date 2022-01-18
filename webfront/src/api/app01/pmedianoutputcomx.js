import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/pmedianoutputcomx/list',
    method: 'get',
    params: query
  })
}

export function fetchpmedianoutputcomx(id) {
  return request({
    url: '/api/pmedianoutputcomx/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/pmedianoutputcomx/pv',
    method: 'get',
    params: { pv }
  })
}

export function fetchCost(project_id) {
  return request({
    url: '/api/pmedianoutputcomx/cost',
    method: 'get',
    params: { project_id }
  })
}

export function createpmedianoutputcomx(data) {
  return request({
    url: '/api/pmedianoutputcomx/create',
    method: 'post',
    data
  })
}

export function updatepmedianoutputcomx(data) {
  return request({
    url: '/api/pmedianoutputcomx/update',
    method: 'post',
    data
  })
}
export function deletepmedianoutputcomx(data) {
  return request({
    url: '/api/pmedianoutputcomx/delete',
    method: 'post',
    data
  })
}

export function downloadpmedianoutputcomx(query) {
  return request({
    url: '/api/pmedianoutputcomx/download',
    method: 'get',
    params: query
  })
}

export function uploadpmedianoutputcomx(data) {
  return request({
    url: '/api/pmedianoutputcomx/upload',
    method: 'post',
    data
  })
}

export function clearpmedianoutputcomx(query) {
  return request({
    url: '/api/pmedianoutputcomx/clear',
    method: 'post',
    params: query
  })
}
