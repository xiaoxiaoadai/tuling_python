# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.回顾循环语法.py
# @Software: PyCharm
# @Time    : 2023/11/10 21:31


"""
列表
字典
元组
集合
字符串
"""

from collections.abc import Iterable  # Iterable: 迭代类型 标准库


nums = [1, 2, 3]

for item in nums:
    print(item)

str_data = 'abc'
for item in str_data:
    print(item)


# for item in 12345:
#     pass

# 判断对象类型的方法: isinstance()  被判断的对象是否是Iterable类的子类
print(isinstance(nums, Iterable))
print(isinstance(123, Iterable))


# 是一个对象的类型: 迭代类型
# 是什么确定这个对象是一个迭代类型？
