# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用装饰器完成bug定位.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:51


def debug(func):
    print(id(func))

    def wrapper():
        print(f'[DEBUG]: {func.__name__}')
        func()

    return wrapper


def say_hello():
    print('你好')


print(id(say_hello))

func_obj = debug(say_hello)
func_obj()

"""
装饰器定义:
    1.外层函数定义的形参接收的是要被执行的函数的地址
    2.内层函数运行外层函数所接收的函数地址
    3.外层函数返回内层函数的引用
"""
