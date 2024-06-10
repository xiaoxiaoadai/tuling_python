# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.使用切片的方式获取列表中的元素.py
# @Software: PyCharm
# @Time    : 2023/10/25 20:04


stu_names_1 = ["张三", "李四", "王五", "赵六", "田七"]

print(stu_names_1[1:3])  # 使用列表切片的方式获取到的结果是一个列表
print(type(stu_names_1[1:3]))

print(stu_names_1[::-1])

stu_names_2 = stu_names_1[::-1]
print(stu_names_2)


