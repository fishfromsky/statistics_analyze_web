'use strict';

var _interopRequireWildcard = function (obj) { return obj && obj.__esModule ? obj : { 'default': obj }; };

var _classCallCheck = function (instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } };

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _import = require('underscore');

var _import2 = _interopRequireWildcard(_import);

var _Promise = require('bluebird');

var _Promise2 = _interopRequireWildcard(_Promise);

var _import3 = require('./npm');

var npm = _interopRequireWildcard(_import3);

var _import4 = require('./finder');

var finder = _interopRequireWildcard(_import4);

var defaults = {
  devider: '-',
  includes: ['name', 'version', 'logo', 'styles', 'fonts', 'javascripts', 'static', 'screenshot', 'description', 'main', 'repository', 'keywords', 'author', 'license', 'bugs', 'readme', 'path', 'depth', 'realPath', 'view engine']
};

var pkgHub = (function () {
  function pkgHub() {
    var devider = arguments[0] === undefined ? '-' : arguments[0];

    _classCallCheck(this, pkgHub);

    this.module = {};
    this.module.dependencies = {};
    this.settings = _import2['default'].clone(defaults);
    this.settings.devider = devider;
  }

  _createClass(pkgHub, [{
    key: 'config',
    value: function config() {
      var params = arguments[0] === undefined ? {} : arguments[0];

      this.settings = _import2['default'].extend(defaults, params);
      return this.settings;
    }
  }, {
    key: 'list',

    // 列出所有依赖模块
    value: function list() {
      var _this = this;

      return npm.ls().then(function (packages) {
        var modules = _import2['default'].clone(packages);
        var dependencies = modules.dependencies;

        if (dependencies) {
          delete modules.dependencies;

          _import2['default'].each(dependencies, function (module, name) {
            dependencies[name] = wash(module);
          });
        }

        modules = wash(modules);
        modules.dependencies = dependencies;

        _this.module = modules;
        _this.cached = new Date();

        return _Promise2['default'].resolve(modules);
      });
    }
  }, {
    key: 'keywords',
    value: function keywords(shortcut, name) {
      var devider = this.settings.devider;
      var shortcuts = {
        __pkghub_addons: name + devider,
        __pkghub_plugins: name + devider + 'plugin' + devider,
        __pkghub_themes: name + devider + 'theme' + devider
      };

      return shortcuts[shortcut];
    }
  }, {
    key: 'find',

    // 这里要加一层缓存，不要每次都去 list 一遍模块
    // 因为 npm 有个问题同时调用两次 load list 会报错。
    // 这样的话如果在路由里使用基本不现实
    value: function find(name, modules) {
      var _this2 = this;

      return new _Promise2['default'](function (resolve, reject) {
        // 先判断是否完全匹配模块名称
        var pkg = modules.dependencies[name];
        if (pkg) return resolve(pkg);

        // 分离模块名称和模板名称
        // e.g: candy-theme-default/index => candy-theme-default
        var pkgname = finder.split(name);
        var filename = finder.split(name, 'filename');

        if (pkgname && filename) {
          var m = modules.dependencies[pkgname] || null;
          if (!m || !m.realPath) return reject(new Error('No module ' + pkgname + ' was found'));

          return resolve({
            module: m,
            file: finder.read(m.realPath, filename)
          });
        }

        // 如果找不到 `/` 而且不匹配任何模块，进行搜索
        var result = {};
        var keyword = _this2.keywords(name, modules.name) || name;

        Object.keys(modules.dependencies).forEach(function (name) {
          if (name.indexOf(keyword) > -1) result[name] = modules.dependencies[name];
        });

        if (_import2['default'].isEmpty(result)) return reject('No module ' + name + ' was found');

        var availables = Object.keys(result);
        if (availables.length === 1) return resolve(result[availables[0]]);

        return resolve(result);
      });
    }
  }, {
    key: 'load',

    // 加载某一个模块
    // 模块名称可以是全名，也可以是部分名
    // 模块名称可以包涵名称和子文件，比如 candy 或 candy/template.html
    // e.g: name = 'candy/tpl.html', file === tpl.html;
    value: function load(name, force) {
      var _this3 = this;

      var cache = this.module;

      // 如果有缓存，返回缓存内容，这里还应该判断缓存时间, 比如大于多少天自动更新之类
      // 这里可能出现一个 bug，就是前后查询条件不符合
      // 这样 hub 可能会缓存到不正确的结果
      if (this.cached && !force) {
        return this.find(name, cache);
      } // 如果没有缓存，第一次生成缓存
      return this.list().then(function (modules) {
        if (!modules.dependencies) return _Promise2['default'].reject(new Error('No module ' + name + ' was found'));

        return _this3.find(name, modules);
      });
    }
  }, {
    key: 'addons',

    // 返回一个模块的相关模块，包括插件和主题
    // e.g: candy-editor 是 candy 的插件，此例中，插件包涵 `candy-` 字符串
    value: function addons() {
      return this.load('__pkghub_addons');
    }
  }, {
    key: 'plugins',

    // 返回一个模块的插件列表
    // 某个包的插件是以 devider 分割的模块名字
    // e.g: candy-editor 是 candy 的插件，此例中，插件包涵 `candy-plugin` 字符串
    value: function plugins() {
      return this.load('__pkghub_plugins');
    }
  }, {
    key: 'themes',

    // 返回一个模块的主题列表
    // e.g:  candy-theme-balbala 会被返回
    value: function themes() {
      return this.load('__pkghub_themes');
    }
  }, {
    key: 'install',

    // 安装一个包，并返回所有依赖
    value: function install(modules, dir) {
      var _this4 = this;

      if (_import2['default'].isString(modules)) modules = [modules];

      return npm.install(modules, dir).then(function (logs) {
        return _this4.list();
      });
    }
  }]);

  return pkgHub;
})();

exports['default'] = pkgHub;

// 清理 NPM 返回的包信息中不需要的部分
function wash(obj) {
  var washed = {};

  defaults.includes.forEach(function (key) {
    if (obj[key]) washed[key] = obj[key];
  });

  return washed;
}
module.exports = exports['default'];
//# sourceMappingURL=pkghub.js.map