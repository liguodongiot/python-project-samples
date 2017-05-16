#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 四种初始化方式
# Author: liguodong
# DateTime: 2017/5/16 7:47
# PythonVersion: 3.6

# 1、直接字符串
from pyquery import PyQuery as pq
# pq 参数可以直接传入 HTML 代码，doc 现在就相当于 jQuery 里面的 $ 符号了。
doc = pq("<html></html>")

# 2、lxml.etree
from lxml import etree
# 首先用 lxml 的 etree 处理一下代码，这样如果你的 HTML 代码出现一些不完整或者疏漏，
# 都会自动转化为完整清晰结构的 HTML代码。
doc2 = pq(etree.fromstring("<html></html>"))

# 3、直接传URL
from pyquery import PyQuery as pq
# 这里就像直接请求了一个网页一样，类似用 urllib2 来直接请求这个链接，得到 HTML 代码。
doc = pq('http://www.baidu.com')

# 4、传文件
from pyquery import PyQuery as pq
# 直接传某个路径的文件名。
doc = pq(filename='hello.html')

