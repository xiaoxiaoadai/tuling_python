# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.自定义线程类完成并发任务.py
# @Software: PyCharm
# @Time    : 2023/11/20 21:34

import time
import requests
import threading


class ImageSpider(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    # 重写run方法改变线程绑定任务
    def run(self):
        response = requests.get(self.url).content

        file_name = self.url.rsplit('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response)
            time.sleep(1)
            print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

for image_url in url_list:
    image_spider = ImageSpider(image_url)
    image_spider.start()

"""
run和start之间的关系是什么？
    通过源码的方式发现start方法代码内部其实已经调用了run方法
    
start方法是启动线程方法
run方法才是真正运行绑定任务的方法
"""
