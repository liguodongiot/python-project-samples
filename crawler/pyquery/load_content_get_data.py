#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 根据索引获取元素，根据类名和ID获取元素
# Author: liguodong
# DateTime: 2017/5/17 8:17
# PythonVersion: 3.6

from pyquery import PyQuery as pq

# 可以从字符串，文件或URL加载HTML内容
doc_1 = pq("<html><head><body><h1>Hello</h1></body></head></html>")
doc_2 = pq(filename="hello.html")
doc_3 = pq(url="http://www.baidu.com")

# 根据HTML标签来获得元素
doc_1 = pq("<html><head><body><h1>Hello</h1><h2>World</h2><p>test1</p><p>test2</p></body></head></html>")
print(doc_1('head'))   # <head><body><h1>Hello</h1></body></head>
print(doc_1('h1'))   # <h1>Hello</h1>

print("---------------------")

# 获取HTML块或文本块 使用html()和text()
print(doc_1('head').html())  # <body><h1>Hello</h1></body>
print(doc_1('head').text())  # Hello World

# 从索引获取元素 eq(index)
html_content = """
<html>
    <head>
        <body>
            <h1>Hello</h1>
            <h2>World</h2>
            <p>test1</p>
            <p>test2</p>
        </body>
    </head>
</html>
"""
doc_format = pq(html_content)
print(doc_format('p').eq(0).html())   # test1
print(doc_format('p').eq(1).html())   # test2

# 根据类名和id获取元素
doc_html = pq("<html><head><body><div class='div1'><p id='2'>test1</p></div></body></head></html>")
print(doc_html('div.div1').html())   # <p id="2">test1</p>
print(doc_html('.div1').html())   # <p id="2">test1</p>
print(doc_html('p#2').html())   # test1
print(doc_html('#2').html())   # test1

print("-------------------")
# 获取属性值
doc_attr = pq("<html><head><body><div class='div1'><a href='http://abc.com'>test1</a></div></body></head></html>")
print(doc_attr('div').attr('class'))  # div1
print(doc_attr('a').attr('href'))   # http://abc.com

# 修改属性值
print(doc_attr('a').attr('href', 'http://www.google.com'))   # 将href属性修改为google的地址

# 查找嵌套元素find()
doc_nest = pq("<html><head><body><div class='div1'><a href='http://abc.com'>test1</a></body></head></html>")
print(doc_nest('div').find('a'))  # <a href="http://abc.com">test1</a>

# 获取子元素
html_context = """
<html><head><body><div class='div1'><p id='1'>test1</p><a href='http://abc.com'>test2</a></div></body></head></html>
"""
doc_child = pq(html_context)
print(doc_child('div').children())     # <p id="1">test1</p><a href="http://abc.com">test2</a>
print(doc_child('div').children('a'))  # <a href="http://abc.com">test2</a>

# 获取父元素
print(doc_child('a').parents())   # 所有的HTML内容
print(doc_child('a').parents('div'))  # <div class="div1"><p id="1">test1</p><a href="http://abc.com">test2</a></div>

# 为元素添加类
html_class = """
<html><head><body><div><p id='1'>test1</p><a href='http://abc.com'>test2</a></div></body></head></html>
"""
doc_class = pq(html_class)
# <div class="divClass"><p id="1">test1</p><a href="http://abc.com">test2</a></div>
print(doc_class('div').addClass('divClass'))

# 判断元素是否有给定的类
html_class_no = """
<html><head><body><div><p id='1'>test1</p><a href='http://abc.com'>test2</a></div></body></head></html>
"""
doc_class_no = pq(html_class_no)
print(doc_class_no('div').hasClass('div1'))   # False
print(doc_class_no('div').addClass('div1'))
# <div class="div1"><p id="1">test1</p><a href="http://abc.com">test2</a></div>
print(doc_class_no('div').hasClass('div1'))   # True
