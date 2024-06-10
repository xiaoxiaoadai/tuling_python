# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.迭代器.py
# @Software: PyCharm
# @Time    : 2023/11/10 21:40


"""
python中的字典、列表、字符串、集合等等这些容器类型是不是一个对象？
    一切皆对象

对象是怎么出来的？
    类的实例化完成的
"""

from collections.abc import Iterable


class Test:
    def __iter__(self):  # __iter__方法可以确定这个类生成的对象是一个迭代对象
        pass


test = Test()
print(isinstance(test, Iterable))

for item in test:
    print(item)

nums = [1, 2, 3]
iter_obj = iter(nums)  # 可以将一个迭代对象变成一个迭代器对象
print(iter_obj)
# 迭代器对象可以依次取值
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

# 迭代对象只是告诉循环我支持循环操作, 但是真正取值的是迭代器
nums.__next__()

"""
python内置方法:
    id dir print input type isinstance iter
"""

"""
迭代对象和迭代器对象的区别:
    迭代对象只是告诉循环我支持循环操作, 但是是无法取值    
    迭代器是真正在底层循环取值的人
"""
