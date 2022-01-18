'use strict';

var _interopRequireWildcard = function (obj) { return obj && obj.__esModule ? obj : { 'default': obj }; };

Object.defineProperty(exports, '__esModule', {
  value: true
});
exports.split = split;

// 使用 glob 模糊匹配
exports.read = read;

var _fs = require('fs');

var _fs2 = _interopRequireWildcard(_fs);

var _path = require('path');

var _path2 = _interopRequireWildcard(_path);

var _glob = require('glob');

var _glob2 = _interopRequireWildcard(_glob);

function split(name, isFilename) {
  if (!name || name.indexOf('/') === -1) {
    return;
  }if (!isFilename) {
    return name.substr(0, name.indexOf('/'));
  }return name.substr(name.indexOf('/') + 1);
}

function read(abs, name) {
  if (!abs) {
    return null;
  }var dir = _path2['default'].join(abs, name);
  var file = {
    name: name,
    dir: dir,
    exist: _fs2['default'].existsSync(dir)
  };

  if (file.exist) {
    return file;
  }try {
    file.availables = _glob2['default'].sync(file.dir + '*');
  } catch (err) {
    file.err = err;
  }

  return file;
}
//# sourceMappingURL=finder.js.map