# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.继承.py
# @Software: PyCharm
# @Time    : 2023/11/6 21:50


"""
继承在日常生活中的意思其实就是长辈去世之后晚辈可以获取到长辈的一些资源[房产、存额...]
编程领域中的继承和日常生活中的继承区别不大, 一个类可以继承另外一个类的所有属性和方法
"""


# 父类
class Animal:
    pass


# 子类
class Dog(Animal):
    pass


class Cat(Animal):
    pass


"""
以上案例表示了父类与子类的继承写法
    并且一个父类可以被多个子类继承
"""
