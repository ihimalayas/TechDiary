# 如何间隔相同的时间执行相同或者不同的命令


## BAT文件中如何注释:

    1、:: 注释内容（第一个冒号后也可以跟任何一个非字母数字的字符）
    2、rem 注释内容（不能出现重定向符号和管道符号）
    3、echo 注释内容（不能出现重定向符号和管道符号）〉nul
    4、if not exist nul 注释内容（不能出现重定向符号和管道符号）
    5、:注释内容（注释文本不能与已有标签重名）
    6、%注释内容%（可以用作行间注释，不能出现重定向符号和管道符号）
    7、goto 标签 注释内容（可以用作说明goto的条件和执行内容）
    8、:标签 注释内容（可以用作标签下方段的执行内容）

## windows批处理 ->bat

### 命令梳理

- 

@echo off

// 显示标题
title 定期执行tracert 172.30.10.1

// 循环体

:loop
if "%time%" GTR "23:00.00" (exit) else goto t //如果系统时间是23点退出程序。如果不是则继续进行t标签的程序
:t

tracert 172.30.10.1 >> tracert.log

goto loop

那么如下的各个操作的意义如下：
%date:~0,4%  表示从左向右指针向右偏0位，然后从指针偏移到的位置开始提取4位字符，结果是2014（年的值）
%date:~5,2%  表示指针从左向右偏移5位，然后从偏移处开始提取2位字符，结果是03（月的值）
%date:~8,2%  表示指针从左向右偏移8位，然后从偏移处开始提取2位字符，结果是01（日的值）
%date:~5%    表示指针从左向右偏移5位，然后提取所有的值
%date:~-5%   表示指针反方向偏移，从最右端开始，偏移5位，然后从指针处提取左边的所有数值。

注意：“2014-03-01 星期六”是个字符串，在计算机里指针是从0开始计数的，所以这串字符的指针意义上的第5位是0，月份的0，取两位刚好是03.

同理，比如当前系统的time变量的值如下：

那么如下的各个操作的意义如下：
%time:~0,2%  表示从左向右指针向右偏0位，然后从指针偏移到的位置开始提取2位字符，结果是小时字段数值
%time:~3,2%  表示指针从左向右偏移3位，然后从偏移处开始提取2位字符，结果是分钟字段数值
%time:~6,2%  表示指针从左向右偏移6位，然后从偏移处开始提取2位字符，结果是秒字段数值
实战操作：

md d:\%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%

注：md是创建目录的意思

执行后D盘根目录多了一个文件夹


del abc.txt>nul 2>nul
这个">nul 2>nul"可以屏蔽一切屏幕的输出可以这样理解：

假如执行一个命令，但是不想在屏幕里看到这个命令的执行情况，可以使用"[命令]>nul"就可以屏蔽命令在屏幕上的输出，但是有的命令执行会出错，即使用了">nul"也不能屏蔽命令产生的信息，所以就在后面加" 2>nul"这个，就是"[命令]>nul＋空格＋2>nul"，这样，不管命令是否正确的运行，都不会在屏幕看到这个命令所产生的屏幕显示了。
用"dir"命令可以显示当前目录的文件及文件夹列表，这时如果用"dir>nul"，就看不见dir命令执行的屏幕输出了，那么再键入"dirr"时会显示" 'dirr' 不是内部命令，也不是外部命令，也不是批处理文件。"，这时如果用"dirr>nul"来屏蔽这个错误，因为依然会出现" 'dirr' 不是内部命令，也不是外部命令，也不是批处理文件。"这个错误提示，这时如果用"dirr>nul 2>nul"的话，就在屏幕上看不到上面的出错提示了


批处理（.bat）无限循环，定时，固定时间间隔
需要固定时间间隔比如5秒运行一个文件，网上查了下最简单的就是用goto语句，如果不加延时那就是死循环，在里面加上延时语句choice /t 5 /d y /n >nul。下面的批处理作用就是每隔5秒屏幕上输出一次jajaja。

@echo off

:start
echo jajaja
choice /t 5 /d y /n >nul

goto start


https://www.jb51.net/article/107285.htm


Choice 命令

使用此命令可以让用户输入一个字符，从而运行不同的命令。使用时应该加/c:参数，c:后应写提示可输入的字符，之间无空格。它的返回码为1234……。这个命令在有些Windows版本（比如WindowsXP）上可能不可用。

语法：
CHOICE：[/C[:]按键表] [/N] [/S] [/T[:]选择值,秒数] [显示文本]
其中，/C表示可选则的按键，/N表示不要显示提示信息，/S表示大小写字符敏感方式，/T表示若在批定的时间内没有选择的话，自动执行/C中定义的某个选择值。显示文本是CHOICE命令执行时的提示信息。选择结果将用ERRORLEVEL值来表示。

示例：

@echo off
choice /c:dme defrag,mem,end
if errorlevel 3 goto defrag
 REM 应先判断数值最高的错误码
if errorlevel 2 goto mem
if errorlevel 1 goto end
 
:defrag
c:\dos\defrag
goto end
 
:mem
mem
goto end
 
:end
echo good bye
此文件运行后，将显示 defrag,mem,end[D,M,E]? 用户可选择d m e ，然后if语句将作出判断，d表示执行标号为defrag的程序段，m表示执行标号为mem的程序段，e表示执行标号为end的程序段，每个程序段最后都以goto end将程序跳到end标号处，然后程序将显示good bye，文件结束。

可替换的命令

对WindowsXP上不能使用CHOICE命令的情形，如果想使用相似的功能，可以使用 SET 命令，参见Set 命令 /P选项。

choice一般在cmd批处理中用来根据用户输入执行不同的操作，非常实用，例如

