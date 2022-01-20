'use strict';

var _interopRequireWildcard = function (obj) { return obj && obj.__esModule ? obj : { 'default': obj }; };

Object.defineProperty(exports, '__esModule', {
  value: true
});

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
exports['default'] = renderer;

var _pkghub = require('pkghub');

var _pkghub2 = _interopRequireWildcard(_pkghub);

var _Promise = require('bluebird');

var _Promise2 = _interopRequireWildcard(_Promise);

var _compile = require('./compile');

var _compile2 = _interopRequireWildcard(_compile);

function renderer(template, data) {
  var hub = new _pkghub2['default']();

  return hub.load(template).then(function (_ref) {
    var module = _ref.module;
    var file = _ref.file;

    if (!module) return _Promise2['default'].reject(new Error('Target theme module was not found'));
    if (!module['view engine']) return _Promise2['default'].reject(new Error('Template engine in `package.json` was required'));
    if (!file) return _Promise2['default'].reject(new Error('Template file was not found'));

    // Select the first file when template file does not exist.
    var dest = file.exist ? file.dir : file.availables[0];

    // Inject `THEME` locals
    data.THEME = module;
    // Replace #{static} in template with real public path.
    data['static'] = isURI(module['static']) ? module['static'] : '/' + module.name;

    return _compile2['default'](dest, data, {
      engine: module['view engine']
    });
  });
}

function isURI(dir) {
  return dir && (dir.indexOf('http') === 0 || dir.indexOf('https') === 0);
}
module.exports = exports['default'];
//# sourceMappingURL=render.js.map