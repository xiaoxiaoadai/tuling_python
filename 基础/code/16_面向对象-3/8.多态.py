# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.多态.py
# @Software: PyCharm
# @Time    : 2023/11/8 21:23


"""
什么是多态
    多个类实现了同一个方法
        但是多个类中的同一个方法的实现方式不一样: 有继承关系

    游泳游泳:
        仰泳
        蝶泳
        狗刨
        蛙泳
        ...

        你在水中不会溺水
"""


class Dog:
    def bark(self):
        print('狗汪汪叫...')


class LangGou(Dog):
    def bark(self):
        print('狼狗震耳欲聋的叫...')


class TaiDi(Dog):
    def bark(self):
        print('泰迪嘤嘤嘤的叫...')


"""
1.必须有继承
2.必须有重写
"""