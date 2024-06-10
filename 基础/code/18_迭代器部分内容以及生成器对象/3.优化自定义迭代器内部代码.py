# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.优化自定义迭代器内部代码.py
# @Software: PyCharm
# @Time    : 2023/11/13 20:50


class MyList:
    def __init__(self):
        self.container = list()
        self.index = 0

    def __iter__(self):  # 声明的是这个类是一个迭代对象
        return self

    def __next__(self):
        if self.index < len(self.container):
            item = self.container[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def add(self, item):
        self.container.append(item)


my_list = MyList()
my_list.add(1)
my_list.add(2)
my_list.add(3)

for item in my_list:
    print(item)

