# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.函数说明文档.py
# @Software: PyCharm
# @Time    : 2023/10/27 21:40


"""
函数说明文档主要是用来表述当前这个函数的功能以及用法

python中一切皆对象, 函数也是
"""


def func_document():
    """
    这是一个函数说明文档
    :return:
    """


# 在pycharm中可以使用__doc__方法输出当前函数的说明文档: 如果有文档的情况下
print(func_document.__doc__)

# 如果大家使用的是ipython交互模式则可以使用函数名称 + ?的方式查询函数说明文档

