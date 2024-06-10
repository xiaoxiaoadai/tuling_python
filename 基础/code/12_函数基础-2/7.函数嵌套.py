# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.函数嵌套.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:46


def test_1():
    print(1)
    test_2()  # 在test_1函数内部调用了test2函数


def test_2():
    print(2)
    # test_1()  # 在test_2函数内部调用了test1函数


test_1()


"""
可以在一个函数的内部调用另外一个函数
    无限递归: 自己调用自己
"""

