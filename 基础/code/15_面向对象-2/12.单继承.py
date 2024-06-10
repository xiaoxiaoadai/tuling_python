# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 12.单继承.py
# @Software: PyCharm
# @Time    : 2023/11/6 22:03


"""
一个子类只继承一个父类: 单继承
"""


class Animal:
    def eat(self):
        print('正在吃饭...')

    def drink(self):
        print('正在喝水...')

    def run(self):
        print('正在跑...')

    def info(self):
        print(f'{self.name}的年龄为: {self.age}岁')


# 如果子类括号中只有一个父类的名字则当前继承为单继承
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog('哈士奇', 3)
dog.eat()
dog.drink()
dog.run()
dog.info()

"""
在完成继承代码时大家需要遵守一个原则:
    如果需要给代码增加方法时, 去修改子类代码, 不要修改父类代码！！！
    
    父类可以被多个子类继承, 如果修改父类中的代码, 那么会影响所有继承的子类！
"""
