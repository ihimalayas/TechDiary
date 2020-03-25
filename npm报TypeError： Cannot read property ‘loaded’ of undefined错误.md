# npm报TypeError: Cannot read property 'loaded' of undefined错误


执行npm相关的命令时，会报Cannot read property 'loaded' of undefined错误。解决办法:删除 /Users/｛user目录｝/.npmrc
执行npm相关的命令时，会报Cannot read property 'loaded' of undefined错误。

## 错误信息可能还包括如下

Error: EISDIR: illegal operation on a directory, read TypeError: Cannot read property 'loaded' of undefined at exit (/usr/local/lib/node_modules/npm/lib/utils/error-handler.js:97:27) at errorHandler (/usr/local/lib/node_modules/npm/lib/utils/error-handler.js:216:3) at /usr/local/lib/node_modules/npm/bin/npm-cli.js:78:20 at cb (/usr/local/lib/node_modules/npm/lib/npm.js:225:22) at /usr/local/lib/node_modules/npm/lib/npm.js:263:24 at /usr/local/lib/node_modules/npm/lib/config/core.js:81:7 at Array.forEach () at /usr/local/lib/node_modules/npm/lib/config/core.js:80:13 at f (/usr/local/lib/node_modules/npm/node_modules/once/once.js:25:25) at finalize (/usr/local/lib/node_modules/npm/lib/config/core.js:187:14) /usr/local/lib/node_modules/npm/lib/utils/error-handler.js:97 var doExit = npm.config.loaded ? npm.config.get('_exit') : true

## 解决办法

> 删除 /Users/｛user目录｝/.npmrc

 