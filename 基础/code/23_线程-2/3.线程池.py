# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.线程池.py
# @Software: PyCharm
# @Time    : 2023/11/22 20:25


"""
在python中创建线程池使用的是concurrent标准库
    多任务的api: concurrent
        统一了线程池和进程池的调用方法
"""
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed, wait


def get_images(url):
    response = requests.get(url).content

    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        time.sleep(1)
        print('下载完成...')
    return 1


# max_workers: 定义最大线程数
pool = ThreadPoolExecutor(max_workers=10)

url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

# for img_url in url_list:
#     # submit需要接受两个参数: 1. 绑定的任务 2. 当前任务需要的参数
#     pool.submit(get_images, img_url)
#
# for res in pool.map(get_images, url_list):
#     print(res)  # 获取当前任务函数的返回值


futures = [pool.submit(get_images, img_url) for img_url in url_list]
wait(futures)  # 等待线程池中的所有方法全部完成之后主线程接堵塞
print('主线程结束...')

# 同步的
# for future in futures:
#     # submit提交任务之后会返回一个future对象, 这个对象包含线程对象的运行状态以及当前这个任务的返回值
#     print(future.result())
#
# for future in as_completed(futures):
#     print(future.result())

"""
1. 如何创建一个线程池对象
2. 设置最大线程数
3. 如何向线程池提交任务
4. 什么是future
5. 如何利用future对象获取函数返回值
6. 如何实现任务只要完成就立马获取返回值
7. 让主线程堵塞
"""