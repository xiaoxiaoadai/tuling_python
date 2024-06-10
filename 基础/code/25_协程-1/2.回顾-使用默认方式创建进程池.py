# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.回顾-使用默认方式创建进程池.py
# @Software: PyCharm
# @Time    : 2023/11/27 20:22


import time
from random import randint
from multiprocessing import Pool


def work(message):
    time.sleep(randint(1, 3))
    print(message)


if __name__ == '__main__':
    # 创建进程池对象
    pool = Pool(3)

    for i in range(10):
        # pool.apply(work, args=(i,))  # 同步执行
        pool.apply_async(work, args=(i,))  # 异步执行: 任务提交并随机调度任务并发执行

    pool.close()  # 关闭进程池: 给进程对象发送信号, 不接收新的任务
    pool.join()  # 当执行进程池任务并让主进程堵塞会直接报错