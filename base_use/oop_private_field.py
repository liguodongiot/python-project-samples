#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 私有属性

# 1、类的私有属性
# __private_attrs：两个下划线开头，ivate_attrs

# 2、类的私有方法声明该属性为私有，不能在类地外部被使用或直接访问。
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。
# 在类的内部调用 self.__private_method


class JustCounter:

    __secret_count = 0  # 私有变量
    public_count = 0    # 公开变量

    def count(self):
        self.__secret_count += 1
        self.public_count += 1
        print(self.__secret_count)

counter = JustCounter()
counter.count()
print(counter.public_count)

# print(counter.__secret_count)  # 报错，实例不能访问私有变量
# Python不允许实例化的类访问私有数据，
# 但可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的代码：
print(counter._JustCounter__secret_count)
