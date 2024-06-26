# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 下午8:00
# @Author  : 顾安
# @File    : 1.关于使用and关键字需要注意的地方.py
# @Software: PyCharm


"""
and
链接两个条件
    返回两个条件中如果同时成立则返回什么以及如果一个其中一个条件不成立则返回什么结果
"""

# 在当前代码中并没有返回布尔值
"""
and主要返回的是这个关键字左边或者右边的值

''
[]
()
{}
0
    认为是一个false
"""
print(1 and 2)

# 因为当前的条件不是变量，意味着当前成立中的代码永远不会被执行
if '':
    print('条件成立')
else:
    print('条件不成立')

# 因为当前的条件不是变量，意味着当前成立中的代码永远不会被执行
if 0:
    print('0条件成立')
else:
    print('0条件不成立')

# and左边和右边返回的数据你要看当前写的是不是一个表达式
print(1 and 0)
print(0 and 5 > 6)

