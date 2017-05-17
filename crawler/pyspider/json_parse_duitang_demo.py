#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 解析JSON数据(堆糖网站示例)
# Author: guodong.li 
# DateTime: 2017/5/17 10:44
# PythonVersion: 2.7

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.duitang.com/napi/friendship/fans/?start=0&limit=1000&user_id=116965',
                   callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.json['data']['object_list']:
            id = each['id']
            self.crawl('http://www.duitang.com/napi/friendship/fans/?start=0&limit=1000&user_id=' + str(id),
                       callback=self.index_page)
            # 个人详情页
            self.crawl('http://www.duitang.com/napi/people/profile/?user_id=' + str(id),
                       callback=self.detail_page)

        start = response.json['data']['next_start']
        total = response.json['data']['total']
        user = response.json['data']['visit_user']['user_id']
        if start < total:
            self.crawl(
                'http://www.duitang.com/napi/friendship/fans/?start=' + str(start) + '&limit=1000&user_id=' + str(user),
                callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "username": response.json['data']['username'],
            "id": response.json['data']['id']
        }

