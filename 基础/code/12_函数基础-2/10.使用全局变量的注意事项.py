# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.使用全局变量的注意事项.py
# @Software: PyCharm
# @Time    : 2023/10/30 21:13


# 全局变量相对于局部变量来说, 全局变量可以被任意函数或类访问
number = 100


def get_number():
    print(number)


def set_number():
    # number = 200  # 在一个函数的内部重新创建了一个新的变量, 这个变量的名字与全局变量重名 但是不是同一个变量
    global number  # 如果在函数中需要修改全局变量 则需要在这个变量的前面加上 global修饰符
    number = 200
    print(number)


get_number()
set_number()
print(number)




