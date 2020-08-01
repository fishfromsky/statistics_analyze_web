import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/pmedianreccen/list',
    method: 'get',
    params: query
  })
}

export function fetchpmedianreccen(id) {
  return request({
    url: '/api/pmedianreccen/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/pmedianreccen/pv',
    method: 'get',
    params: { pv }
  })
}

export function createpmedianreccen(data) {
  return request({
    url: '/api/pmedianreccen/create',
    method: 'post',
    data
  })
}

export function updatepmedianreccen(data) {
  return request({
    url: '/api/pmedianreccen/update',
    method: 'post',
    data
  })
}
export function deletepmedianreccen(data) {
  return request({
    url: '/api/pmedianreccen/delete',
    method: 'post',
    data
  })
}

export function downloadpmedianreccen(query) {
  return request({
    url: '/api/pmedianreccen/download',
    method: 'get',
    params: query
  })
}

export function uploadpmedianreccen(data) {
  return request({
    url: '/api/pmedianreccen/upload',
    method: 'post',
    data
  })
}

export function clearpmedianreccen(query) {
  return request({
    url: '/api/pmedianreccen/clear',
    method: 'post',
    params: query
  })
}
