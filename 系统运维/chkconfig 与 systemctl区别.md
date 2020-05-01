# chkconfig 与 systemctl区别

## chconfig命令

### 参数用法：

- –add 　增加所指定的系统服务，让chkconfig指令得以管理它，并同时在系统启动的叙述文件内增加相关数据。
- –del 　删除所指定的系统服务，不再由chkconfig指令管理，并同时在系统启动的叙述文件内删除相关数据。
- –level<等级代号> 　指定读系统服务要在哪一个执行等级中开启或关毕。
- 等级0表示：表示关机
- 等级1表示：单用户模式
- 等级2表示：无网络连接的多用户命令行模式
- 等级3表示：有网络连接的多用户命令行模式
- 等级4表示：不可用
- 等级5表示：带图形界面的多用户模式
- 等级6表示：重新启动
- 需要说明的是，level选项可以指定要查看的运行级而不一定是当前运行级。对于每个运行级，只能有一个启动脚本或者停止脚本。当切换运行级时，init不会重新启动已经启动的服务，也不会再次去停止已经停止的服务。主要用来更新（启动或停止）和查询系统服务（service）的运行级信息，用于维护/etc/rc[0-6].d目录的命令行工具。

- 增加httpd服务

  chkconfig -–add httpd

- 删除httpd服务

  chkconfig –-del httpd

- 列出系统所有的服务启动情况
  
  chkconfig –-list

- 列出mysqld服务设置情况
  
  chkconfig –-list mysqld

- 设定mysqld在等级3和5为开机运行服务（on表示开机启动，off表示开机不启动，reset指重置服务的启动信息）

  chkconfig –-level 35 mysqld on

-设定mysqld在各等级为on，“各等级”包括2、3、4、5等级

  chkconfig mysqld on


## systemctl（代替chkconfig和service）

> 在 Centos 中 systemctl 是设置系统服务（service）的命令，它融合之前service和chkconfig的功能于一体。
可以使用它永久性或只在当前会话中启用/禁用服务。

1. 启动、停止、重启、重载服务

    systemctl start name.service
    systemctl stop name.service
    systemctl restart name.service
    systemctl reload name.service

2. 查看某个服务（单元）的状态

  systemctl status name.service

3. 激活/禁止自动启动

   systemctl enable httpd.service
   systemctl disable httpd.service

3. 杀死服务

   systemctl kill httpd

## 比较

 任务  |  旧指令  |  新指令
 ---------|----------|---------
使某服务自动启动 | chkconfig --level 3 httpd on | systemctl enable httpd.service
使某服务不自动启动 | chkconfig --level 3 httpd off | systemctl disable httpd.service
检查服务状态 | service httpd status | systemctl status httpd.service（服务详细信息） / systemctl is-active httpd.service （仅显示是否 Active)
加入自定义服务 | chkconfig --add test | systemctl load test.service
删除服务 | chkconfig --del xxx | 停掉应用，删除相应的配置文件
显示所有已启动的服务 | chkconfig --list | systemctl list-units --type=service
启动某服务 | service httpd start | systemctl start httpd.service
停止某服务 | service httpd stop | systemctl stop httpd.service
重启某服务 | service httpd restart | systemctl restart httpd.service