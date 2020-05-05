#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   get-list.py
@Time    :   2020/03/17 09:39:30
@Author  :   David Kuo 
@Version :   1.0
@Contact :   secguy@126.com
'''


import os
from requests_html import HTMLSession
from requests_file import FileAdapter
from bs4 import BeautifulSoup

session = HTMLSession()

# 如果是网络文件此时即可直接请求
# session.get("https://www.baidu.com")
# 如果是本地文件，需要以下代码
# 挂载文件

session.mount('file://', FileAdapter())

# Windows系统路径目录分隔符为反斜杠，但get需要正斜杠所以先进行一下替换

pwd = os.getcwd().replace("\\","/")
print(pwd)
# 测试发现使用相对路径读不到文件，需要使用绝对路径
html_obj = session.get(f'file:///{pwd}/test.html')
# print(html_obj.html.html)

start_success_num = 0
start_fail_num = 0 

all_app_list = [
    "CCBFT-GOVERN-REGULATION-CMS",
    "CCBFT-GOVERN-REGULATION-COMMON-ENFORCEMENT",
    "CCBFT-GOVERN-REGULATION-COMPLAINT-REPORT",
    "CCBFT-GOVERN-REGULATION-CREDIT-SUPERVISE",
    "CCBFT-GOVERN-REGULATION-EFFECT-SUPERVISE",
    "CCBFT-GOVERN-REGULATION-GENERIC",
    "CCBFT-GOVERN-REGULATION-OPENZUUL",
    "CCBFT-GOVERN-REGULATION-PSZUUL",
    "CCBFT-GOVERN-REGULATION-RISK",
    "CCBFT-GOVERN-REGULATION-SMS",
    "CCBFT-GOVERN-REGULATION-UNITE-SUPERVISE",
    "CCBFT-GOVERN-REGULATION-ZUUL",
    "CCBFT-GOVERN-SSO",
    "CCBFT-GOVERN-SYSTEM",
    "CONFIG-SERVER-DB",
    "REGULATION-DATA-MONITOR",
    "REGULATION-ITEM-LIST",
    "CCBFT-GOVERN-REGULATION-INFO"
]

bs = BeautifulSoup(html_obj.html.html,"html.parser")
for i in bs.find_all('b'):
    if(len(i.text)>4 and len(i.text)<70):
        if(i.text in all_app_list):
            print(i.text + "-"*(60-len(i.text)) + "OK")
            all_app_list.remove(i.text)
            start_success_num +=1
        # else:
        # #   print(i.text + "-"*(70-len(i.text)) + "Wrong!")
        #     start_fail_num +=1


print("system has successfully started " + str(start_success_num) + "  Apps!")

for j in all_app_list:
    print(j + "-"*(60-len(j)) + "Wrong!")

print("system has Failed to startup  " + str(len(all_app_list)) + "  Apps!")

