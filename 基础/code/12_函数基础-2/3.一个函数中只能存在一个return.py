# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.一个函数中只能存在一个return.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:16


def return_test():
    return 1
    return 2  # 如果有多个return则只会运行第一个


res = return_test()
print(res)



