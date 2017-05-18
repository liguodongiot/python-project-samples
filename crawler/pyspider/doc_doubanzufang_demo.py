#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 用PyQuery解析页面数据（豆瓣租房）
# Author: guodong.li
# DateTime: 2017/5/17 12:46
# PythonVersion: 2.7

from pyspider.libs.base_handler import *

groups = {
    '上海租房': 'https://www.douban.com/group/shanghaizufang/discussion?start=',
    '上海租房@长宁租房/徐汇/静安租房': 'https://www.douban.com/group/zufan/discussion?start=',
    '上海短租日租小组 ': 'https://www.douban.com/group/chuzu/discussion?start=',
    '上海短租': 'https://www.douban.com/group/275832/discussion?start=',
}


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        for i in groups:
            url = groups[i] + '0'
            self.crawl(url, callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.olt .title a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

        # next page
        for each in response.doc('.next a').items():
            self.crawl(each.attr.href, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        count_not = 0
        notlist = []
        for i in response.doc('.bg-img-green a').items():
            if i.text() != response.doc('.from a').text():
                count_not += 1
                notlist.append(i.text())
        for i in notlist: print i

        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "author": response.doc('.from a').text(),
            "time": response.doc('.color-green').text(),
            "content": response.doc('#link-report p').text(),
            "回应数": len([x.text() for x in response.doc('h4').items()]),
            # "最后回帖时间": [x for x in response.doc('.pubtime').items()][-1].text(),
            "非lz回帖数": count_not,
            "非lz回帖人数": len(set(notlist)),
            # "主演": [x.text() for x in response.doc('.actor a').items()],
        }
