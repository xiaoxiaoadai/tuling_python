# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.手动捕获指定的异常.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:11


# print(a)

try:
    print(9 / 0)
except ZeroDivisionError as e:
    print('程序发生错误:', e)  # 通过 as e的形式输出发生错误的原因
