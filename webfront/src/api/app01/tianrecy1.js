import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/tianrecy1/list',
    method: 'get',
    params: query
  })
}

export function fetchtianrecy1(id) {
  return request({
    url: '/api/tianrecy1/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/tianrecy1/pv',
    method: 'get',
    params: { pv }
  })
}

export function createtianrecy1(data) {
  return request({
    url: '/api/tianrecy1/create',
    method: 'post',
    data
  })
}

export function updatetianrecy1(data) {
  return request({
    url: '/api/tianrecy1/update',
    method: 'post',
    data
  })
}
export function deletetianrecy1(data) {
  return request({
    url: '/api/tianrecy1/delete',
    method: 'post',
    data
  })
}

export function downloadtianrecy1(query) {
  return request({
    url: '/api/tianrecy1/download',
    method: 'get',
    params: query
  })
}

export function uploadtianrecy1(data) {
  return request({
    url: '/api/tianrecy1/upload',
    method: 'post',
    data
  })
}

export function cleartianrecy1(data) {
  return request({
    url: '/api/tianrecy1/clear',
    method: 'post',
    data
  })
}
