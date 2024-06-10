# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.回顾-使用super解决在多继承中重复运行父类的问题.py
# @Software: PyCharm
# @Time    : 2023/11/10 20:48


class Parent:
    def __init__(self, name, *args, **kwargs):
        print('parent类中的init被调用...')
        self.name = name
        print('parent类中的init结束调用...')


class Son_1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('son_1的init被调用...')
        super().__init__(name, *args, **kwargs)
        self.age = age
        print('son_1的init结束调用...')


class Son_2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('son_2的init被调用...')
        super().__init__(name, *args, **kwargs)
        self.gender = gender
        print('son_2的init结束调用...')


class GrandSon(Son_1, Son_2):
    def __init__(self, name, age, gender):
        print('grand_son的init被调用...')
        super().__init__(name, age, gender)
        print('grand_son的init结束调用...')


gs = GrandSon('双双', 18, '女')

print(GrandSon.__mro__)

print(gs.gender)

"""
super在多继承中的同级父类优先级大

    super调用顺序是严格按照mro链表继承顺序来进行调用的
"""
