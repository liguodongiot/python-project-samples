# 基本语法及其使用

### 行与缩进,变量和集合
**demo**

### 流程控制语句(if,while,for)
**flow_control_stmt**

### 函数(默认参数和可变参数,匿名函数)
**func**

### 模块
```
模块和包
在python中一个文件可以被看成一个独立模块，
而包对应着文件夹，模块把python代码分成一些有组织的代码段，通过导入的方式实现代码重用。

导入模块时，是按照sys.path变量的值搜索模块，
sys.path的值是包含每一个独立路径的列表，
包含当前目录、python安装目录、PYTHONPATH环境变量（一般当前目录优先级最高）。


使用import语句导入模块

有下面两种方式
import module1
import module2
import module3

import module1,module2,module3

这两种方式的效果是一样的，但是第一种可读性比第二种好，推荐按照下面的顺序导入模块，
并且一般在文件首部导入所有的模块：
python标准库
第三方模块
应用程序自定义模块
也可以在函数内部导入模块，这样被导入的模块作用域是局部的。


使用from-import语句导入模块的属性
单行导入
from module import name1,name2,name3

多行导入
from module import name1,name2,\
                   name3

导入全部属性（由于容易覆盖当前名称空间中现有的名字，所以一般不推荐使用，
适合模块中变量名很长并且变量很多的情况）
from module import *

如果你不想某个模块的属性被以上方法导入，可以给该属性名称前加一个下划线(_test)，
如果需要取消隐藏，可以显示的导入该属性（from module import _test）

扩展的import语句
使用自定义的名称替换模块的原始名称
import simplejson as json
模块被导入时，加载的时候模块顶层代码会被执行，如：设定全局变量、类和函数的声明等，
所以应该把代码尽量封装到类和函数中。一个模块无论被导入多少次，只加载一次，可以防止多次导入时代码被多次执行。

重新导入模块
reload(module)
内建函数reload可以重新导入一个已经存在的模块

包结构

包将有联系的模块组织在一起，有效避免模块名称冲突问题，让应用组织结构更加清晰。

一个普通的python应用程序目录结构：
app/
__init__.py
    a/
    __init__.py
    a.py
    b/
    __init__.py
    b.py

app是最顶层的包，a和b是它的子包，可以这样导入：

from app.a import a
from app.b.b import test

a.test()
test()
上面代码表示：导入app包的子包a和子包b的属性test，然后分别调用test方法。

__init__.py的作用
每个目录下都有__init__.py文件，这个是初始化模块，from-import语句导入子包时需要它，
可以在里面做一些初始化工作，也可以是空文件。
ps：__init__.py定义的属性直接使用 顶层包.子包 的方式导入，如在目录a的__init__.py文件中定义init_db()方法，
调用如下：
from app import a
a.init_db()

指定python文件编码方式
python默认是使用ASCII编码，可以指定编码方式，如
#!/usr/bin/env python
#coding=utf-8
或者
#!/usr/bin/env python
# -*- coding:utf-8 -*-

解决导入循环问题
有下面两个模块，a.py和b.py
a.py
#!/usr/bin/env python
#coding=utf-8

import b
if __name__ == '__main':
    print 'hello,I'm a'

b.py
#!/usr/bin/env python
#coding=utf-8

import a
if __name__ == '__main':
    print 'hello,I'm b'

在这里a尝试导入b，而b也尝试导入a，导入一个先前没有完全导入的模块，会导致导入失败。
解决办法：移除一个导入语句，把导入语句放到函数内部，在需要的时候导入。
b.py
#!/usr/bin/env python
#coding=utf-8

if __name__ == '__main':
    import a
    print 'hello,I'm b'

```
**module_support**
**module_main**


### 文件IO
```
文件读写
Python进行文件读写的函数为open或file:
file_handler = open(filename,,mode）

open mode
w	以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
a	以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
r+	以读写方式打开文件，可对文件进行读和写操作。
w+	消除文件内容，然后以读写方式打开文件。
a+	以读写方式打开文件，并把文件指针移到文件尾。
b	以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。

操作文件对象方法
f.close()	    关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
f.fileno()	    获得文件描述符，是一个数字
f.flush()	    刷新输出缓存
f.isatty()	    如果文件是一个交互终端，则返回True，否则返回False。
f.read([count])	读出文件，如果有count，则读出count个字节。
f.readline()	读出一行信息。
f.readlines()	读出所有行，也就是读出整个文件的信息。
f.seek(offset[,where])	把文件指针移动到相对于where的offset位置。where为0表示文件开始处，这是默认值 ；1表示当前位置；2表示文件结尾。
f.tell()	            获得文件指针位置。
f.truncate([size])	    截取文件，使文件的大小为size。
f.write(string)	        把string字符串写入文件。
f.writelines(list)	    把list中的字符串一行一行地写入文件，是连续写入文件，没有换行。

文件夹相关操作
Python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。
得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
返回指定目录下的所有文件和目录名:os.listdir()
删除一个文件:os.remove()
删除多个目录（只能删除空目录）：os.removedirs（r”c：\python”）
检验给出的路径是否是一个文件：os.path.isfile()
检验给出的路径是否是一个目录：os.path.isdir()
判断是否是绝对路径：os.path.isabs()
检验给出的路径是否存在:os.path.exists()
返回一个路径的目录名和文件名:os.path.split()
   
eg：
os.path.split('/home/swaroop/byte/code/poem.txt')
结果：('/home/swaroop/byte/code', 'poem.txt') 
分离扩展名：os.path.splitext()
获取路径名：os.path.dirname()
获取文件名：os.path.basename()
运行shell命令: os.system()
读取和设置环境变量:os.getenv() 与os.putenv()
给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
指示你正在使用的平台：os.name          对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
重命名：os.rename（old， new）
创建多级目录：os.makedirs（r“c：\python\test”）
创建单个目录：os.mkdir（“test”）
获取文件属性：os.stat（file）
修改文件权限与时间戳：os.chmod（file）
终止当前进程：os.exit（）
获取文件大小：os.path.getsize（filename）
```


### 多线程
```
Python中的多线程是伪线程；
不能充分利用cpu中的多核，但是在io等待型的场景下多线程还是可以提高效率。
Python中的多线程有多种实现方式，利用threading包实现是比较普遍的做法。
```
**thread_main**