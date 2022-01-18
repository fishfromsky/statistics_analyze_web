import _ from 'underscore'
import Promise from 'bluebird'
import * as npm from './npm'
import * as finder from './finder'

const defaults = {
  devider: '-',
  includes: [
    'name',
    'version',
    'logo',
    'styles',
    'fonts',
    'javascripts',
    'static',
    'screenshot',
    'description',
    'main',
    'repository',
    'keywords',
    'author',
    'license',
    'bugs',
    'readme',
    'path',
    'depth',
    'realPath',
    'view engine'
  ]
}

export default class pkgHub {
  constructor(devider = '-') {
    this.module = {}
    this.module.dependencies = {}
    this.settings = _.clone(defaults)
    this.settings.devider = devider
  }

  config(params = {}) {
    this.settings = _.extend(defaults, params)
    return this.settings
  }

  // 列出所有依赖模块
  list() {
    return npm.ls().then(packages => {
      var modules = _.clone(packages)
      var dependencies = modules.dependencies

      if (dependencies) {
        delete modules.dependencies

        _.each(dependencies, function(module, name) {
          dependencies[name] = wash(module)
        })
      }

      modules = wash(modules)
      modules.dependencies = dependencies

      this.module = modules
      this.cached = new Date()

      return Promise.resolve(modules)
    })
  }

  keywords(shortcut, name) {
    const devider = this.settings.devider
    const shortcuts = {
      '__pkghub_addons': name + devider,
      '__pkghub_plugins': name + devider + 'plugin' + devider,
      '__pkghub_themes': name + devider + 'theme' + devider
    }

    return shortcuts[shortcut]
  }

  // 这里要加一层缓存，不要每次都去 list 一遍模块
  // 因为 npm 有个问题同时调用两次 load list 会报错。
  // 这样的话如果在路由里使用基本不现实
  find(name, modules) {
    return new Promise((resolve, reject) => {
      // 先判断是否完全匹配模块名称
      var pkg = modules.dependencies[name]
      if (pkg) 
        return resolve(pkg)

      // 分离模块名称和模板名称
      // e.g: candy-theme-default/index => candy-theme-default
      var pkgname = finder.split(name)
      var filename = finder.split(name, 'filename')

      if (pkgname && filename) {
        var m = modules.dependencies[pkgname] || null
        if (!m || !m.realPath) 
          return reject(new Error(`No module ${pkgname} was found`))

        return resolve({
          module: m,
          file: finder.read(m.realPath, filename)
        })
      }

      // 如果找不到 `/` 而且不匹配任何模块，进行搜索
      var result = {}
      var keyword = this.keywords(name, modules.name) || name

      Object.keys(modules.dependencies).forEach(name => {
        if (name.indexOf(keyword) > -1) 
          result[name] = modules.dependencies[name]
      })

      if (_.isEmpty(result)) 
        return reject(`No module ${name} was found`)

      var availables = Object.keys(result)
      if (availables.length === 1) 
        return resolve(result[availables[0]])

      return resolve(result)
    })
  }

  // 加载某一个模块
  // 模块名称可以是全名，也可以是部分名
  // 模块名称可以包涵名称和子文件，比如 candy 或 candy/template.html
  // e.g: name = 'candy/tpl.html', file === tpl.html;
  load(name, force) {
    var cache = this.module

    // 如果有缓存，返回缓存内容，这里还应该判断缓存时间, 比如大于多少天自动更新之类
    // 这里可能出现一个 bug，就是前后查询条件不符合
    // 这样 hub 可能会缓存到不正确的结果
    if (this.cached && !force) 
      return this.find(name, cache)

    // 如果没有缓存，第一次生成缓存
    return this.list().then(modules => {
      if (!modules.dependencies) 
        return Promise.reject(new Error(`No module ${name} was found`))

      return this.find(name, modules)
    })
  }

  // 返回一个模块的相关模块，包括插件和主题
  // e.g: candy-editor 是 candy 的插件，此例中，插件包涵 `candy-` 字符串
  addons() {
    return this.load('__pkghub_addons')
  }

  // 返回一个模块的插件列表
  // 某个包的插件是以 devider 分割的模块名字
  // e.g: candy-editor 是 candy 的插件，此例中，插件包涵 `candy-plugin` 字符串
  plugins() {
    return this.load('__pkghub_plugins')
  }

  // 返回一个模块的主题列表
  // e.g:  candy-theme-balbala 会被返回
  themes() {
    return this.load('__pkghub_themes')
  }

  // 安装一个包，并返回所有依赖
  install(modules, dir) {
    if (_.isString(modules)) 
      modules = [ modules ]

    return npm.install(modules, dir).then(logs => {
      return this.list()
    })
  }
}

// 清理 NPM 返回的包信息中不需要的部分
function wash(obj) {
  var washed = {}

  defaults.includes.forEach(key => {
    if (obj[key]) 
      washed[key] = obj[key]
  })

  return washed
}
