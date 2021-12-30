import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/pmedianbs/list',
    method: 'get',
    params: query
  })
}

export function fetchpmedianbs(id) {
  return request({
    url: '/api/pmedianbs/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/pmedianbs/pv',
    method: 'get',
    params: { pv }
  })
}

export function createpmedianbs(data) {
  return request({
    url: '/api/pmedianbs/create',
    method: 'post',
    data
  })
}

export function updatepmedianbs(data) {
  return request({
    url: '/api/pmedianbs/update',
    method: 'post',
    data
  })
}
export function deletepmedianbs(data) {
  return request({
    url: '/api/pmedianbs/delete',
    method: 'post',
    data
  })
}

export function downloadpmedianbs(query) {
  return request({
    url: '/api/pmedianbs/download',
    method: 'get',
    params: query
  })
}

export function uploadpmedianbs(data) {
  return request({
    url: '/api/pmedianbs/upload',
    method: 'post',
    data
  })
}

export function clearpmedianbs(query) {
  return request({
    url: '/api/pmedianbs/clear',
    method: 'post',
    params: query
  })
}
