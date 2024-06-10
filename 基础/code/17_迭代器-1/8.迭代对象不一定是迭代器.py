# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.迭代对象不一定是迭代器.py
# @Software: PyCharm
# @Time    : 2023/11/10 21:54


from collections.abc import Iterable, Iterator


class Test:
    def __iter__(self):
        pass


test = Test()
print(isinstance(test, Iterable))
print(isinstance(test, Iterator))

nums = [1, 2, 3]
print(isinstance(nums, Iterable))
print(isinstance(nums, Iterator))  # false


iter_obj = iter(nums)  # 手动的将一个迭代对象通过iter方法转为了一个迭代器对象
print(isinstance(iter_obj, Iterator))
print(isinstance(iter_obj, Iterable))

# for循环的底层代码实现
while True:
    try:
        print(iter_obj.__next__())
    except StopIteration:
        break

"""
while循环完成的
    通过以上案例发现, 在进行循环取值的时候需要手动的将列表迭代对象转为一个迭代器对象

for循环会在底层自动的将迭代对象转为迭代器对象

迭代对象不一定是迭代器
迭代器一定是迭代对象
"""
