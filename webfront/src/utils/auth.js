import Cookies from 'js-cookie'

const TokenKey = 'environment_token'
const IDKey = 'environment_id'
const RoleKey = 'environment_role'
const nameKey = 'environment_name'


export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function setRole(role) {
  return Cookies.set(RoleKey, role)
}

export function getRole() {
  return Cookies.get(RoleKey)
}

export function removeRole() {
  return Cookies.remove(RoleKey)
}

export function setId(Id) {
  return Cookies.set(IDKey, Id)
}

export function getId() {
  return Cookies.get(IDKey)
}

export function removeId() {
  return Cookies.remove(IDKey)
}

export function setName(name) {
  return Cookies.set(nameKey, name)
}

export function getName() {
  return Cookies.get(nameKey)
}
