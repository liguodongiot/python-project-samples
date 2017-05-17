#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 生成随机数的方法
# Author: guodong.li 
# DateTime: 2017/5/16 18:27
# PythonVersion: 2.7

import random
import string

# 随机整数 下限必须小于上限
print(random.randint(0, 99))
print(random.randint(20, 20))  # 结果永远是20
# print(random.randint(20, 10)) # 错误

# 随机选取0到100间的偶数
print(random.randrange(0, 101, 2))

print("----------------------")

# 随机浮点数
print(random.random())
print(random.uniform(1, 10))
print(random.uniform(20, 10))

# 随机字符
print(random.choice('abcdefg&#%^*f'))

# 多个字符中选取特定数量的字符
print(random.sample('abcdefghij', 3))

# 多个字符中选取特定数量的字符组成新字符串
new_str = string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).replace(" ","")
print(new_str)

# 随机选取字符串
print(random.choice(['apple', 'pear', 'peach', 'orange', 'lemon']))

# 洗牌
items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
print(items)

print("--------------------")

# random.seed(int)
# 给随机数对象一个种子值，用于产生随机序列。
# 对于同一个种子值的输入，之后产生的随机数序列也一样。
# 通常是把时间秒数等变化值作为种子值，达到每次运行产生的随机系列都不一样
# seed()省略参数，意味着使用当前系统时间生成随机数

random.seed(10)
print(random.random())  # 0.57140259469
random.seed(10)
print(random.random())  # 0.57140259469  同一个种子值，产生的随机数相同
print(random.random())  # 0.428889054675

random.seed()  # 省略参数，意味着取当前系统时间
print(random.random())
random.seed()
print(random.random())
