# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.自定义迭代器.py
# @Software: PyCharm
# @Time    : 2023/11/13 20:13


from collections.abc import Iterable, Iterator


class MyList:
    def __init__(self):
        self.container = list()

    def __iter__(self):  # 声明的是这个类是一个迭代对象
        return MyIterator(self)

    def add(self, item):
        self.container.append(item)


class MyIterator:
    def __init__(self, my_list_obj):
        self.my_list_obj = my_list_obj
        self.index = 0

    def __next__(self):
        if self.index < len(self.my_list_obj.container):
            item = self.my_list_obj.container[self.index]
            self.index += 1
            return item
        else:
            # 手动抛出异常
            raise StopIteration

    def __iter__(self):
        return self  # 返回一个实例对象


my_list = MyList()
my_list.add(1)
my_list.add(2)
my_list.add(3)

print(isinstance(my_list, Iterable))

iter_obj = iter(my_list)
print(isinstance(iter_obj, Iterator))

for item in my_list:  # iter(my_list)
    print(item)
