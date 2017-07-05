#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/7/4 9:54
# PythonVersion: 3.6

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello.*\!')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello, liguodong! How are you?')

if match:
    # 使用Ma`tch获得分组信息
    print(match.group())



