# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.装饰器语法使用.py
# @Software: PyCharm
# @Time    : 2023/11/15 21:05


def debug(func):
    def wrapper():
        print(f'[DEBUG]: {func.__name__}')
        print(id(wrapper))
        func()

    return wrapper


@debug  # == debug(say_hello)
def say_hello():
    print('你好...')


print(id(say_hello))

say_hello()


"""
被装饰的函数在运行的时候实际上运行的是装饰器的内层函数
"""



