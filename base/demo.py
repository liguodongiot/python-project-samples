#!/usr/bin/env python
# encoding=utf-8

# 行与缩进

if True:
    print("True")
else:
    print("False")

print("-------")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
print("False")

print("-------")

# 三重引号可以用于跨越多个行的字符串。

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print(paragraph)

print("-------")

# 一个语句的结束不需要使用分号
# 如果想在一行中输入多个语句，可使用分号

import sys; x = 'foo';sys.stdout.write(x + """
""")

print("-------")

# 变量和集合

# 基本使用
counter = 100          # 整型
miles = 1000.0       # 浮点
name = "John"      # 字符串

print(counter)
print(miles)
print(name)

print("-------")

# 多重赋值

a = b = c = 1
d, e, f = 1, 2, "john"

print(str(id(a))+" "+str(id(b))+" "+str(id(c)))

b = 2
print(id(b))

print("-------")

# 字符串

string = 'Hello World!'     # 字符串在python中本质上是一个字符序列Seq

print(string)           # 打印整个字符串
print(string[0])        # 打印字符串第一个字母
print(string[2:5])      # 打印第3到第5个字母
print(string[2:])       # 打印从第3个字母到末尾
print(string * 2)       # 字符串重复2次
print(string + "TEST")  # 字符串拼接

print("-------")

# 列表

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)             # 打印整个列表
print(list[0])          # 打印第一个元素
print(list[1:3])        # 打印第二和第三个元素
print(list[2:])         # 打印第三个元素到末尾
print(tinylist * 2)     # 打印2次
print(list + tinylist)  # 拼接两个list

# 修改list中的元素
list[0] = "python"
print(list)

print("-------")

# 元组


