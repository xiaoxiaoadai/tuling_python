# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.配合判断语句返回不同的值.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:19


def create_num(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return 3


res = create_num('1')
print(res)
