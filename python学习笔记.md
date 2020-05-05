# python

## 关于在centos下安装python3.7.0以上版本时报错ModuleNotFoundError: No module named '_ctypes'的解决办法

3.7版本需要一个新的包libffi-devel，安装此包之后再次进行编译安装即可。

#yum install libffi-devel -y
#make install
若在安装前移除了/usr/bin下python的文件链接依赖，此时yum无法正常使用，需要自己下载相关软件包安装，为节省读者时间，放上链接

#wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libffi-devel-3.0.13-18.el7.x86_64.rpm
#rpm -ivh libffi-devel-3.0.13-18.el7.x86_64.rpm
安装完成后重新进行make install，结束后再次配置相关文件的软连接即可。

> python3中有个内置模块叫ctypes，它是python3的外部函数库模块，提供了兼容C语言的数据类型，并通过它调用Linux系统下的共享库(Shared library)，此模块需要使用centos7系统中外部函数库(Foreign function library)的开发链接库(头文件和链接库)。
由于在centos7系统中没有安装外部函数库(libffi)的开发链接库软件包，所以在安装pip的时候就报了"ModuleNotFoundError: No module named '_ctypes'"的错误。
