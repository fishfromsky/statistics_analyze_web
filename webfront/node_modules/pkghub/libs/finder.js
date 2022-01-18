import fs from 'fs'
import path from 'path'
import glob from 'glob'

export function split(name, isFilename) {
  if (!name || name.indexOf('/') === -1) 
    return
  if (!isFilename) 
    return name.substr(0, name.indexOf('/'))

  return name.substr(name.indexOf('/') + 1)
}

// 使用 glob 模糊匹配
export function read(abs, name) {
  if (!abs) 
    return null

  var dir = path.join(abs, name)
  var file = {
    name,
    dir,
    exist: fs.existsSync(dir)
  }

  if (file.exist) 
    return file

  try {
    file.availables = glob.sync(file.dir + '*')
  } catch (err) {
    file.err = err
  }

  return file
}
