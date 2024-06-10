# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.线程池使用完毕之后需要释放资源.py
# @Software: PyCharm
# @Time    : 2023/11/22 21:14

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def work(num):
    print('开启任务:', num)
    # raise NameError
    # time.sleep(3)
    return num


# 当前这段代码中是使用手动的方式完成的线程池对象的关闭
# pool = ThreadPoolExecutor(max_workers=2)
# future_list = [pool.submit(work, num) for num in range(1, 11)]
# pool.shutdown()


with ThreadPoolExecutor(max_workers=2) as pool:
    future_list = [pool.submit(work, num) for num in range(1, 11)]

