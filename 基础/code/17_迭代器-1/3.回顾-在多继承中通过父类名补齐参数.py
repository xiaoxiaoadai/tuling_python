# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.回顾-在多继承中通过父类名补齐参数.py
# @Software: PyCharm
# @Time    : 2023/11/10 20:27


class Parent:
    def __init__(self, name):
        print('parent类中的init被调用...')
        self.name = name
        print('parent类中的init结束调用...')


class Son_1(Parent):
    def __init__(self, name, age):
        print('son_1类中的init被调用...')
        # 通过调用父类的初始化方法完成参数补齐
        Parent.__init__(self, name)
        self.age = age
        print('son_1类中的init结束调用...')


class Son_2(Parent):
    def __init__(self, name, gender):
        print('son_2类中的init被调用...')
        # 通过调用父类的初始化方法完成参数补齐
        Parent.__init__(self, name)
        self.gender = gender
        print('son_2类中的init结束调用...')


class GrandSon(Son_1, Son_2):
    def __init__(self, name, age, gender, address):
        print('grand_son类中的init被调用...')
        Son_1.__init__(self, name, age)
        Son_2.__init__(self, name, gender)
        self.address = address
        print('grand_son类中的init结束调用...')


gs = GrandSon('安娜', 18, '女', '长沙')

