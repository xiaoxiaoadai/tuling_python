# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.使用property模拟价格设置.py
# @Software: PyCharm
# @Time    : 2023/11/15 22:10


class Goods:
    def __init__(self):
        self.old_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.old_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.discount = value

    @price.deleter
    def price(self):
        self.discount = 1


goods = Goods()
print(goods.price)

goods.price = 0.7
print(goods.price)

del goods.price
print(goods.price)



