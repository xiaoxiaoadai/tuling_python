# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.同步爬虫程序.py
# @Software: PyCharm
# @Time    : 2023/11/20 20:28


import time
import requests


def get_images(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        time.sleep(1)
        print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

start = time.time()
for image_url in url_list:
    get_images(image_url)
end = time.time()
print('耗时:', end - start)



