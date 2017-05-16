#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/5/16 18:27
# PythonVersion: 2.7

import random


# 随机整数
print(random.randint(0, 99))

# 随机选取0到100间的偶数
print(random.randrange(0, 101, 2))

# 随机浮点数
print(random.random())
print(random.uniform(1, 10))


# 随机字符
print(random.choice('abcdefg&#%^*f'))


