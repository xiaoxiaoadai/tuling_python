# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.创建多个实例对象.py
# @Software: PyCharm
# @Time    : 2023/11/6 20:36


class Dog:
    def __init__(self):
        self.dog_name = None

    def run(self):
        print(f'{self.dog_name}正在跑...')


dog_1 = Dog()
dog_1.dog_name = '哈士奇'

dog_2 = Dog()
dog_2.dog_name = '金毛'

dog_2.run()
dog_1.run()

"""
实例对象与实例对象之间是内存隔离的
    每一个创建出来的实例对象都有自己的属性, 并占用属于自己的内存空间

多个对象是有一个类创建的, 多个对象能不能访问同一个类？
"""

print(id(dog_1.__class__))
print(id(dog_2.__class__))
