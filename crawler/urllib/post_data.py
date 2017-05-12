#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: liguodong
# Created on 2017-05-11 23:12:48

import urllib
import urllib2

# values = {"username": "215666835@qq.com", "password": "li2guod2133ong34"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print(response.read())

values2 = {}
values2['username'] = "215666835@qq.com"
values2['password'] = "liguodo22ng3222"
data2 = urllib.urlencode(values2)
urlCsdn = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request2 = urllib2.Request(urlCsdn, data2)
response2 = urllib2.urlopen(request2)
print(response2.read())




