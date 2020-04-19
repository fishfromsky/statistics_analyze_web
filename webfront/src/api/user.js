import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/info',
    method: 'get',
    params: { token }
  })
}

export function logout(token) {
  return request({
    url: '/logout',
    method: 'post',
    params: { token }
  })
}

export function getsuperuser() {
  return request({
    url: '/getsuperuser',
    method: 'get'
  })
}

export function fetchsuperuser(data) {
  return request({
    url: '/fetchsuperuser',
    method: 'get',
    params: data
  })
}

export function addsuperuser(data) {
  return request({
    url: '/addsuperuser',
    method: 'post',
    data
  })
}

export function deletesuperuser(data) {
  return request({
    url: '/deletesuperuser',
    method: 'get',
    params: data
  })
}
