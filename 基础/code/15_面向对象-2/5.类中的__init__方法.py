# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.类中的__init__方法.py
# @Software: PyCharm
# @Time    : 2023/11/6 20:44


"""
__init__被称之为初始化方法
    在类被实例化的过程中会自动调用__init__方法
    通过这个特性可以利用__init__创建实例属性
"""


class Student:
    def __init__(self):
        print('我被执行了...')
        self.name = '顾安'
        # s.name = '顾安'


s = Student()

"""
1.类在实例化的过程中会自动调用__init__方法, 不需要开发者自己手动调用
2.__init__和普通实例方法一样, 第一个参数为self, 也不需要通过开发者手动传递
3.self代表实例对象可以解决多个实例对象名称不同的问题
4.__init__方法中除了有self参数之外, 也允许存在其他多个参数
"""


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


p = Person('双双', '女')
print(p.name, p.gender)
