# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.函数基础回顾-递归函数.py
# @Software: PyCharm
# @Time    : 2023/11/3 20:28


"""
递归函数并不是一种函数声明的表达方式
    递归的本质是一种算法
        自身调用自身
"""


def test():
    print(1)
    test()


test()  # 函数调用次数超出递归最大深度 997次


"""
数据分析中可能会用到递归
    python建议程序员不要任意的使用递归
        死循环
"""
