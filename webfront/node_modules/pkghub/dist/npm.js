'use strict';

var _interopRequireWildcard = function (obj) { return obj && obj.__esModule ? obj : { 'default': obj }; };

Object.defineProperty(exports, '__esModule', {
  value: true
});
exports.load = load;
exports.ls = ls;
exports.install = install;

var _npm = require('npm');

var _npm2 = _interopRequireWildcard(_npm);

var _import = require('underscore');

var _import2 = _interopRequireWildcard(_import);

var _Promise = require('bluebird');

var _Promise2 = _interopRequireWildcard(_Promise);

var config = {
  loglevel: 'silent',
  parseable: true
};

function load() {
  return new _Promise2['default'](function (res, rej) {
    _npm2['default'].load(config, function (err, n) {
      if (err) return rej(err);

      return res(n);
    });
  });
}

function ls() {
  return load().then(function (npmInstance) {
    return new _Promise2['default'](function (res, rej) {
      npmInstance.commands.ls([], true, function (err, modules) {
        if (err) return rej(err);

        return res(modules);
      });
    });
  });
}

function install(modules, dir) {
  return load().then(function (n) {
    return new _Promise2['default'](function (res, rej) {
      if (!_import2['default'].isArray(modules)) return rej(new Error('Modules name must be array'));

      var params = dir ? [dir, modules, callback] : [modules, callback];

      return n.commands.install.apply(n, params);

      function callback(err, result) {
        if (err) {
          return rej(err);
        }return res(result);
      }
    });
  });
}
//# sourceMappingURL=npm.js.map