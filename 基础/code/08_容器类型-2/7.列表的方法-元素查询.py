# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.列表的方法-元素查询.py
# @Software: PyCharm
# @Time    : 2023/10/25 20:41


# in: 成员运算符
stu_names = ['安娜', '双双', '百川']

name = '夏洛'
if name in stu_names:
    print(1)
else:
    print(2)

# count: 查询指定元素在列表中出现的次数
nums = [1, 2, 1, 4, 6, 4, 9, 7, 7, 4, 1]
print(nums.count(4))
# 统计不存在的元素
print(nums.count(5))


