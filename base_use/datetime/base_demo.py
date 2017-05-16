#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: liguodong
# DateTime: 2017/5/15 23:03
# PythonVersion: 3.6

import datetime
# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
# 当前时间加上半小时
d2 = d1 + datetime.timedelta(hours=0.5)
print(d2)
# 格式化字符串输出
d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
print(d3)

# 将字符串转化为时间类型
d4 = datetime.datetime.strptime(d3, '%Y-%m-%d %H:%M:%S')
print(d4)
print(type(d4))
