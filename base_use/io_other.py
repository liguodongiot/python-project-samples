#!/usr/bin/env/ python
# coding=utf-8

# 其他文件IO函数的使用
fileHandler = open('E:/data/test.txt', 'a+')  # 以读写方式处理文件IO
fileHandler.seek(0)

# 读取整个文件
contents = fileHandler.read()
print(contents)

# 读取所有行,再逐行输出
fileHandler.seek(0)
lines = fileHandler.readlines()
for line in lines:
    print(line)

# 当前文件指针的位置
print(fileHandler.tell())

fileHandler.close
