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
