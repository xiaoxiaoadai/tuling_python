# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.手动抛出异常.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:14


try:
    raise NameError  # 可以使用raise 手动抛出一个指定异常
    print(1)
except NameError as e:
    # print('代码异常')
    pass