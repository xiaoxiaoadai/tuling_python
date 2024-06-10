# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.实例方法的定义.py
# @Software: PyCharm
# @Time    : 2023/11/3 21:29


class Hero:
    def test_1(self):
        print('这是一个实例方法')

    def test_2(self, age):
        print(age)

    def test_3(self):
        print('这是一个实例方法: test_3')


"""
在一个类中定义实例方法时, 实例方法中必须要有一个参数: self
    如果一个方法中的第一个参数的名字叫self, 则这个方法一定是一个实例方法
    
如何调用类中的实例方法
    1.创建当前这个类的实例对象
    2.根据这个实例对象打点调用对应方法
    
    一个对象可以分别调用不同的实例方法
        只要是实例对象则可以重复的调用不同的实例方法
"""

h = Hero()  # 不需要传参: 看__init__

h.test_1()
h.test_1()
h.test_2(10)
h.test_3()


