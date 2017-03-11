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

# 变量和集合
# 数字，字符串，列表，元组，字典，set

# 基本使用
print("----变量基本使用----")
counter = 100           # 整型
miles = 1000.0          # 浮点
name = "John"           # 字符串

print(counter)
print(miles)
print(name)

# 多重赋值
print("----多重赋值----")
a = b = c = 1
d, e, f = 1, 2, "john"

print(str(id(a))+" "+str(id(b))+" "+str(id(c)))

b = 2
print(id(b))

# 字符串
print("----字符串----")

string = 'Hello World!'     # 字符串在python中本质上是一个字符序列Seq

print(string)           # 打印整个字符串
print(string[0])        # 打印字符串第一个字母
print(string[2:5])      # 打印第3到第5个字母
print(string[2:])       # 打印从第3个字母到末尾
print(string * 2)       # 字符串重复2次
print(string + "TEST")  # 字符串拼接

# 列表
print("----列表----")

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

# 元组
# 元组是类似于列表中的序列数据类型，一个元组由数个逗号分隔的值组成。
# 列表和元组之间的主要区别是：列表用方括号[]，列表的长度和元素值是可以改变的
# 而元组用圆括号()，不能被更新。
# 元组可以被认为是只读列表。

print("----元组----")

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)                # 打印整个元组
print(tuple[0])             # 打印第一个元素
print(tuple[1:3])           # 打印第2、3两个元素
print(tuple[2:])            # 打印第3及其之后的元素
print(tinytuple * 2)        # 重复2遍
print(tuple + tinytuple)    # 拼接

# 字典
# Python字典是一种哈希表型。由“键-值”对组成。
# 键可以是任何Python类型，但通常是数字或字符串。
# 值可以是任意Python的对象。
# 字典是由花括号括号{}，可分配值，并用方括号[]访问。

print("----字典----")

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])          # Prints value for 'one' key
print(dict[2])              # Prints value for 2 key
print(tinydict)             # Prints complete dictionary
print(tinydict.keys())      # Prints all the keys
print(tinydict.values())    # Prints all the values

# set

print("----set----")

a = {1, 2, 3, 4, 5}
b = {1, 7, 3, 4, 6}
print(a)

a.remove(3)
print(a)

a.add(6)
print(a)
print(a.union(b))


