# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.多继承案例.py
# @Software: PyCharm
# @Time    : 2023/11/8 20:07


class A:
    name = 'A'


class B:
    name = 'B'


# 当前类C继承的顺序是根据括号中的写入顺序决定的
class C(A, B):
    name = 'C'


print(C.name)


"""
如果类本身存在需要的属性, 则直接找自身属性, 如果没有, 则按照类的继承顺序依次查找
    如果在第一个类中已经找到了需要的属性或方法, 那么python不会继续向上查找
"""
