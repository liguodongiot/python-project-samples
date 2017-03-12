#!/usr/bin/env/ python
# coding=utf-8

fileHandler = open('E:/data/test.txt', 'a+')
fileHandler.write("\r\n")
fileHandler.write("thank you")

fileHandler.seek(0)
contents = fileHandler.read()
print(contents)

fileHandler.close
