# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.property装饰器的高级使用.py
# @Software: PyCharm
# @Time    : 2023/11/15 22:02


class Goods:

    @property
    def price(self):
        print('property')

    @price.setter
    def price(self, value):
        print('property.setter')

    @price.deleter
    def price(self):
        print('property.deleter')

    # @price.getter
    # def price(self):
    #     print('property.getter')


obj = Goods()
obj.price

# 设置价格
obj.price = 123

# 删除价格
del obj.price
