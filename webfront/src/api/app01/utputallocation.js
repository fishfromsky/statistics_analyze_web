import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/utputallocation/list',
    method: 'get',
    params: query
  })
}

export function fetchall_list(query){
  return request({
    url: '/api/utputallocation/allist',
    method: 'get',
    params: query
  })
}

export function fetchutputallocation(id) {
  return request({
    url: '/api/utputallocation/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/api/utputallocation/pv',
    method: 'get',
    params: { pv }
  })
}

export function createutputallocation(data) {
  return request({
    url: '/api/utputallocation/create',
    method: 'post',
    data
  })
}

export function updateutputallocation(data) {
  return request({
    url: '/api/utputallocation/update',
    method: 'post',
    data
  })
}
export function deleteutputallocation(data) {
  return request({
    url: '/api/utputallocation/delete',
    method: 'post',
    data
  })
}

export function downloadutputallocation(query) {
  return request({
    url: '/api/utputallocation/download',
    method: 'get',
    params: query
  })
}

export function uploadutputallocation(data) {
  return request({
    url: '/api/utputallocation/upload',
    method: 'post',
    data
  })
}

export function clearutputallocation(query) {
  return request({
    url: '/api/utputallocation/clear',
    method: 'post',
    params: query
  })
}
