# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 下午9:20
# @Author  : 顾安
# @File    : 3.测试题.py
# @Software: PyCharm


# 计算 1 - 100 的累计和

i = 1
sum_result = 0  # 创建一个变量用于存储结果, 默认值为0

# while i <= 100:
#     # sum_result = sum_result + i
#     sum_result += i
#     i += 1

# print(sum_result)


# 计算1 - 100 的偶数累积和
# while i <= 100:
#     if i % 2 == 0:  # 这个if不需要else
#         sum_result += i
#     # 当前计数器不能受到if代码块的控制
#     i += 1
#
# print(sum_result)


# 计算 1 - 100 之间能被3整除且能够被7整除的所有数字之和
# while i <= 100:
#     if i % 3 == 0 and i % 7 == 0:
#         sum_result += i
#
#     # 当前计数器不能受到if代码块的控制
#     i += 1
#
# print(sum_result)


# 输出以下格式
"""
1 ----> 1
2 ----> 4
3 ----> 9
4 ----> 16
5 ----> 25
"""

while i <= 5:
    print(f'{i} ----> {i * i}')
    i += 1
