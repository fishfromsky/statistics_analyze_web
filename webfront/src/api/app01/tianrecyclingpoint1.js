import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/tianrecyclingpoint1/list',
    method: 'get',
    params: query
  })
}

export function fetchtianrecyclingpoint1(id) {
  return request({
    url: '/api/tianrecyclingpoint1/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/tianrecyclingpoint1/pv',
    method: 'get',
    params: { pv }
  })
}

export function createtianrecyclingpoint1(data) {
  return request({
    url: '/api/tianrecyclingpoint1/create',
    method: 'post',
    data
  })
}

export function updatetianrecyclingpoint1(data) {
  return request({
    url: '/api/tianrecyclingpoint1/update',
    method: 'post',
    data
  })
}
export function deletetianrecyclingpoint1(data) {
  return request({
    url: '/api/tianrecyclingpoint1/delete',
    method: 'post',
    data
  })
}

export function downloadtianrecyclingpoint1(query) {
  return request({
    url: '/api/tianrecyclingpoint1/download',
    method: 'get',
    params: query
  })
}

export function uploadtianrecyclingpoint1(data) {
  return request({
    url: '/api/tianrecyclingpoint1/upload',
    method: 'post',
    data
  })
}

export function cleartianrecyclingpoint1(data) {
  return request({
    url: '/api/tianrecyclingpoint1/clear',
    method: 'post',
    data
  })
}
