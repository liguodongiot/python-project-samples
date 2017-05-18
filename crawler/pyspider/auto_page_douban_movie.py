#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/5/18 20:03
# PythonVersion: 2.7

from pyspider.libs.base_handler import *


class Handler(BaseHandler):

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://movie.douban.com/tag/', callback=self.index_page, validate_cert=False)

    @config(age=24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if 'tag' in each.attr.href:
                self.crawl(each.attr.href, callback=self.list_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60, priority=2)
    def list_page(self, response):
        for each in response.doc(
                'HTML>BODY>DIV#wrapper>DIV#content>DIV.grid-16-8.clearfix>DIV.article>DIV>TABLE TR.item>TD>DIV.pl2>A').items():
            self.crawl(each.attr.href, priority=9, callback=self.detail_page, validate_cert=False)
        # 翻页
        for each in response.doc(
                'HTML>BODY>DIV#wrapper>DIV#content>DIV.grid-16-8.clearfix>DIV.article>DIV.paginator>A').items():
            self.crawl(each.attr.href, callback=self.list_page, validate_cert=False)

    @config(priority=3)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('HTML>BODY>DIV#wrapper>DIV#content>H1>SPAN').text(),
            "rating": response.doc(
                '#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong').text(),
            "导演": [x.text() for x in response.doc('a[rel="v:directedBy"]').items()],
        }
