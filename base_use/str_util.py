#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/5/18 14:48
# PythonVersion: 2.7

# 判断字符串是够存在某个子字符串
# 方法1：使用 in 方法实现contains的功能：
site = 'http://www.jb51.net/'
if "jb51" in site:
    print('site contains jb51')

# 方法2：使用find函数实现contains的功能

s = "This be a string"
if s.find("is") == -1:
    print "No 'is' here!"
else:
    print "Found 'is' in the string."

ss = "There be a string"
if ss.find("is") == -1:
    print "No 'is' here!"
else:
    print "Found 'is' in the string."


