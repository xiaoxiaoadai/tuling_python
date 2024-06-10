# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.可变对象可以不使用global声明.py
# @Software: PyCharm
# @Time    : 2023/10/30 21:19


nums = [1, 2, 3, 4, 5]


def get_nums_list():
    print(nums)


def set_nums_list():
    nums.append(6)
    print(nums)


get_nums_list()
set_nums_list()
print(nums)


"""
global需要修饰在不可变类型上
    如果全局变量是一个可变类型则不需要加
"""
