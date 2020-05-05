#YUM 本地源配置


## 备份CentOS的yum源配置文件

目录：/etc/yum.repos.d/
将所有mv *.repo ./backup

## 新增并修改local.repo文件

        [base]
        name=Centos-$releasever-Base
        baseurl=http://172.16.2.11/
        gpgcheck=0
        enbale=1

## 安装NTP

yum  install NTP


## 同步时间

ntpdate 100.123.0.21



[root@clientlinux ~]# ntpdate 192.168.100.254 
#由于ntpd的server/client之间的时间误差不允许超过1000秒，
# 因此你得先手动进行时间同步，然后再设定与启动时间伺服器呦！

[root@clientlinux ~]# vim /etc/ntp.conf 
#server 0.centos.pool.ntp.org
#server 1.centos.pool.ntp.org
#server 2.centos.pool.ntp.org
restrict 192.168.100.254   <==放行伺服器来源！
server 192.168.100.254     <==这就是伺服器！
#很简单，就是将原本的server项目注解，加入我们要的伺服器即可

[root@clientlinux ~]# /etc/init.d/ntpd start 
[root@clientlinux ~]# chkconfig ntpd on




1.ntpstat
ntpstat 命令查看时间同步状态，这个一般需要回5-10分钟后才能成功连接和同步。所以，服务器启动后答需要稍等下。
# ntpstat
unsynchronised
time server re-starting
polling server every 64 s
连接并同步后:
synchronised to NTP server (202.112.10.36) at stratum 3
time correct to within 275 ms
polling server every 256 s



restrict 100.123.0.21 nomodify notrap noquery