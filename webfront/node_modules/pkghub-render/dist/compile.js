'use strict';

var _interopRequireWildcard = function (obj) { return obj && obj.__esModule ? obj : { 'default': obj }; };

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _Promise = require('bluebird');

var _Promise2 = _interopRequireWildcard(_Promise);

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

exports['default'] = function (template) {
  var data = arguments[1] === undefined ? {} : arguments[1];
  var opts = arguments[2] === undefined ? { engine: 'swig' } : arguments[2];

  return new _Promise2['default'](function (res, rej) {
    var engine = opts.engine;

    try {
      var _engine = require(engine);
      var html;

      if (engine === 'jade') html = _engine.renderFile(template, data);
      if (engine === 'swig') html = _engine.compileFile(template)(data);
      if (engine === 'ejs') html = _engine.render(require('fs').readFileSync(template), data);

      if (!html) return rej(new Error('Template engine is not supported yet'));
      // Errors come from view engine
      if (typeof html === 'object') return rej(html);

      res(html);
    } catch (err) {
      return rej(err);
    }
  });
};

module.exports = exports['default'];
//# sourceMappingURL=compile.js.map