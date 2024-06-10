# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.使用装饰器装饰带有参数的函数.py
# @Software: PyCharm
# @Time    : 2023/11/15 21:11

# 外层函数接收的一定是被装饰的函数地址
def debug(func_obj):
    # 内层函数接收的是被装饰的函数的参数
    def wrapper(*args, **kwargs):
        print(f'[DEBUG]: {func_obj.__name__}')
        func_obj(*args, **kwargs)

    return wrapper


@debug
def send_message(content):
    print(content)


send_message('你好')
