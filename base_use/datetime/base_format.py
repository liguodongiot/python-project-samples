#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/5/16 9:48
# PythonVersion: 2.7

from datetime import datetime as dt

# 日期时间格式
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
date_str = "2017-05-16 09:19:56"
publish_time = dt.strptime(date_str, DATE_FORMAT)
print(publish_time)
print(type(publish_time))
