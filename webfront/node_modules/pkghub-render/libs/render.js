import pkghub from 'pkghub'
import Promise from 'bluebird'
import compile from './compile'

/**
*
* A wrapper function for rendering html string by given template and data,
* Support mutilple view engines.
*
* @param {String} [template] [template's short name]
* @example
*   exports.render('mails-flat/message', {...});
*
**/
export default function renderer(template, data) {
  const hub = new pkghub

  return hub.load(template)
    .then(({ module, file }) => {
      if (!module) 
        return Promise.reject(new Error('Target theme module was not found'))
      if (!module['view engine']) 
        return Promise.reject(new Error('Template engine in `package.json` was required'))
      if (!file) 
        return Promise.reject(new Error('Template file was not found'))

      // Select the first file when template file does not exist.
      const dest = file.exist ? file.dir : file.availables[0]

      // Inject `THEME` locals
      data.THEME = module
      // Replace #{static} in template with real public path.
      data.static = isURI(module.static) ? 
        module.static : 
        '/' + module.name;

      return compile(dest, data, {
        engine: module['view engine']
      })
    })
}

function isURI(dir) {
  return dir && (dir.indexOf('http') === 0 || dir.indexOf('https') === 0)
}
