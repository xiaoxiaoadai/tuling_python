# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.给进程对象绑定的任务传递参数.py
# @Software: PyCharm
# @Time    : 2023/11/24 20:41

import time
import requests
import multiprocessing


def get_images(image_url):
    response = requests.get(image_url).content

    file_name = image_url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        time.sleep(1)
        print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]


if __name__ == '__main__':
    for url in url_list:
        p = multiprocessing.Process(target=get_images, args=(url,))
        p.start()
