# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.补充: python中没有元组推导式.py
# @Software: PyCharm
# @Time    : 2023/10/27 21:04


int_tuple = (i for i in range(1, 21))
print(int_tuple)  # 生成器对象

"""
对于生成器对象在之后的课程中会详细说明
    当前只要知道生成器也是可以被for循环执行的就可以
"""

for item in int_tuple:
    print(item)
