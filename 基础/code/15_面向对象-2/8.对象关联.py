# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.对象关联.py
# @Software: PyCharm
# @Time    : 2023/11/6 21:14


class ClassRoom:
    def __init__(self, cls_name):
        self.cls_name = cls_name


class Student:
    def __init__(self, stu_name):
        self.stu_name = stu_name


python_room = ClassRoom('python一班')
stu = Student('安娜')


# 可以使用动态创建实例属性的方式将学生对象加入到教室对象中
python_room.stu_info = stu

# 通过教室对象将学生信息打印出来
print(id(python_room.stu_info))
print(id(stu))
print(id(stu.stu_name))
print(python_room.stu_info.stu_name)


"""
1.在教室对象中创建一个实例属性: stu_info
2.将学生对象添加到stu_info属性中: 当前这个属性指向的地址是学生对象的地址
"""


