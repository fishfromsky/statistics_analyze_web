import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/pmediancstmtr/list',
    method: 'get',
    params: query
  })
}

export function fetchpmediancstmtr(id) {
  return request({
    url: '/api/pmediancstmtr/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/pmediancstmtr/pv',
    method: 'get',
    params: { pv }
  })
}

export function createpmediancstmtr(data) {
  return request({
    url: '/api/pmediancstmtr/create',
    method: 'post',
    data
  })
}

export function updatepmediancstmtr(data) {
  return request({
    url: '/api/pmediancstmtr/update',
    method: 'post',
    data
  })
}
export function deletepmediancstmtr(data) {
  return request({
    url: '/api/pmediancstmtr/delete',
    method: 'post',
    data
  })
}

export function downloadpmediancstmtr(query) {
  return request({
    url: '/api/pmediancstmtr/download',
    method: 'get',
    params: query
  })
}

export function uploadpmediancstmtr(data) {
  return request({
    url: '/api/pmediancstmtr/upload',
    method: 'post',
    data
  })
}

export function clearpmediancstmtr(query) {
  return request({
    url: '/api/pmediancstmtr/clear',
    method: 'post',
    params: query
  })
}
