#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从文本文件中每读取一行文本便输出

fileHandler = open('E:/data/test.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)
line = fileHandler.readline()
while line:
    print(line)
    line = fileHandler.readline()
fileHandler.close
