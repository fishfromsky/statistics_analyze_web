import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/dianoutputbuilds/list',
    method: 'get',
    params: query
  })
}

export function fetchdianoutputbuilds(id) {
  return request({
    url: '/api/dianoutputbuilds/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/dianoutputbuilds/pv',
    method: 'get',
    params: { pv }
  })
}

export function createdianoutputbuilds(data) {
  return request({
    url: '/api/dianoutputbuilds/create',
    method: 'post',
    data
  })
}

export function updatedianoutputbuilds(data) {
  return request({
    url: '/api/dianoutputbuilds/update',
    method: 'post',
    data
  })
}
export function deletedianoutputbuilds(data) {
  return request({
    url: '/api/dianoutputbuilds/delete',
    method: 'post',
    data
  })
}

export function downloaddianoutputbuilds(query) {
  return request({
    url: '/api/dianoutputbuilds/download',
    method: 'get',
    params: query
  })
}

export function uploaddianoutputbuilds(data) {
  return request({
    url: '/api/dianoutputbuilds/upload',
    method: 'post',
    data
  })
}

export function cleardianoutputbuilds(query) {
  return request({
    url: '/api/dianoutputbuilds/clear',
    method: 'post',
    params: query
  })
}
