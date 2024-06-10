# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.可能会遇到的函数类型.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:23


"""
1. 无参数, 无返回值
2. 无参数, 有返回值
3. 有参数, 无返回值
4. 有参数, 有返回值 *
"""


def test_1():
    pass


def test_2():
    return 1


def test_3(a, b):
    print(a, b)


def test_4(a, b):
    return a + b


# 如果一个函数中没有return关键字, 则默认返回一个None
def return_none():
    # return None
    pass

res = return_none()
print(res)
