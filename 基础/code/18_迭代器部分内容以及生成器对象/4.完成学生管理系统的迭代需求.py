# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.完成学生管理系统的迭代需求.py
# @Software: PyCharm
# @Time    : 2023/11/13 20:54


class StudentSystem:
    def __init__(self):
        self.stu_list = list()
        self.index = 0

    def add_student(self):
        stu_name = input('请输入学生姓名:')
        stu_gender = input('请输入学生性别:')

        stu_dict = dict()
        stu_dict['stu_name'] = stu_name
        stu_dict['stu_gender'] = stu_gender
        self.stu_list.append(stu_dict)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.stu_list):
            result = self.stu_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


stu_system = StudentSystem()
stu_system.add_student()
stu_system.add_student()

for item in stu_system:
    print(item)
