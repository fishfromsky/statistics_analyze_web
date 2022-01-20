import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/pmediants/list',
    method: 'get',
    params: query
  })
}

export function fetchpmediants(id) {
  return request({
    url: '/api/pmediants/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/pmediants/pv',
    method: 'get',
    params: { pv }
  })
}

export function createpmediants(data) {
  return request({
    url: '/api/pmediants/create',
    method: 'post',
    data
  })
}

export function updatepmediants(data) {
  return request({
    url: '/api/pmediants/update',
    method: 'post',
    data
  })
}
export function deletepmediants(data) {
  return request({
    url: '/api/pmediants/delete',
    method: 'post',
    data
  })
}

export function downloadpmediants(query) {
  return request({
    url: '/api/pmediants/download',
    method: 'get',
    params: query
  })
}

export function uploadpmediants(data) {
  return request({
    url: '/api/pmediants/upload',
    method: 'post',
    data
  })
}

export function clearpmediants(query) {
  return request({
    url: '/api/pmediants/clear',
    method: 'post',
    params: query
  })
}
