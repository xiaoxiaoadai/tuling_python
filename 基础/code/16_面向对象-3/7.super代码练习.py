# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.super代码练习.py
# @Software: PyCharm
# @Time    : 2023/11/8 21:04


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}的年龄: {self.age}岁'


class Son(Father):
    def __init__(self, name, age, collage):
        super().__init__(name, age)
        self.collage = collage

    def __str__(self):
        return f'姓名: {self.name}, 年龄: {self.age}, 学历: {self.collage}'


class GrandChild(Son):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 儿子类的初始化方法
        print('这是一个孙子类')


father = Father('父亲', 50)
print(father)

son = Son('儿子', 18, '大学')
print(son)

grand_child = GrandChild('孙子', 4, '幼儿园')
print(grand_child)


"""
1.子类可以获取父类的属性与方法,如果子类定义的属性与父类相同则不用定义,直接使用父类的属性
2.子类构造初始化方法要检查父类中是否存在__init__方法。如果存在必须手动调用
    当父类的__init__有参数的话则子类负责补齐参数
"""

