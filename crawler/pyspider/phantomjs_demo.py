#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 利用phantomjs解决js问题（www.sciencedirect.com网站示例）
# Author: guodong.li 
# DateTime: 2017/5/17 9:50
# PythonVersion: 2.7

import re
from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    """
    this is a sample handler
    """
    crawl_config = {
        "headers": {
            "User-Agent": "BaiDu_Spider",
        },
        "timeout": 300,
        "connect_timeout": 100
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.sciencedirect.com/science/article/pii/S1568494612005741',
                   timeout=300,
                   connect_timeout=100,
                   callback=self.detail_page)
        self.crawl('http://www.sciencedirect.com/science/article/pii/S0167739X12000581',
                   timeout=300,
                   connect_timeout=100,
                   age=0,
                   callback=self.detail_page)
        self.crawl('http://www.sciencedirect.com/science/journal/09659978',
                   timeout=300,
                   connect_timeout=100,
                   callback=self.index_page)

    @config(fetch_type="js", age=0)
    def index_page(self, response):
        for each in response.doc('a').items():
            url = each.attr.href
            # print(url)
            if url is not None:
                if re.match('http://www.sciencedirect.com/science/article/pii/\w+$', url):
                    self.crawl(url, callback=self.detail_page, timeout=300, connect_timeout=100)

    @config(fetch_type="js")
    def detail_page(self, response):
        self.index_page(response)
        self.crawl(response.doc('#relArtList > li > .cLink').attr.href,
                   callback=self.index_page,
                   timeout=300,
                   connect_timeout=100)

        return {
            "url": response.url,
            "title": response.doc('.svTitle').text(),
            "authors": [x.text() for x in response.doc('.authorName').items()],
            "abstract": response.doc('.svAbstract > p').text(),
            "keywords": [x.text() for x in response.doc('.keyword span').items()],
        }
