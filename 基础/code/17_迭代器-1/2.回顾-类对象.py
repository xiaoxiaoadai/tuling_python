# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.回顾-类对象.py
# @Software: PyCharm
# @Time    : 2023/11/10 20:11


"""
类对象:
    指的是当前这个类本身

实例对象:
    指的是对一个类进行实例化之后得到的对象本身
"""


class A:
    def __init__(self, name):
        self.name = name
    pass

    def print_a(self):
        print()


print(id(A))
print(A)

a_1 = A('顾安')
a_2 = A('安娜')
a_3 = A('双双')
print(id(a_1), id(a_2), id(a_3))  # 多个实例对象中的地址是不一样的, 是隔离的状态
print(a_1, a_2, a_3)

"""
类对象在全局内存中只有一个
实例对象随着多次的创建会在内存中开辟多个空间来存储这个实例对象

实例对象的内存地址存储的是当前这个实例对象的实例属性以及类对象的地址
类对象的内存地址中存储的是这个类的类属性和所有方法[实例方法] *

实例对象中除了保存自身的实例属性之外, 还保存了类的地址

在实例对象中有一些属性和方法, 怎么去查询实例对象与类对象中包含的属性和方法？
    dir()
"""
print(id(a_1.__class__))  # __class__是一个方法
print(id(a_2.__class__))
print(id(a_3.__class__))


print(dir(A))
print(dir(a_1))


