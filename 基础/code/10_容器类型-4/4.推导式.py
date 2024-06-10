# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.推导式.py
# @Software: PyCharm
# @Time    : 2023/10/27 20:39


"""
列表推导式
"""
int_data = [i for i in range(10)]
print(int_data)

# 配合if判断使用
int_data = [i for i in range(10) if i % 2 == 0]
print(int_data)

# 使用步长
int_data = [i for i in range(1, 21, 3)]
print(int_data)

# 生成二维列表
int_data = [[x, y] for x in range(1, 3) for y in range(3)]
print(int_data)

"""
集合推导式
    对于列表推导式、集合推导式的使用方式是一样的
"""
set_data = {x for x in range(1, 21) if x % 2 == 0}
print(set_data)


"""
字典推导式
"""
# 快速生成一个1 - 10以内key为某个数此时value是key的平方
int_dict = {x: x ** 2 for x in range(1, 11)}
print(int_dict)
int_dict = {x: x + 1 for x in range(1, 11)}
print(int_dict)



