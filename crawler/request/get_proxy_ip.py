#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: liguodong
# DateTime: 2017/5/14 23:09
# PythonVersion: 3.6

import requests
import re

iplist = []  # 初始化一个list用来存放我们获取到的IP
html = requests.get("http://www.kuaidaili.com/")
# <td data-title="IP">((?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]))</td>
# <td data-title="PORT">(\d+)</td>
p = r'<td data-title="IP">((?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]))</td>'

# 表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配，包括换行符，findall返回的是个list哦！
# <td data-title="IP">58.101.16.133</td><td data-title="PORT">8888</td>
iplistn = re.findall(p, html.text, re.S)
for ip in iplistn:
    # re.sub 是re模块替换的方法，这儿表示将\n替换为空
    i = re.sub('\n', '', ip)
    iplist.append(i.strip())  # 添加到我们上面初始化的list里面, i.strip()的意思是去掉字符串的空格哦！
    print(i.strip())
print(iplist)

