# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.使用生成器完成任务切换.py
# @Software: PyCharm
# @Time    : 2023/11/27 21:19


import time


def work_1():
    while True:
        print('这是第一个任务...')
        yield
        time.sleep(1)


def work_2(gen_obj):
    while True:
        print('这是第二个任务...')
        next(gen_obj)


obj = work_1()
work_2(obj)
