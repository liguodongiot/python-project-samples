#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/5/19 10:09
# PythonVersion: 2.7


class BaseListUse:

    # 初始化
    def __init__(self):
        self.base_list = ['html', 'js', 'css', 'python']

    def loop_list(self):
        print(self.base_list)
        print '遍历列表方法：'
        for i in self.base_list:
            print i
            # print ("序号：%s   值：%s" % (list.index(i) + 1, i))

    def loop_list2(self):
        list_str = ['html', 'js', 'css', 'python']
        print '遍历列表方法：'
        for i in list_str:
            print ("序号：%s   值：%s" % (list.index(i) + 1, i))


base_list_use = BaseListUse()
base_list_use.loop_list()
print("----------------")
base_list_use.loop_list2()
