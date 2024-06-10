# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.函数引用.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:14


def test():
    print('这是一个测试函数...')


func_obj = test

print(id(test))
print(id(func_obj))


"""
一个函数名如果没有携带括号则返回的是这个函数在内存中的地址
    函数引用
"""


func_obj()
