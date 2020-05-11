import request from '@/utils/request'

export function getfactory() {
  return request({
    url: '/getfactorylist',
    method: 'get'
  })
}

export function getfactorybyid(data) {
  return request({
    url: '/getfactorybyid',
    method: 'get',
    params: data
  })
}

