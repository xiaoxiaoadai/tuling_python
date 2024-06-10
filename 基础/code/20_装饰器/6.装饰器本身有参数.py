# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.装饰器本身有参数.py
# @Software: PyCharm
# @Time    : 2023/11/15 21:16


def logging(level):
    def wrapper(func_obj):
        def inner_wrapper(*args, **kwargs):
            print(f'[{level}]: {func_obj.__name__}')
            func_obj(*args, **kwargs)
        return inner_wrapper
    return wrapper


@logging(level='info')  # == logging('info') => wrapper(send_message)
def send_message(content):
    print(f'信息内容: {content}')


send_message('今天天气不错...')


