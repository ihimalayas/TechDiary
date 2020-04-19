##  npm报TypeError: Cannot read property 'loaded' of undefined错误


执行npm相关的命令时，会报Cannot read property 'loaded' of undefined错误。解决办法:删除 /Users/｛user目录｝/.npmrc
执行npm相关的命令时，会报Cannot read property 'loaded' of undefined错误。

## 错误信息可能还包括如下

Error: EISDIR: illegal operation on a directory, read TypeError: Cannot read property 'loaded' of undefined at exit (/usr/local/lib/node_modules/npm/lib/utils/error-handler.js:97:27) at errorHandler (/usr/local/lib/node_modules/npm/lib/utils/error-handler.js:216:3) at /usr/local/lib/node_modules/npm/bin/npm-cli.js:78:20 at cb (/usr/local/lib/node_modules/npm/lib/npm.js:225:22) at /usr/local/lib/node_modules/npm/lib/npm.js:263:24 at /usr/local/lib/node_modules/npm/lib/config/core.js:81:7 at Array.forEach () at /usr/local/lib/node_modules/npm/lib/config/core.js:80:13 at f (/usr/local/lib/node_modules/npm/node_modules/once/once.js:25:25) at finalize (/usr/local/lib/node_modules/npm/lib/config/core.js:187:14) /usr/local/lib/node_modules/npm/lib/utils/error-handler.js:97 var doExit = npm.config.loaded ? npm.config.get('_exit') : true

## 解决办法

> 删除 /Users/｛user目录｝/.npmrc



## centos下python3 pip3安装airflow问题

### raise EnvironmentError("%s not found" % (mysql_config.path,)) EnvironmentError: mysql_config not...

    解决办法：

    yum install mysql-devel

### 关于在centos下安装python3.7.0以上版本时报错ModuleNotFoundError: No module named '_ctypes'的解决办法

    #wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libffi-devel-3.0.13-18.el7.x86_64.rpm
    #rpm -ivh libffi-devel-3.0.13-18.el7.x86_64.rpm
    安装完成后重新进行make install，结束后再次配置相关文件的软连接即可。

    解读：
    python3中有个内置模块叫ctypes，它是python3的外部函数库模块，提供了兼容C语言的数据类型，并通过它调用Linux系统下的共享库(Shared library)，此模块需要使用centos7系统中外部函数库(Foreign function library)的开发链接库(头文件和链接库)。
    由于在centos7系统中没有安装外部函数库(libffi)的开发链接库软件包，所以在安装pip的时候就报了"ModuleNotFoundError: No module named '_ctypes'"的错误。
