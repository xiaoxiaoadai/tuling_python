# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.通过继承获取父类的资源.py
# @Software: PyCharm
# @Time    : 2023/11/6 21:55


class A:
    def __init__(self, name):
        self.name = name

    def print_attr(self):
        print(self.name)


class B(A):
    def work(self):
        print(f'{self.name}正在做作业...')


class C(B):
    pass


b = B('hello')
b.print_attr()


c = C('world')
c.print_attr()
c.work()

"""
一个子类继承了一个父类则可以使用这个类中的所有资源[私有属性、私有方法无法继承]
"""
