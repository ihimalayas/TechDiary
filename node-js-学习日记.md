#


## npm 查看和修改 prefix和 cache配置

> 一般选择用命令的方式设置，并且将这两个文件夹配置在其他盘符防止权限问题

    npm config set prefix “D:\nodejs\node_global” //设置全局包目录
    npm config set cache “D:\nodejs\node_cache” //设置缓存目录

    npm config list //查看基本配置

    npm config list -l //查看所有配置

### npm本地安装与全局安装有什么区别？
    
    npm install grunt // 本地安装，则是将模块下载到当前命令行所在目录。
    npm install -g grunt//全局安装，模块将被下载安装到【全局目录】中；

### npm如何获取全局安装的默认目录？

    npm config get prefix

### npm如何设置全局安装的默认目录？
    
    npm config set prefix “directory”


## 配置淘宝 NPM 镜像

> 国内直接使用 npm 的官方镜像非常慢，这里推荐使用淘宝 NPM 镜像。淘宝 NPM 镜像是一个完整 npmjs.org 镜像，你可以用此代替官方版本(只读)，同步频率目前为 10分钟一次以保证尽量与官方服务同步。

- 你可以使用淘宝定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm:

    npm config set registry=https://registry.npm.taobao.org

    
## 需要关注的一个配置文件 \node_modules\npm\.npmrc

Windows下的Nodejs npm路径是appdata，存在在cmd下执行以下命令无效的情况

    npm config set cache "C:\apps\nodejs\node_cache"
    npm config set prefix "C:\apps\nodejs\node_global"
    npm config set registry=https://registry.npm.taobao.org

最后在nodejs的安装目录中找到node_modules\npm\.npmrc文件

原文件内容为：
    
    prefix=${APPDATA}\npm

修改如下即可：

    prefix = C:\apps\nodejs\
    cache = C:\apps\nodejs\node_cache
    registry=https://registry.npm.taobao.org

> nodejs会自动寻找该路径下的node_modules文件夹为实际存放全局模块的路径，这也是为啥叫prefix不叫global的原因；以后安装的全局模块都会被放到C:\apps\nodejs\node_modules下，跟npm模块在一个文件夹中；

## 安装更新模块

    命令：npm install model –g
        - npm install代表安装更新， model是指的模块名字
        - -g：代表安装到global目录下