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


# 浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
# 开始的URL地址
all_url = 'http://www.mzitu.com/all'
# 使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头
start_html = requests.get(all_url,  headers=headers)
# 打印出start_html (请注意，concent是二进制的数据，
# 一般用于下载图片、视频、音频等多媒体内容是才使用concent, 对于打印网页内容请使用text)
# print(start_html.text)

####################

# 使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 ）
Soup = BeautifulSoup(start_html.text, 'lxml')
# 使用BeautifulSoup解析网页过后就可以用找标签呐！
# （find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
# li_list = Soup.find_all('li')
# for li in li_list:
#     print(li)

####################

# 意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
all_a = Soup.find('div', class_='all').find_all('a')
# for a in all_a:
#     print(a)

# ‘find’ 只查找给定的标签一次，就算后面还有一样的标签也不会提取出来哦！
# 而‘find_all’是在页面中找出所有给定的标签！

####################

# for a in all_a:
#     # 取出a标签的文本
#     title = a.get_text()
#     # 取出a标签的href 属性
#     href = a['href']
#     print(title, href)

####################

for a in all_a:
    # 取出a标签的文本
    title = a.get_text()
    # 去掉空格
    path = str(title).strip()
    # 创建一个存放套图的文件夹
    os.makedirs(os.path.join("D:\\mzitu", path))
    # 切换到上面创建的文件夹
    os.chdir("D:\\mzitu\\" + path)
    # 取出a标签的href 属性
    href = a['href']
    html = requests.get(href, headers=headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    # 查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span)+1):
        page_url = href + '/' + str(page)
        # 这个page_url就是每张图片的页面地址啦！但还不是实际地址！
        # print(page_url)
        # 打印jpg
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src']
        # print(img_url)

        # 取URL 倒数第四至第九位做图片的名字
        name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers)
        # 写入多媒体文件必须要 b 这个参数！！必须要！！
        f = open(name+'.jpg', 'ab')
        # 多媒体文件要是用conctent
        f.write(img.content)
        f.close()


