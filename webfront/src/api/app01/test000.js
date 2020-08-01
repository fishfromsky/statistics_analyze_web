import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/test000/list',
    method: 'get',
    params: query
  })
}

export function fetchtest000(id) {
  return request({
    url: '/api/test000/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/test000/pv',
    method: 'get',
    params: { pv }
  })
}

export function createtest000(data) {
  return request({
    url: '/api/test000/create',
    method: 'post',
    data
  })
}

export function updatetest000(data) {
  return request({
    url: '/api/test000/update',
    method: 'post',
    data
  })
}
export function deletetest000(data) {
  return request({
    url: '/api/test000/delete',
    method: 'post',
    data
  })
}

export function downloadtest000(query) {
  return request({
    url: '/api/test000/download',
    method: 'get',
    params: query
  })
}

export function uploadtest000(data) {
  return request({
    url: '/api/test000/upload',
    method: 'post',
    data
  })
}

export function cleartest000(data) {
  return request({
    url: '/api/test000/clear',
    method: 'post',
    data
  })
}
