# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.super的使用方式.py
# @Software: PyCharm
# @Time    : 2023/11/8 20:40


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 返回当前这个类的信息的
    def __str__(self):  # 如果使用print打印了这个类的实例对象则自动触发这个类的__str__方法
        return f'{self.name}的年龄: {self.age}岁'


class Son(Father):
    def __init__(self, name, age, collage):
        super().__init__(name, age)  # 在子类中必须调用父类的构造方法并补齐父类所需的参数
        # Father.__init__(self, name, age)
        self.collage = collage


son = Son('儿子', 18, '本科')
print(son.name, son.age, son.collage)
