#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 搜索引擎爬取(github)
# Author: guodong.li 
# DateTime: 2017/5/18 18:32
# PythonVersion: 2.7

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        list = ['douyu', 'panda', 'zhanqi', 'longzhu', 'huya', 'yy', 'momo', 'tv']
        for q in list:
            url = 'https://github.com/search?p=1&q=' + q + '&type=Code&utf8'
            self.crawl(url, callback=self.index_page, validate_cert=False)

    @config(age=1)
    def index_page(self, response):
        self.crawl(response.doc('.next_page').attr.href, callback=self.index_page, validate_cert=False)
        flag = 0
        for each in response.doc('.title > a').items():
            flag += 1
            if flag % 2 == 0:
                self.crawl(each.attr.href, callback=self.into_page, validate_cert=False)

    @config(age=1, etag=True)
    def into_page(self, response):
        for each in response.doc('table').items():
            return {
                "app": "githack",
                "origin": "github.net",
                "code": each.text(),
            }



