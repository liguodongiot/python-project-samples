#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/7/4 18:36
# PythonVersion: 3.6

import re

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print("p.pattern:", p.pattern)

print("p.flags:", p.flags)

print("p.groups:", p.groups)

print("p.groupindex:", p.groupindex)

print("########################")

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'H.*g')

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello Hanxiaoyang!')

if match:
    # 使用Match获得分组信息
    print(match.group())

print("########################")

p2 = re.compile(r'\d+')
print(p2.split('one1two2three3four4'))

print("########################")

p3 = re.compile(r'\d+')
print(p3.findall('one1two2three3four4'))

print("########################")

p4 = re.compile(r'\d+')
for m in p4.finditer('one1two2three3four4'):
    print(m.group())

print("########################")

p5 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello hanxiaoyang!'

print(p5.sub(r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print(p5.sub(func, s))

print("########################")

p6 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello hanxiaoyang!'

print(p6.subn(r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print(p6.subn(func, s))

