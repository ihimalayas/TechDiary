# windows 10 环境下VScode中如何使用Git

> Github注册邮箱ccbguodawei@126.com
> 用户名：ihimalayas
> Github 仓库地址： https://github.com/ihimalayas/TechDiary.git

## 下载Git并安装，并添加路径到环境变量。

    C:\Users\inkS\Desktop\TechDiary>Git --version
    git version 2.23.0.rc2.windows.1

## 在GitHub上新建一个仓库

    TechDiary

## 在本地新建一个文件夹，作为VSCode代码的工作文件夹。

    TechDiary
> mycode既是VSCode的代码工作文件夹又应该是Git的本地仓库。在命令行方式下进入TechDiary，输入git init

    git init

## 添加用户名和邮箱。该用户名和邮箱是注册GitHub时使用的用户名和邮箱:

    git config --global user.name "ihimalayas"
    git config --global user.email "ccbguodawei@126.com"

## 生成秘钥,并配置github的

    继续在该目录下输入：
    ssh-keygen -t rsa -C "ccbguodawei@126.com"

    ```
    C:\Users\inkS\Desktop\pyProject>ssh-keygen -t rsa -C "ccbguodawei@126.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (C:\Users\inkS/.ssh/id_rsa): D:\workSpace\ssh-key
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in id_rsa.
    Your public key has been saved in id_rsa.pub.
    The key fingerprint is:
    SHA256:Vr50A4LcmoEL+O3MJUDlhjATlonHAqznJ8ROR3fPiVw ccbguodawei@126.com
    The key's randomart image is:
    +---[RSA 2048]----+
    |X++..            |
    |+Xoo.o.o. E      |
    |o++.+.+oo=o.     |
    |..==.. +o++.     |
    | *..+ + S o o    |
    |  ++.o . . o .   |
    |   o+     .      |
    |                 |
    |                 |
    +----[SHA256]-----+
    ```

> 命令执行完毕会生成一个名为ssh-key.pub的文件。利用文本编辑器打开该文件，全文复制。

打开GitHub上的TechDiary仓库，进入setting，设置deploy keys，将ssh-key.pub中的内容粘贴进去即可。

## 绑定本地文件夹和GitHub仓库：

    git remote add origin https://ihimalayas:************@github.com/ihimalayas/TechDiary.git

    1. 如果输错了需要修改，可以删除.git文件重新init
    2. 或者使用下面的命令修改地址：git remote set-url origin https://username:password@github.com/ihimalayas/TechDiary.git
    3. 或者用下面的命令只删掉remote设置：git remote remove origin

## 设置完成后可以做一下连接测试

    ssh -T git@github.com

## 从远程Github拉取（复制、克隆）项目文件

    git pull origin master

## github.com关于新建仓库和已存在仓库连接方式

    1. create a new repository on the command line
        echo "# datascience" >> README.md
        git init
        git add README.md
        git commit -m "first commit"
        git remote add origin https://github.com/ihimalayas/datascience.git
        git push -u origin master
    2. push an existing repository from the command line
        git remote add origin https://github.com/ihimalayas/datascience.git
        git push -u origin master

## 小结

### 使用Github版本源文件管理的过程是：

    1. 安装了Git
    2. 有Github账号，并且创建了对应仓库
    3. VSCode中为项目初始化了git init有了.git文件夹
    4. 设置了remote，链接到Github远程仓库
    5. 先要推送到本地Git仓库，就是Ctrl+回车
    6. 从菜单推送到远程Github仓库

> 之后如果代码文件有了修改，那么就可以直接
>
> - Ctrl+回车提交到本地Git，
> - 再菜单推送到Github，
> - 反复如此即可。

亦即：

    1. 打开源代码管理栏
    2. 输入提交信息（注释）
    3. 提交 CTRL+ENTER
    4. 点开…选择>推送
