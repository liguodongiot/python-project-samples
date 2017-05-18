#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 搜索引擎爬取(gitlab)
# Author: guodong.li 
# DateTime: 2017/5/18 18:28
# PythonVersion: 2.7

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        list = ['bigsec', 'password', 'email', 'tongdun', 'vpn', 'address', 'pop3',
                'smtp', 'imap', 'zhengxin', 'jdbc', 'mysql', 'credit', 'access_token', 'client_secret',
                'privatekey', 'secret_key', 'xiecheng', 'ctrip', 'tongcheng']
        for u in list:
            url = 'https://gitlab.com/search?group_id=&scope=issues&search=' + u
            self.crawl(url, callback=self.index_page, validate_cert=False)

    @config(age=10)
    def index_page(self, response):
        self.crawl(response.doc('.next > a').attr.href, callback=self.index_page)
        for each in response.doc('h4 > a[href^="http"]').items():
            # print each.text()
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(etag=True)
    def detail_page(self, response):
        for each in response.doc('.detail-page-description').items():
            return {
                "app": "githack",
                "origin": "gitlab.net",
                "code": each.text(),
            }


