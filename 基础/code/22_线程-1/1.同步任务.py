# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.同步任务.py
# @Software: PyCharm
# @Time    : 2023/11/20 20:10

import time


def work_1():
    print('任务1')
    time.sleep(2)


def work_2():
    print('任务2')
    time.sleep(2)


work_1()
work_2()


"""
以上任务都是单线程同步任务
    如果有多个任务的情况下, 分别执行不同任务, 必须等待前一个任务完成之后才能执行后一个任务
"""