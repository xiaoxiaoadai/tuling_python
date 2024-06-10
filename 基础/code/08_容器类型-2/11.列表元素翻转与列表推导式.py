# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.列表元素翻转与列表推导式.py
# @Software: PyCharm
# @Time    : 2023/10/25 21:26


# 列表倒序
int_list_1 = [1, 2, 3, 4]
# print(int_list_1[::-1])  # 切片会生成一个新列表
# sort方法是用于排序的, 默认为正序
# int_list_1.sort(reverse=True)  # sort在原有列表中进行倒序, 会修改原有列表的元素位置
print(sorted(int_list_1, reverse=True))  # 会生成一个新列表, 不会修改原有列表的元素位置

# 列表推导式
# 用于快速生成一个有规则的序列
int_list_2 = [i for i in range(1, 11)]
print(int_list_2)

int_list_3 = [i for i in range(1, 11) if i % 2 == 0]
print(int_list_3)









