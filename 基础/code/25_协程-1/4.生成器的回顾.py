# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.生成器的回顾.py
# @Software: PyCharm
# @Time    : 2023/11/27 21:18


def func():
    print('程序启动...')
    while True:
        yield '这是一个返回值...'


gen_obj = func()
print(next(gen_obj))
print(next(gen_obj))
