# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.生成器推导式.py
# @Software: PyCharm
# @Time    : 2023/11/13 21:39


nums = (i for i in range(300000000) if i % 2 == 0)  # 生成器推导式语法

print(next(nums))

for item in nums:
    print(item)

nums = [i for i in range(300000000)]  # 等待列表中的元素全部生成完毕为止
for item in nums:
    print(item)


"""
没有元组推导式
    返回的是一个生成器对象
"""