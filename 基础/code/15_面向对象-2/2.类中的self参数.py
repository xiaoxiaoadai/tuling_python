# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.类中的self参数.py
# @Software: PyCharm
# @Time    : 2023/11/6 20:18

# 遵守规定, 当代码量过多可能会导致在调用的时候当成属性去用
class Person:
    def set_attr(self):
        self.name = '安娜'
        self.age = 18
        self.address = '长沙'
        print(self)  # 输出：<__main__.Person object at 0x10ab1cfd0> [Person的一个对象, 这个对象其实就是实例对象]

    def print_attr(self):
        self.set_attr()
        print(self.name, self.age, self.address)


p = Person()
p.print_attr()
"""
通过print打印发现self输出的信息是Person这个类的对象, 这个对象其实就是这个类的实例对象
    self是一个类的实例对象本身
"""
