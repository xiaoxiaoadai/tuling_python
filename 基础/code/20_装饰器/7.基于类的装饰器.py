# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.基于类的装饰器.py
# @Software: PyCharm
# @Time    : 2023/11/15 21:31


# class Test:
#     def __call__(self, *args, **kwargs):  # 让实例对象像函数一样被调用
#         print(args, kwargs)
#
#
# t = Test()
# t(1, 2, 3, name='安娜')


class Logging:
    def __init__(self, func_obj):
        self.func_obj = func_obj

    def __call__(self, *args, **kwargs):
        print(f'[DEBUG]: {self.func_obj.__name__}')
        self.func_obj(*args, **kwargs)


@Logging  # Logging(send_message) => 返回的是当前这个类的实例对象
def send_message(content):
    print(f'信息内容: {content}')


send_message('双双胖三斤...')
