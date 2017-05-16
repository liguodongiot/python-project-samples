#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe:
# Author: liguodong
# DateTime: 2017/5/16 8:04
# PythonVersion: 3.6

from pyquery import PyQuery as pq


doc = pq(filename='hello.html')
print(doc.html())
print(type(doc))
li = doc('li')
print(type(li))
print(li.text())

print("------------------------")

# 完全按照 jQuery 的语法来进行 PyQuery 的操作
p = pq('<p id="hello" class="hello"></p>')('p')
print(p.attr("id"))
print(p.attr("id", "plop"))
print(p.attr("id", "hello"))

print("------------------------")

p = pq('<p id="hello" class="hello"></p>')('p')
print(p.addClass('beauty'))
print(p.removeClass('hello'))
print(p.css('font-size', '16px'))
print(p.css({'background-color': 'yellow'}))
# 这是一连串的操作，而 p 是一直在原来的结果上变化的。因此执行上述操作之后，p 本身也发生了变化。

print("------------------------")

# DOM操作
p = pq('<p id="hello" class="hello"></p>')('p')
print(p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>'))
print(p.prepend('Oh yes!'))
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
p.prependTo(d('#test'))
print(p)
print(d)
d.empty()
print(d)

print("------------------------")

# 遍历用到 items 方法返回对象列表，或者用 lambda
doc = pq(filename='hello.html')
lis = doc('li')
for li in lis.items():
    print(li.html())

print(lis.each(lambda e: e))

print("------------------------")

# 网页请求
# PyQuery 本身还有网页请求功能，而且会把请求下来的网页代码转为 PyQuery 对象。
print(pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'}))
print(pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True))

