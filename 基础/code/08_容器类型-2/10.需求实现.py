# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.需求实现.py
# @Software: PyCharm
# @Time    : 2023/10/25 21:06


"""
在一个学校中有三个办公室, 要求将学校中的八位老师随机分配到这三个办公室中
"""

import random

# 定义学校
school = [[], [], []]

# 定义老师
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 通过for循环依次取出老师名称
for name in names:
    # 生成随机办公室对应的索引值
    random_office_number = random.randint(0, 2)
    # 根据随机生成的索引值选中其中一个办公室并使用append添加老师名称
    school[random_office_number].append(name)

# 定义办公室编号
office_number = 1
for office in school:
    print(f'办公室{office_number}老师有：{office}')
    office_number += 1


