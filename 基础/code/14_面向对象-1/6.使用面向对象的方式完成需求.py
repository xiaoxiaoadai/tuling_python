# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.使用面向对象的方式完成需求.py
# @Software: PyCharm
# @Time    : 2023/11/3 20:40


class Person:
    def __init__(self, stu_name, stu_age):
        self.stu_name = stu_name
        self.stu_age = stu_age

    def print_info(self):
        print(f'学生姓名: {self.stu_name}, 学生年龄: {self.stu_age}')


stu_guan = Person('顾安', 18)
stu_guan.print_info()

stu_anna = Person('安娜', 20)
stu_anna.print_info()
