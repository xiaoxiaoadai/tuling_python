# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.私有属性.py
# @Software: PyCharm
# @Time    : 2023/11/6 20:55


class Person:
    def __init__(self, name, gender, money):
        self.name = name
        self.gender = gender
        self.__money = money  # 私有属性

    # 创建一个对外访问私有属性的方法
    def get_attr(self):
        print(self.__money)

    def set_attr(self, value):
        self.__money = value

    def del_attr(self):
        del self.__money


p = Person('夏洛', '男', 23000)
print(p.name)
print(p.gender)
# print(p.__money)  不能在声明私有属性的类的外部使用

p.get_attr()


"""
第二种方法不要在公司内部使用
    当前这种方法容易出现生产事故
    
_类名__属性名可以直接访问私有属性
"""
print(p._Person__money)


"""
如果在类中创建了私有属性则需要通过专门的内部实例方法去进行私有属性的操作
    
"""