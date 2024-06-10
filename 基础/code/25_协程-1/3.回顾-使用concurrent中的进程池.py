# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.回顾-使用concurrent中的进程池.py
# @Software: PyCharm
# @Time    : 2023/11/27 20:37


import os
import time
from random import random
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed, wait


def work(msg_1, msg_2):
    p_start = time.time()
    print(f'{msg_1}开始执行, 进程号为: {os.getpid()}')
    print('这是当前任务的第二个参数值:', msg_2)
    time.sleep(random() * 2)
    p_stop = time.time()
    print(f'程序[{msg_1}]执行完毕, 耗时: {p_stop - p_start}')
    return msg_2


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as pool:
        # for i in range(1, 11):
        #     future = pool.submit(work, i, '测试参数...')
        #     print('函数返回值:', future.result())

        # 使用map返回的是一个生成器对象, 对生成器对象迭代可以直接获取到任务的返回值
        futures = pool.map(work, [_ for _ in range(1, 11)], ['测试参数...' for _ in range(1, 11)])
        # for future in futures:
        #     print('函数返回值:', future.result())
        for future in futures:
            print('函数返回值:', future)

        # futures = [pool.submit(work, i, '测试参数...') for i in range(1, 11)]
        # for res in as_completed(futures):
        #     print('函数返回值:', res.result())
