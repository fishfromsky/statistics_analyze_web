import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/article2/list',
    method: 'get',
    params: query
  })
}

export function fetcharticle2(id) {
  return request({
    url: '/api/article2/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/article2/pv',
    method: 'get',
    params: { pv }
  })
}

export function createarticle2(data) {
  return request({
    url: '/api/article2/create',
    method: 'post',
    data
  })
}

export function updatearticle2(data) {
  return request({
    url: '/api/article2/update',
    method: 'post',
    data
  })
}
export function deletearticle2(data) {
  return request({
    url: '/api/article2/delete',
    method: 'post',
    data
  })
}

export function downloadarticle2(query) {
  return request({
    url: '/api/article2/download',
    method: 'get',
    params: query
  })
}

export function uploadarticle2(data) {
  return request({
    url: '/api/article2/upload',
    method: 'post',
    data
  })
}

export function cleararticle2(data) {
  return request({
    url: '/api/article2/clear',
    method: 'post',
    data
  })
}
