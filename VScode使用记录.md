# Vscode使用记录

## 问题：VSCode 多行批量添加冒号

有时候需要在 VSCode 重执行多行批量操作，比如给每行添加字符冒号、分号或者其它字符，你可以使用 VSCode 的基于正则表达式的替换功能。操作步骤：

    1. Ctrl + H 调出替换窗口
    2. Alt + R 开起正则表达式匹配模式
    3. 查找行输入 $ ，替换行输入替换后的文本
    4. Ctrl+Alt+Enter 替换全部

## VSCode 当前文件显示完整路径信息

File->Preferences->Settings
搜索window.title
修改 activeEditorShort => activeEditorLong