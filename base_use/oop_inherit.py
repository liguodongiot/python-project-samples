#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 类的继承
# 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
# 继承完全可以理解成类之间的类型和子类型关系。

# 派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后。


class Parent:        # 定义父类
    parent_attr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parent_method(self):
        print('调用父类方法')

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print("父类属性 :", Parent.parent_attr)

    def my_method(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类

    def __init__(self):
        print("调用子类构造方法")

    def child_method(self):
        print('调用子类方法 child method')

    def my_method(self):
        print('调用子类方法')

c = Child()             # 实例化子类
c.child_method()        # 调用子类的方法
c.parent_method()       # 调用父类方法
c.set_attr(200)         # 再次调用父类的方法
c.get_attr()            # 再次调用父类的方法

c.my_method()           # 子类调用重写方法

# 继承多个类
# class A:          # 定义类 A
# class B:          # 定义类 B

# class C(A, B):    # 继承类 A 和 B

# 可以使用issubclass()或者isinstance()方法来检测。
# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。


# 基础重载方法
# 下表列出了一些通用的功能，你可以在自己的类重写：
# __init__ ( self [,args...] )
# 构造函数
# 简单的调用方法: obj = className(args)

# __del__( self )
# 析构方法, 删除一个对象
# 简单的调用方法 : dell obj

# __str__( self )
# 用于将值转化为适于人阅读的形式
# 简单的调用方法 : str(obj)

# __cmp__ ( self, x )
# 对象比较
# 简单的调用方法 : cmp(obj, x)

class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 + v2)
