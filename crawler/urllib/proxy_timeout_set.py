#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: Proxy（代理）的设置
# Author: guodong.li 
# DateTime: 2017/5/12 18:48

import urllib2
import urllib

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)


# 第三个参数就是timeout的设置，可以设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响。
# 如果第二个参数data为空那么要特别指定是timeout是多少，写明形参，如果data已经传入，则不必声明。
response = urllib2.urlopen('https://github.com/', timeout=10)

# response = urllib2.urlopen('http://www.baidu.com',data, 10)

print("----------------------------")
# 使用HTTP的PUT和DELETE方法
# http协议有六种请求方法，get, head, put, delete, post, options，我们有时候需要用到PUT方式或者DELETE方式请求。

# PUT：这个方法比较少见。HTML表单也不支持这个。本质上来讲， PUT和POST极为相似，都是向服务器发送数据，
# 但它们之间有一个重要区别，PUT通常指定了资源的存放位置，而POST则没有，POST的数据存放位置由服务器自己决定。
# DELETE：删除某一个资源。基本上这个也很少见，不过还是有一些地方比如amazon的S3云服务里面就用的这个方法来删除资源。

# 如果要使用HTTP,PUT和DELETE ，只能使用比较低层的httplib库。虽然如此，我们还是能通过下面的方式，使
# urllib2能够发出PUT或DELETE的请求。

# request = urllib2.Request(uri, data=data)
# request.get_method = lambda: 'PUT'  # or 'DELETE'
# response = urllib2.urlopen(request)

print("----------------------------")
# 下面的方法把 Debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

