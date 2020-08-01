import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/article1/list',
    method: 'get',
    params: query
  })
}

export function fetcharticle1(id) {
  return request({
    url: '/api/article1/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/article1/pv',
    method: 'get',
    params: { pv }
  })
}

export function createarticle1(data) {
  return request({
    url: '/api/article1/create',
    method: 'post',
    data
  })
}

export function updatearticle1(data) {
  return request({
    url: '/api/article1/update',
    method: 'post',
    data
  })
}
export function deletearticle1(data) {
  return request({
    url: '/api/article1/delete',
    method: 'post',
    data
  })
}

export function downloadarticle1(query) {
  return request({
    url: '/api/article1/download',
    method: 'get',
    params: query
  })
}

export function uploadarticle1(data) {
  return request({
    url: '/api/article1/upload',
    method: 'post',
    data
  })
}

export function cleararticle1(query) {
  return request({
    url: '/api/article1/clear',
    method: 'post',
    params: query
  })
}
