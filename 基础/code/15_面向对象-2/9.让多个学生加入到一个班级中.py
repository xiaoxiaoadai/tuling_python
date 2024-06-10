# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.让多个学生加入到一个班级中.py
# @Software: PyCharm
# @Time    : 2023/11/6 21:35


class ClassRoom:
    def __init__(self, cls_name):
        self.cls_name = cls_name
        self.stu_info = list()

    # 方法中的形式参数其实就是一个暂时没有被绑定值的一个普通变量
    def add_student(self, key, value):  # 当前接收到的value是学生类的实例对象
        stu_dict = {key: value.stu_name}
        self.stu_info.append(stu_dict)


class Student:
    def __init__(self, stu_name):
        self.stu_name = stu_name


stu_1 = Student('顾安')
stu_2 = Student('安娜')
stu_3 = Student('双双')

cls_room = ClassRoom('python一班')
cls_room.add_student('顾安', stu_1)
cls_room.add_student('安娜', stu_2)
cls_room.add_student('双双', stu_3)


"""
所谓的对象关联其实就是在一个类中创建了一个属性
    让这个属性指向另外一个类的实例对象
"""