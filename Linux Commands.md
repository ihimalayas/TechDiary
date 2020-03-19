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

    ps -ef | grep meross | grep -v grep | cut -c 9-15 | xargs kill -s 9
    ps -ef | grep meross | grep -v grep | awk '{print $2}' | xargs kill -s 9

> 说明：
    “grep meross”的输出结果是，所有含有关键字“firefox”的进程。
    “grep -v grep”是在列出的进程中去除含有关键字“grep”的进程。
        “cut -c 9-15”是截取输入行的第9个字符到第15个字符，而这正好是进程号PID。
         awk '{print $2}'是打印出第二行的数据，正好是进程号PID.

    “xargs kill -s 9”中的xargs命令是用来把前面命令的输出结果（PID）作为“kill -s 9”命令的参数，并执行该命令。“kill -s 9”会强行杀掉指定进程。

## 计算ls命令后显示的文件个数

    ls -al | wc -l