# Mac 使用记录

## Mac下显示隐藏的文件与文件夹

1. 打开“终端”，根据自己的版本选择命令

   - 早期的OS X（10.6~10.8）系统可以使用如下两条命令来开始或者关闭系统隐藏文件的显示：

         defaults write com.apple.Finder AppleShowAllFiles Yes && killall Finder //显示隐藏文件
         defaults write com.apple.Finder AppleShowAllFiles No && killall Finder //不显示隐藏文件

   - 当升级到OS X 10.9 Mavericks版本之后，这两条命令需要做一些修改，变成了如下命令：
         
          defaults write com.apple.finder AppleShowAllFiles Yes && killall Finder //显示隐藏文件
          defaults write com.apple.finder AppleShowAllFiles No && killall Finder //不显示隐藏文件

2. 快捷键 

   - 在 macOS Sierra，可以使用快捷键⌘⇧.(Command + Shift + .) 来快速（在 Finder 中）显示和隐藏隐藏文件了。


## brew 源更改


# 1、替换brew.git:
$ cd "$(brew --repo)"
# 中国科大:
$ git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
# 清华大学:
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

# 2、替换homebrew-core.git:
$ cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
# 中国科大:
$ git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
# 清华大学:
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

# 3、替换homebrew-bottles:
# 中国科大:
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
$ source ~/.bash_profile
# 清华大学:
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.bash_profile
$ source ~/.bash_profile

# 4、应用生效:
$ brew update