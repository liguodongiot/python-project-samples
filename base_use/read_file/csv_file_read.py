#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 读写CSV文件
# Author: guodong.li 
# DateTime: 2017/6/16 9:22
# PythonVersion: 2.7

import csv

csv_reader = csv.reader(open('d:\\test.csv'))
for row in csv_reader:
    print(row[1].decode('GBK'))

print("-------")

with open('d:\\test.csv', 'rb') as f:  # 采用b的方式处理可以省去很多问题
    reader = csv.reader(f)
    for row in reader:
        print(row[1].decode('GBK'))


print("-----------")

listcsv = [1, 2, 3]
with open('d:\\some.csv', 'wb') as f:   # 采用b的方式处理可以省去很多问题
    writer = csv.writer(f)
    writer.writerow(listcsv)

with open('d:\\some2.csv', 'wb') as f:   # 采用b的方式处理可以省去很多问题
    writer = csv.writer(f)
    writer.writerows([listcsv])

