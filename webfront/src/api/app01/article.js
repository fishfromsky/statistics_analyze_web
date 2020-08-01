import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/article/list',
    method: 'get',
    params: query
  })
}

export function fetchArticle(id) {
  return request({
    url: '/api/article/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/article/pv',
    method: 'get',
    params: { pv }
  })
}

export function createArticle(data) {
  return request({
    url: '/api/article/create',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: '/api/article/update',
    method: 'post',
    data
  })
}

export function deleteArticle(data) {
  return request({
    url: '/api/article/delete',
    method: 'post',
    data
  })
}

export function downloadArticle(query) {
  return request({
    url: '/api/article/download',
    method: 'get',
    params: query
  })
}

export function uploadArticle(data) {
  return request({
    url: '/api/article/upload',
    method: 'post',
    data
  })
}

export function clearArticle(data) {
  return request({
    url: '/api/article/clear',
    method: 'post',
    data
  })
}
