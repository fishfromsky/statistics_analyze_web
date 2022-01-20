import npm from 'npm'
import _ from 'underscore'
import Promise from 'bluebird'

const config = {
  loglevel: 'silent',
  parseable: true
}

export function load() {
  return new Promise((res, rej) => {
    npm.load(config, (err, n) => {
      if (err)
        return rej(err)

      return res(n)
    })
  })
}

export function ls() {
  return load().then(npmInstance => {
    return new Promise((res, rej) => {
      npmInstance.commands.ls([], true, (err, modules) => {
        if (err)
          return rej(err)

        return res(modules)
      })
    })
  })
}

export function install(modules, dir) {
  return load().then(n => {
    return new Promise((res, rej) => {
      if (!_.isArray(modules)) 
        return rej(new Error('Modules name must be array'))

      const params = dir ? 
        [ dir, modules, callback ] : 
        [ modules, callback ];

      return n.commands.install.apply(n, params)

      function callback(err, result) {
        if (err)
          return rej(err)

        return res(result)
      }
    })
  })
}
