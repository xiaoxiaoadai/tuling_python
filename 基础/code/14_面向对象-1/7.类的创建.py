# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.类的创建.py
# @Software: PyCharm
# @Time    : 2023/11/3 21:00


# 定义类
class Person:
    # 可以定义这个类共同具有的行为[方法]与特征[属性]代码
    def __init__(self, name, gender):  # 定义特征的方法
        self.name = name
        self.gender = gender

    # 一个类共用具有的行为可以使用函数定义, 如果一个函数在一个类的内部, 不能被称之为函数: 方法
    def run(self):
        print(f'{self.name}正在跑...')


"""
类由三部分构成
    1.类名
    2.属性 -- 一组数据
    3.方法 -- 行为
    

class 类名:
    在当前位置定义属性与方法...
"""


# 当前这种方式在python3中已经被淘汰了
# 类名后面的括号是用来进行类继承用的  现在暂时不用管
class Test(object):
    pass

