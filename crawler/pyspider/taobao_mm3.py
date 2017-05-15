#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: MM个性域名
# Author: guodong.li 
# DateTime: 2017/5/12 17:27

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    # 初始化
    def __init__(self):
        self.base_url = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.page_num = 1
        self.total_num = 30

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            print url
            self.crawl(url, callback=self.index_page, validate_cert=False)
            self.page_num += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.lady-name').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js', validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        domain = 'https:' + response.doc('.mm-p-domain-info li > span').text()
        print domain
        self.crawl(domain, callback=self.domain_page, validate_cert=False)

    def domain_page(self, response):
        pass
