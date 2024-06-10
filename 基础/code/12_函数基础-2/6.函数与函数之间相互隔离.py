# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.函数与函数之间相互隔离.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:27


def test_1():
    a = 30000
    print(id(a))
    return a


def test_2():
    a = 30000
    print(id(a))
    return a


# print(id(test_1))
# print(id(test_2))

test_1()
test_2()


"""
在函数内部的变量是属于这个函数的
    也就是说不能通过函数1访问函数2中的变量对应的值
"""


