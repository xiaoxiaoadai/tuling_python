# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.拆包.py
# @Software: PyCharm
# @Time    : 2023/10/27 20:51

"""
拆包是对容器类型快速取值的一种方式
    列表、元组、集合拆包方式一致, 以列表拆包为例
"""

nums = [1, 2, 3, 4]
# num_1 = nums[0]
# num_2 = nums[1]
# num_3 = nums[2]
# num_4 = nums[3]
# print(num_1, num_2, num_3, num_4)

# 拆包
# 在完成拆包需要注意位置问题
# 变量个数需要个容器中的元素个数一致
num_1, num_2, num_3, num_4 = nums
print(num_1, num_2, num_3, num_4)

# 字典拆包
# 对字典直接拆包只能获取到字典中的key
stu_info = {"name": "张三", "age": 18, "sex": "男"}
a, b, c = stu_info
print(a, b, c)

# 在for循环中使用k、v变量进行的拆包
for k, v in stu_info.items():
    print(k, v)
