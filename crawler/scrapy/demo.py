#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: liguodong
# DateTime: 2017/5/13 14:55
# PythonVersion: 3.6

import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://dmoztools.net/Home/Apartment_Living/',
        'http://dmoztools.net/Home/Entertaining/'
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

print("test")

