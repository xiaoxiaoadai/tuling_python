# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.元组中元素的修改探究.py
# @Software: PyCharm
# @Time    : 2023/10/25 21:34


# 定义一个元组使用的是() 并且元组不能修改元素值[内存地址]
int_tuple_1 = (1, 2, 3, 4)
print(type(int_tuple_1))

# 尝试修改元组中的值
# int_tuple_1[0] = 100
# print(int_tuple_1)

# python中的内存地址
# print(id(1))  # 返回的是当前这个值在哪个内存中, 内存也是有编号的
# print(id(2))


# 在元组中修改列表中的元素
int_tuple_2 = (1, 2, 3, [4, 5])
list_1 = int_tuple_2[3]
int_tuple_2[3][0] = 6
list_2 = int_tuple_2[3]
print(int_tuple_2)

print(id(list_1))
print(id(list_2))

"""
在以上案例中修改列表中的元素不会更改列表本身的内存地址
    所以是允许的
"""

list_3 = [3, 4]
list_4 = [4, 6]
print(id(list_3) == id(list_4))

