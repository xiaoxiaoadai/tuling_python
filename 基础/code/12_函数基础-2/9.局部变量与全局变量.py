# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.局部变量与全局变量.py
# @Software: PyCharm
# @Time    : 2023/10/30 21:00


def test_1():
    a = 300
    print(f'test_1在修改a变量之前的值为: {a}')

    a = 200
    print(f'test_1在修改a变量之后的值为: {a}')


def test_2():
    a = 400
    print(f'test_2在修改a变量的值为: {a}')


test_1()
test_2()

"""
如果一个变量在一个函数的内部
    那么这个变量只能被开启作用域的代码使用: 局部变量
    
    局部变量一般在代码块的内部
        当前在函数中定义局部变量是专供这个函数使用的, 其他函数无权使用
"""

number = 100


def get_number_1():
    number = 99  # 如果一个函数的内部中具有指定的变量 那么优先使用内部的
    print(number)


def get_number_2():
    print(number)  # 当前这个函数内部没有number变量 会在这个py整体文件中查询指定变量
    #  如果当前函数中没有number 也不会进入到get_number_1中进行查询


get_number_1()
get_number_2()

