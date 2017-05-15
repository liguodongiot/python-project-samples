#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: Mysql数据库基本使用
# Author: guodong.li 
# DateTime: 2017/5/15 15:05
# PythonVersion: 2.7

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "db_lgd_demo")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
print "Database version : %s " % data

# 关闭数据库连接
db.close()
