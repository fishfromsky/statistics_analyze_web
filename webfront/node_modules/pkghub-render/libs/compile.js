import Promise from 'bluebird'

/**
*
* Render html string by given tempate and data
* Built-in template engine: ['swig']
*
* @param {String(Path)} [template] [the template abs path]
* @param {Object} [data] [the template locals]
* @param {Object} [engine] [the view engine's object, contains `engine.name`, `engine._engine`]
*
**/
export default function(template, data = {}, opts = { engine: 'swig' }) {
  return new Promise((res, rej) => {
    const engine = opts.engine
    
    try {
      const _engine = require(engine)
      var html

      if (engine === 'jade') 
        html = _engine.renderFile(template, data)
      if (engine === 'swig') 
        html = _engine.compileFile(template)(data)
      if (engine === 'ejs') 
        html = _engine.render(require('fs').readFileSync(template), data)

      if (!html)
        return rej(new Error('Template engine is not supported yet'))
      // Errors come from view engine
      if (typeof(html) === 'object')
        return rej(html)

      res(html)
    } catch (err) {
      return rej(err)
    }
  })
}
