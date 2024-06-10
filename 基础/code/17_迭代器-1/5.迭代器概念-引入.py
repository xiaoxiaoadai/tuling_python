# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.迭代器概念-引入.py
# @Software: PyCharm
# @Time    : 2023/11/10 21:25


class StuSystem:
    def __init__(self):
        self.stu_list = list()

    def add(self):
        name = input('请输入学生名称:')
        gender = input('请输入学生性别:')

        new_stu = dict()
        new_stu['stu_name'] = name
        new_stu['stu_gender'] = gender

        self.stu_list.append(new_stu)


stu_sys = StuSystem()

stu_sys.add()
stu_sys.add()

for item in stu_sys:
    print(item)