下面是两个软件根据用户选择来执行

@echo off
远程协助工具集
:start
cls
color 0a
MODE con: COLS=60 LINES=20
echo.
echo  ===============================
echo   请选择远程工具
echo  ===============================
echo.
echo  1. AnyDesk
echo.
echo  2. TeamViewer
echo.
echo.
:cho
set choice=
set /p choice=  请输入工具编号:
IF NOT "%Choice%"=="" SET Choice=%Choice:~0,1%
if /i "%choice%"=="1" goto AnyDesk
if /i "%choice%"=="2" goto TeamViewer
 
:AnyDesk
AnyDesk.exe
exit
 
:TeamViewer
TeamViewer.exe
exit
下面来介绍一下choice的命令使用


CHOICE [/C choices] [/N] [/CS] [/T timeout /D choice] [/M text]

描述:
该工具允许用户从选择列表选择一个项目并返回所选项目的索引。

参数列表:
/C choices 指定要创建的选项列表。默认列表是 "YN"。

/N 在提示符中隐藏选项列表。提示前面的消息得到显示，选项依旧处于启用状态。

/CS 允许选择分大小写的选项。在默认情况下，这个工具是不分大小写的。

/T timeout 做出默认选择之前，暂停的秒数。可接受的值是从 0到 9999。如果指定了 0，就不会有暂停，默认选项会得到选择。

/D choice 在 nnnn 秒之后指定默认选项。字符必须在用 /C 选项指定的一组选择中; 同时，必须用 /T 指定 nnnn。

/M text 指定提示之前要显示的消息。如果没有指定，工具只显示提示。

/? 显示此帮助消息。

注意:
ERRORLEVEL 环境变量被设置为从选择集选择的键索引。列出的第一个选择返回 1，第二个选择返回 2，等等。如果用户按的键不是有效的选择，该工具会发出警告响声。如果该工具检测到错误状态，它会返回 255 的ERRORLEVEL 值。如果用户按 Ctrl+Break 或 Ctrl+C 键，该工具会返回 0 的 ERRORLEVEL 值。在一个批程序中使用 ERRORLEVEL 参数时，将参数降序排列。

示例:
CHOICE /?
CHOICE /C YNC /M "确认请按 Y，否请按 N，或者取消请按 C。"
CHOICE /T 10 /C ync /CS /D y
CHOICE /C ab /M "选项 1 请选择 a，选项 2 请选择 b。"
CHOICE /C ab /N /M "选项 1 请选择 a，选项 2 请选择 b。"
下面是来自国外网站的介绍

The CHOICE command was introduced in MS-DOS 6 and is still available in MS-DOS 7 (Windows 95/98).

In Windows NT 4, 2000 and XP, CHOICE is no longer a part of the standard distribution. It is, however, available as part of the Windows NT 4 Resouce Kit.
On the other hand, if you still have that old unused MS-DOS 6 or Windows 95/98 version lying around, you can use the CHOICE.COM from that version instead. (*)
Just copy it to a directory that is in your PATH.

Note: 16-bit DOS versions will not work in 64-bit Windows versions.
CHOICE is available again in Windows Vista and later versions.

大部分意思就是 这个命令会在以后的系统中一直存在，但注意16位的系统无法在64位系统自带了，而我们安装的64位系统已经集成了64的choice命令，大家可以放心使用。

注释
ERRORVALUE 环境变量被设置为用户从选择列表中选择的键的索引。您指派的第一个键将返回值 1，第二个将返回值 2，第三个将返回值 3，依此类推。如果用户按下一个不在您指派的键中间的键，Choice.exe 将发出警告声（即，它向控制台发送一个 BEL 或 07h 字符）。如果 Choice.exe 检测到错误情况，它就会返回错误值 255。如果用户按 Ctrl+Break 或 Ctrl+C，Choice.exe 就会返回错误值 0。当您在批处理程序中使用错误值参数时，请将它们以降序列出。

示例
请在批处理文件中键入下列语法：
choice /c ync
运行 Choice.exe 时出现下列语句：
[Y,N,C]?
请在批处理文件中键入下列语法：
choice /c ync /n /m Yes, No or Continue?
运行 Choice.exe 时出现下列语句：
Yes, No, or Continue?
按如下方式将文字添加到语法中：
choice /c ync /m Yes, No, or Continue
运行 Choice.exe 时出现下列语句：
Yes, No, or Continue [Y,N,C]?
/t 命令行选项将设置一个时间限制（在该限制内用户必须响应），并指定当用户在该时间限制内没有作出响应时将显示的值。要将时间限制设置为五秒并指定 N 作为默认值，请在批处理程序中键入下列命令行：
choice /c ync /t 5 /d n
当批处理文件启动 Choice.exe 时，将出现下列消息：
[Y,N,C]?
如果用户未能在五秒钟内按下一个键，Choice.exe 将选择 N 并返回错误值 2。否则，Choice 将返回与用户所选对应的值。


@echo off

echo %time% > bat.log
if "%time%" GTR "22:25:00.00" (exit) else


echo %date:~0,4%-%date:~5,2%-%date:~8,2% -- %time:~0,8% >> bat.log
echo 
echo 
echo ----------------------------------------------------------------- >> bat.log
tracert 172.30.10.1 >> bat.log
echo ----------------------------------------------------------------- >> bat.log@echo off

echo %time% > bat.log
if "%time%" GTR "22:25:00.00" (exit) else


echo %date:~0,4%-%date:~5,2%-%date:~8,2% -- %time:~0,8% >> bat.log
echo 
echo 
echo ----------------------------------------------------------------- >> bat.log
tracert 172.30.10.1 >> bat.log
echo ----------------------------------------------------------------- >> bat.log

## linux->shell