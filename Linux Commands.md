# Linux Commands

## 检查端口被哪个进程占用

    netstat -lnpt |grep 5672

## 查看进程的详细信息

    ps 6832

## 中止进程

    kill -9 683

## ps -ef|grep ** | grep **

    | 将前一命令的输出项，作为后一命令的输入项目。

## linux操作系统下，怎么使用kill按照PID一次杀死多个进程

    ps -ef | grep ccbft | grep -v grep | cut -c 9-15 | xargs kill -s 9
    ps -ef | grep meross | grep -v grep | awk '{print $2}' | xargs kill -s 9

> 说明：
    “grep meross”的输出结果是，所有含有关键字“firefox”的进程。
    “grep -v grep”是在列出的进程中去除含有关键字“grep”的进程。
        “cut -c 9-15”是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。
         awk '{print $2}'是打印出第二行的数据，正好是进程号PID.

    “xargs kill -s 9”中的xargs命令是用来把前面命令的输出结果（PID）作为“kill -s 9”命令的参数，并执行该命令。“kill -s 9”会强行杀掉指定进程。

## 计算ls命令后显示的文件个数

    ls -al | wc -l


## nginx 重启等操作


### 进入nginx安装目录sbin下，输入命令./nginx -t

    [root@vm-20202141951290001 sbin]# ./nginx -t
    nginx: the configuration file /opt/data/regulation/nginx/conf/nginx.conf syntax is ok
    nginx: configuration file /opt/data/regulation/nginx/conf/nginx.conf test is successful

> 看到如下显示：nginx.conf syntax is ok，nginx.conf test is successful说明配置文件正确！

### 重启Nginx服务

- 方法一
    
    进入nginx可执行目录sbin下，输入命令./nginx -s reload 

- 方法二

  查找当前nginx进程号，然后输入命令：kill -HUP 进程号 ，实现重启nginx服务


## vim 的快捷用法

### 光标移动

- G 到文件尾
- fn+end 到行尾
- gg  文件首行 
- :n  跳到第n行
- :e 刷新文件

### 操作辅助相关

- 显示行号：set number(set nu)
- 不显示行号 set nonumber(set nonu)
- q:  或者 q/显示历史命令
- set cursorline  可以在当前光标所在行显示一条直线
- 分屏:  竖直分屏:vsp， 水平分屏:sp
- ggG= 格式化文档或代码对齐

### 撤销操作

- u  撤销上一步操作
- ctrl+r   重做