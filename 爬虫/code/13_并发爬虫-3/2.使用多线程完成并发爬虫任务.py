# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.使用多线程完成并发爬虫任务.py
# @Software: PyCharm
# @Time    : 2023/11/11 21:14


import requests
import threading
from lxml import etree

url = 'https://movie.douban.com/top250?start={}&filter='
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def get_movie_info(page):
    response = requests.get(url.format(page * 25), headers=headers).text
    tree = etree.HTML(response)
    result = tree.xpath("//div[@class='hd']/a/span[1]/text()")
    print(result)


if __name__ == '__main__':
    thread_obj_list = [threading.Thread(target=get_movie_info, args=(page,)) for page in range(10)]
    for thread_obj in thread_obj_list:
        thread_obj.start()
