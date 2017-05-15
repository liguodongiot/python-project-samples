#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 完善 domain_page 代码，实现保存简介和遍历保存图片的方法,
#           按照淘宝MM姓名分文件夹，存储MM的 txt 文本简介以及所有美图至本地。
# Author: guodong.li 
# DateTime: 2017/5/12 17:27

from pyspider.libs.base_handler import *
import os

PAGE_START = 1
PAGE_END = 2
DIR_PATH = 'D:/down_pic/'


class Handler(BaseHandler):
    crawl_config = {
    }

    # 初始化
    def __init__(self):
        self.base_url = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.page_num = PAGE_START
        self.total_num = PAGE_END
        self.deal = Deal()

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
        # 获取姓名
        name = response.doc('.mm-p-model-info-left-top dd > a').text()
        dir_path = self.deal.mk_dir(name)
        # 获取MM简介
        brief = response.doc('.mm-aixiu-content').text()
        if dir_path:
            # 获取照片链接
            imgs = response.doc('.mm-aixiu-content img').items()
            count = 1
            # 保存简介
            self.deal.save_brief(brief, dir_path, name)
            for img in imgs:
                url = img.attr.src
                if url:
                    extension = self.deal.get_extension(url)
                    file_name = name + str(count) + '.' + extension
                    count += 1
                    self.crawl(img.attr.src, callback=self.save_img,
                               save={'dir_path': dir_path, 'file_name': file_name}, validate_cert=False)

    def save_img(self, response):
        content = response.content
        dir_path = response.save['dir_path']
        file_name = response.save['file_name']
        file_path = dir_path + '/' + file_name
        self.deal.save_img(content, file_path)


class Deal:
    """
        mk_dir：创建文件夹，用来创建 MM 名字对应的文件夹。
        save_brief: 保存简介，保存 MM 的文字简介。
        save_img: 传入图片二进制流以及保存路径，存储图片。
        get_extension: 获得链接的后缀名，通过图片 URL 获得。
    """

    def __init__(self):
        self.path = DIR_PATH
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def mk_dir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path

    def save_img(self, content, path):
        f = open(path, 'wb')
        f.write(content)
        f.close()

    def save_brief(self, content, dir_path, name):
        file_name = dir_path + "/" + name + ".txt"
        f = open(file_name, "w+")
        f.write(content.encode('utf-8'))

    def get_extension(self, url):
        extension = url.split('.')[-1]
        return extension
