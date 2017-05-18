#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 自动翻页https://www.v2ex.com/
# Author: guodong.li 
# DateTime: 2017/5/18 19:44
# PythonVersion: 2.7

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.v2ex.com/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/?tab="]').items():
            self.crawl(each.attr.href, callback=self.tab_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def tab_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/go/"]').items():
            self.crawl(each.attr.href, callback=self.board_page, validate_cert=False)

    @config(priority=2)
    def board_page(self, response):

        for each in response.doc('a[href^="https://www.v2ex.com/t/"]').items():
            url = each.attr.href
            if url.find('#reply') > 0:
                url = url[0:url.find('#')]  # 截取url
            self.crawl(url, callback=self.detail_page, validate_cert=False)

        # 实现自动翻页功能
        for each in response.doc('a.page_normal').items():
            self.crawl(each.attr.href, callback=self.board_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        title = response.doc('h1').text()
        content = response.doc('div.topic_content').html().replace('"', '\\"')
        tmp = zip(response.doc('a[href^="/member/"]').items(), response.doc('div.reply_content').items())
        reply_content = list()
        for e1, e2 in tmp:
            reply_content.append((e1.text(), e2.text()))
        # self.add_question(title, content)  #插入数据库
        return {
            "url": response.url,
            "title": title,
            "content": content,
            "reply_content": reply_content,
        }
