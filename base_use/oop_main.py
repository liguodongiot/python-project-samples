#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee:  # 所有员工的基类
    "所有员工的基类"
    emp_count = 0

    # 构造函数
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print("Total Employee %d" % Employee.emp_count)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# emp_count 变量是一个类变量，它的值将在这个类的所有实例之间共享。
# 你可以在内部类或外部类使用Employee.emp_count 访问。
# 第一个方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，
# 当创建了这个类的实例时就会调用该方法。

# 类的方法
# 使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数。

# 创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数。

# 创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)

# 创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

# 可以使用点(.)来访问对象的属性。使用如下类的名称访问类变量:
emp1.display_employee()
emp2.display_employee()

print("Total Employee %d" % Employee.emp_count)

# 添加，删除，修改类的属性

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性

# 也可以使用以下函数的方式来访问属性：
# getattr(obj, ‘name’[, default])   : 访问对象的属性。
# hasattr(obj,’name’)               : 检查是否存在一个属性。
# setattr(obj,’name’,value)         : 设置一个属性。如果属性不存在，会创建一个新属性。
# delattr(obj, ‘name’)              : 删除属性。

print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
setattr(emp1, 'age', 8)   # 添加属性 'age' 值为 8
print(getattr(emp1, 'age'))    # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'

# 内置类属性
# __dict__      : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__       : 类的文档字符串
# __name__      : 类名
# __module__    : 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# __bases__     : 类的所有父类构成元素（包含了以个由所有父类组成的元组）

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

