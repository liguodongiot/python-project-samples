#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 用PyQuery解析页面数据（豆瓣电影）
# Author: guodong.li 
# DateTime: 2017/5/17 13:51
# PythonVersion: 2.7

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://movie.douban.com/tag/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.tagCol a').items():
            self.crawl(each.attr.href, callback=self.list_tag_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def list_tag_page(self, response):
        all_link = response.doc('.more-links')
        self.crawl(all_link.attr.href, callback=self.list_page, validate_cert=False)

    @config(age=10*24*60*60)
    def list_page(self, response):
        # 处理当前页
        for each in response.doc('.title').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)
        # craw the next page 抓取下一页
        next_page = response.doc('.next > a')
        self.crawl(next_page.attr.href, callback=self.list_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        director = ''
        for item in response.doc('#info > span > .pl'):
            if item.text == u'导演':
                next_item = item.getnext()
                director = next_item.getchildren()[0].text
                break
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "director": director,
        }

