# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.并发爬虫程序.py
# @Software: PyCharm
# @Time    : 2023/11/20 20:34

import time
import requests
import threading


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

thread_obj_list = list()
for image_url in url_list:
    # args接收的是一个元组类型, 任务参数要放在一个元组容器内
    t = threading.Thread(target=get_images, args=(image_url,))
    thread_obj_list.append(t)
    t.start()

for t_obj in thread_obj_list:
    t_obj.join()  # 通过线程对象调用join方法让主线程等待子线程任务执行完毕执行才能继续向下执行

end = time.time()
print('耗时:', end - start)

"""
python中的多线程是一种并发程序而不是并行程序
    并发程序: 在同一时间内, 只有一个线程在执行任务, 其他线程挂起等待
    并行任务: 在同一时间内, 有多个任务利用cpu多核机制共同完成多个任务
"""

