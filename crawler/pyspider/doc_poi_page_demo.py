#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 复杂选择及翻页处理（中国POI数据）
# Author: guodong.li 
# DateTime: 2017/5/18 11:16
# PythonVersion: 2.7

import re
from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.poi86.com/poi/amap/province/330000.html', callback=self.city_page)

    @config(age=24 * 60 * 60)
    def city_page(self, response):
        # 遍历市
        for each in response.doc('body > div:nth-child(2) > div > div.panel-body > ul > li > a').items():
            self.crawl(each.attr.href, callback=self.district_page)

    @config(age=24 * 60 * 60)
    def district_page(self, response):
        # 遍历区县
        for each in response.doc('body > div:nth-child(2) > div > div.panel-body > ul > li > a').items():
            self.crawl(each.attr.href, callback=self.poi_idx_page)

    @config(age=24 * 60 * 60)
    def poi_idx_page(self, response):
        # 遍历店铺
        for each in response.doc('td > a').items():
            self.crawl(each.attr.href, callback=self.poi_dtl_page)
        # 翻页
        for each in response.doc(
                'body > div:nth-child(2) > div > div.panel-body > div > ul > li:nth-child(13) > a').items():
            self.crawl(each.attr.href, callback=self.poi_idx_page)

    @config(priority=100)
    def poi_dtl_page(self, response):
        return {
            "url": response.url,
            "id": re.findall('\d+', response.url)[1],
            "name": response.doc('body > div:nth-child(2) > div:nth-child(2) > div.panel-heading > h1').text(),
            "province": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(1) > a').text(),
            "city": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(2) > a').text(),
            "district": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(3) > a').text(),
            "addr": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(4)').text(),
            "tel": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(5)').text(),
            "type": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(6)').text(),
            "dd_map": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(7)').text(),
            "hx_map": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(8)').text(),
            "bd_map": response.doc(
                'body > div:nth-child(2) > div:nth-child(2) > div.panel-body > ul > li:nth-child(9)').text(),
        }

