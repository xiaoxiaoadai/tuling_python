# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.进程的使用.py
# @Software: PyCharm
# @Time    : 2023/11/24 20:05


"""
线程: 在python中存在GIL锁, 只能允许一个线程在同一时刻被运行
进程: 基于cpu核心数运行, 并行的
"""

import time
import threading
import multiprocessing  # 进程包: 标准库


def work_1():
    for _ in range(5):
        print('任务一')
        time.sleep(1)


def work_2():
    for _ in range(5):
        print('任务二')
        time.sleep(1)


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=work_1)
    t2 = multiprocessing.Process(target=work_2)

    t1.start()
    t2.start()


"""
在不同的操作系统中启动进程的方式是不一样的
    使用函数入口的方式去运行进程代码
    
    进程中传递的参数以及启动方式与线程类似
"""
