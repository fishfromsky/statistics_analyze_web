## ![pkghub](https://cdn1.iconfinder.com/data/icons/Momentum_MatteEntireSet/32/network-hub.png) pkghub ![npm](https://badge.fury.io/js/pkghub.png)

a package hub for human, based on NPM itself

### Installation
```bash
$ npm install pkghub
```

### Example
```js
var Hub = require('pkghub')
var hub = new Hub('-')

// re-config devider
pkghub.config({ devider: '/' })

// list packages' tree (parsed json)
pkghub.list().then(function(modules) {
  console.log(modules)
})

// list selected plugin's package info (parsed)
pkghub.load('mua-wordpress').then(function(plugin) {
  console.log(plugin) // load mua-wordpress as a plugin
})

// list plugins devided by '-'
pkghub.plugins().then(function(plugins) {
  console.log(plugins)
})

// install selected module
pkghub.install('my-new-plugin').then(function(tree) {
  console.log(tree)
})
```

### Contributing
- Fork this repo
- Clone your repo
- Install dependencies
- Checkout a feature branch
- Feel free to add your features
- Make sure your features are fully tested
- Open a pull request, and enjoy <3

### MIT license
Copyright (c) 2013 turing &lt;o.u.turing@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

---
![docor](https://cdn1.iconfinder.com/data/icons/windows8_icons_iconpharm/26/doctor.png)
generated using [docor](https://github.com/turingou/docor.git) @ 0.1.0. brought to you by [turingou](https://github.com/turingou)