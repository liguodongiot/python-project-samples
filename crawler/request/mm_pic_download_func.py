#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: liguodong
# DateTime: 2017/5/13 19:45
# PythonVersion: 3.6

import requests  # 导入requests
# 导入bs4中的BeautifulSoup
from bs4 import BeautifulSoup
import os


class download_mz_pic():

    def request_url(self, url, headers):
        content = requests.get(url, headers=headers)
        return content

    def mk_dir(self, target_mkdir, path):
        path = path.strip()
        is_exists = os.path.exists(os.path.join(target_mkdir, path))
        if not is_exists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join(target_mkdir, path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def save(self, img_url, headers):  # 这个函数保存图片
        name = img_url[-9:-4]
        img = self.request_url(img_url, headers)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def html(self, href, headers):  # 这个函数是处理套图地址获得图片的页面地址
        html = self.request_url(href, headers)
        # 获得最大的span值
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url, headers)  # 调用img函数

    def img(self, page_url, headers):  # 这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request_url(page_url, headers)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url, headers)

    def all_url(self, url, headers, target_mkdir):
        html = self.request_url(url, headers)  # 调用request函数把套图地址传进去会返回给我们一个response
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')  # 注意到有个标题带有？这个符号Windows系统是不能创建文件夹的所以要替换掉
            self.mk_dir(target_mkdir, path)  # 调用mkdir函数创建文件夹！这儿path代表的是标题title
            # 切换到上面创建的文件夹
            os.chdir(target_mkdir + path)
            href = a['href']
            self.html(href, headers)  # 调用html函数把href参数传递过去！href是就是套图的地址


# 开始的URL地址
all_url = 'http://www.mzitu.com/all'
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
target_mkdir = "D:\\mzitu\\"

mz_obj = download_mz_pic()  # 实例化
mz_obj.all_url(all_url, header, target_mkdir)  # 给函数all_url传入参数  你可以当作启动爬虫（就是入口）



