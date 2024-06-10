# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.列表的方法-元素删除.py
# @Software: PyCharm
# @Time    : 2023/10/25 20:47


stu_names = ['安娜', '双双', '百川', '安娜', '安娜', '百川']

# del
"""
del是一种特殊的关键字, 并不是列表对象中的方法
    del可以用来删除任意元素
"""
# del stu_names  # 删除当前列表对象
# print(stu_names)

# del stu_names[0]  # 如果有元素下标则删除对应的元素值
# print(stu_names)


# pop: 将元素弹出原有的列表
# pop方法默认移出列表中的最后一个元素
# 如果想要指定元素则可以写入当前指定元素的下标
# name = stu_names.pop(1)
# print(stu_names)
# print(name)

# remove: 可以根据元素值进行元素定位并删除
# remove删除重复元素只会删除第一个出现的
# stu_names.remove('安娜')
# print(stu_names)


# name = '安娜'
#
# print(stu_names.index(name))
#
# for i in stu_names:
#     if not stu_names[0] == '安娜':
#         stu_names.remove('安娜')
#
# print(stu_names)


print(stu_names.index('百川'))



