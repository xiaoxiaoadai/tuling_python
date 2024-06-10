# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.类装饰器本身带有参数.py
# @Software: PyCharm
# @Time    : 2023/11/15 21:41


class Logging:
    def __init__(self, level):
        self.level = level

    def __call__(self, func_obj):
        def wrapper(*args, **kwargs):
            print(f'[{self.level}]: {func_obj.__name__}')
            func_obj(*args, **kwargs)

        return wrapper


@Logging('DEBUG')  # Loging('DEBUG')(send_message) == send_message
def send_message(content):
    print(f'信息内容: {content}')


send_message('双双胖三斤...')


"""
mixin: 融合继承的设计模式
    如果想要实现多个功能可以使用mixin多继承的方式进行实现
    
    1.mixin类不能自己单独实例化
    2.mixin不能有初始化方法
    3.mixin类中只能实现单一并唯一的功能
"""


