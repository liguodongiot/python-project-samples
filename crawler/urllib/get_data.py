#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: guodong.li 
# DateTime: 2017/5/12 11:11

import urllib
import urllib2

values = {}
values['username'] = "215666835@qq.com"
values['password'] = "32243235"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)

# URL+编码后的参数
print(geturl)
print(response.read())

