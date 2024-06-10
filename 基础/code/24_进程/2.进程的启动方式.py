# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.进程的启动方式.py
# @Software: PyCharm
# @Time    : 2023/11/24 20:18


"""
windows
macOS
Linux

    windows在启动进程是使用的是spawn模式
    macOS在启动进程使用的是spawn模式, macOS也支持fork启动
    Linux在启动进程使用的是fork模式

    在python中使用函数入口来确定当前操作系统启动进程的方式
    也可以指定启动方式, 但是windows系统不支持fork启动方式


    fork模式是将当前任务的代码和状态整个复制一份载入到一个新的进程中
    spawn模式是创建一个新的子python解释器去运行当前任务


并发: 在同一时刻, 只有一个任务被执行, 执行方式是任务随机切换, 只要切换的速度够快, 那么执行的效果类似于并行
并行: 在同一时刻, 有多个任务一起执行, 执行单位是cpu核心, 只要在cpu核心数量范围内, 则无需切换任务
"""


import time
import multiprocessing  # 进程包: 标准库


def work_1():
    for _ in range(5):
        print('任务一')
        time.sleep(1)


def work_2():
    for _ in range(5):
        print('任务二')
        time.sleep(1)


# 在windows中函数入口是必须要加的
multiprocessing.set_start_method('fork')  # windows不支持当前的启动方式
p1 = multiprocessing.Process(target=work_1)
p2 = multiprocessing.Process(target=work_2)

p1.start()
p2.start()
