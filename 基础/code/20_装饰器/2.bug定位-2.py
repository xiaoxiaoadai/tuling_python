# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.bug定位-2.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:48

def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print(f'[DEBUG]: {caller_name}')


def say_hello():
    debug()
    print("hello!")


def say_goodbye():
    debug()
    print("hello!")  # 此处应打印goodbye


say_hello()
say_goodbye()