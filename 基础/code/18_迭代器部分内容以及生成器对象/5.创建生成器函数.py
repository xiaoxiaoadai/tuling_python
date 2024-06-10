# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.创建生成器函数.py
# @Software: PyCharm
# @Time    : 2023/11/13 21:09

# 生成器函数
def my_list(number):  # 生成器函数, 返回值是一个生成器对象
    i = 0
    while i < number:
        yield i
        i += 1


# for item in my_list(5):
#     print(item)

my_obj = my_list(3)
print(my_obj.__next__())
print(my_obj.__next__())
print(my_obj.__next__())

"""
在生成器函数中是否存在之前在迭代器课程中出现的__iter__以及__next__方法？
    是一种特殊的迭代器, 不需要自己手动的创建以上两个方法
"""
