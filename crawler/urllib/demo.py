#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2

urlLink = 'https://www.baidu.com/'
filename = urllib.urlretrieve(urlLink)
print(type(filename))
print(filename)

# urlopen(url, data, timeout)
# 第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
# 第二三个参数是可以不传送的，data默认为空None，timeout默认为socket._GLOBAL_DEFAULT_TIMEOUT。
response = urllib2.urlopen(urlLink)

# response对象有一个read方法，可以返回获取到的网页内容。
print(response.read())

print("~~~~~~~~~~~~~~~~~~~~")

# 推荐大家这么写，因为在构建请求时还需要加入好多内容，
# 通过构建一个request，服务器响应请求得到应答，这样显得逻辑上清晰明确。
request2 = urllib2.Request(urlLink)
response2 = urllib2.urlopen(request2)
print(response2.read())





