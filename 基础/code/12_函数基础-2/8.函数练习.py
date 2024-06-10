# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.函数练习.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:53


# 写一个函数, 打印一条横线
# 定义另外一个函数, 打印自己定义行数的横线

def print_line_1():
    print('-' * 30)


def print_line_number(num):
    i = 0
    while i < num:
        print_line_1()
        i += 1


print_line_number(5)


# 完成两个函数, 函数1计算三个自然数之和, 函数2计算三个自然数的平均值
def sum_3_number(a, b, c):
    return a + b + c


def avg_3_number(a, b, c):
    res = sum_3_number(a, b, c)
    return res, sum_3_number(a, b, c) / 3


a, b = avg_3_number(1, 2, 3)
print(a, b)
