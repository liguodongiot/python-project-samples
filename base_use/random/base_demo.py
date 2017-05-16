#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/5/16 17:15
# PythonVersion: 2.7

import time
import random

print "wait 3 seconds"
# time.sleep(秒数)，其中“秒数”
# 秒为单位，可以是小数，0.1秒则代表休眠100毫秒。
time.sleep(3)
print "3 seconds after"

for num in range(10, 20):
    print random.randint(2, 5)

time.sleep(random.randint(2, 5))
print("over...")
