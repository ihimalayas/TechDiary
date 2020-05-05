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


## centos 远程ssh访问用户

更改etc/ssh/sshd_config。在其中增加AllowUsers:username(可以多个,空格分开)给普通用户增加ssh权限。

#PermitRootLogin yes
这一行的“#”去掉，修改为：
PermitRootLogin yes

## 先备份文件后操作

    cp /etc/ntp.conf{,.bak}

    cp /etc/ntp.conf /etc/ntp.conf.bak

## 2>&1

    1> 指标准信息输出路径（也就是默认的输出方式）
    2> 指错误信息输出路径
    2>&1 指将标准信息输出路径指定为错误信息输出路径（也就是都输出在一起）

    /dev/null  看作"黑洞"，它非常等价于一个只写文件，所有写入它的内容都会永远丢失。而尝试从它那儿读取内容则什么也读不到。

    2>&1 是将错误输出到标准输出。

## linux shell 中行末尾的"&" 的作用

    cp $filename /dev/ &

    & 代表非阻塞方式拷贝文件，如果不加& 则必须等到执行完该指令后才能执行后来的指令。

> 此外，可以使用“＆”符号通过一（1）个ssh连接运行许多进程，以保持最少数量的终端。例如，我有一个进程侦听消息以提取文件，第二个进程侦听消息以上传文件：使用“＆”，我可以在一个终端中通过与服务器的ssh连接来运行两个服务。 。*****我刚刚意识到，在ssh会话关闭后，通过“＆”运行的这些进程也将“保持活动”！如果您与服务器的连接中断，则非常整洁且有用**

> 如果没有其他说明，则命令将接管前台。在一个shell会话中，只有一个“前台”进程正在运行。＆符号指示命令在后台进程中运行，并立即返回命令行以获取其他命令。sh my_script.sh &Shell会话关闭后，后台进程将无法保持活动状态。SIGHUP终止所有正在运行的进程。无论如何还是默认。如果您的命令长时间运行或无限期运行（即：微服务），则需要使用nohup预先挂起它，以便在断开会话连接后它仍在运行：nohup sh my_script.sh &编辑：当使用＆时，关于关闭后台进程似乎确实有一个灰色区域。请注意，根据您的操作系统和本地配置（特别是在CENTOS / RHEL上），shell 可能会关闭您的进程

(3)前台和后台

　　在shell下面，一个新产生的进程可以通过用命令后面的符号“；”和“&”来分别以前台和后台的方式来执行，语法如下：

　　command

　　产生一个前台的进程，下一个命令须等该命令运行结束后才能输入。

　　command &

　　产生一个后台的进程，此进程在后台运行的同时，可以输入其他的命令。

    $*是传递给脚本（或方法）的所有参数复
    $# 是传给脚本的参数个数
    $@ 是传给脚本的所有参数的列表
    $0 是脚本（或方法）本制身的名字
    $1是传递给该知shell脚本（或方法）的第一个参道数
    $2是传递给该shell脚本（或方法）的第二个参数