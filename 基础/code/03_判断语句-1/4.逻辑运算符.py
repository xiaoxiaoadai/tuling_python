# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 下午9:49
# @Author  : 顾安
# @File    : 4.逻辑运算符.py
# @Software: PyCharm

"""
逻辑运算符
    and or not

    and: 多个条件同时成立则得到的结果为True
    or: 多个条件只要成立一个则返回的结果为True
    not: 取反[如果原本的结果为True则返回的结果为False, 如果原本得到的结果为False, 则返回的结果为True]
"""

print(10 > 9 and 8 < 10)
print(10 > 9 or 8 > 10)  # 只要成立一个就返回True, 必须要有一个条件成立才能返回True
print(not(3 < 4 and 7 > 10))  # not里面的表达式返回的结果进行翻转则获取的是not关键字得到的结果
