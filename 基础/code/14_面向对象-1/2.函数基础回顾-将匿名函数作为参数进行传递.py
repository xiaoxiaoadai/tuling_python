# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.函数基础回顾-将匿名函数作为参数进行传递.py
# @Software: PyCharm
# @Time    : 2023/11/3 20:16


def work(a, b, func_obj):
    print(a)
    print(b)
    print(func_obj(a, b))


work(1, 2, lambda a, b: a + b)