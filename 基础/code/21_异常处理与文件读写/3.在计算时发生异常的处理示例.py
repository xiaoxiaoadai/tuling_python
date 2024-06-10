# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.在计算时发生异常的处理示例.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:08


def exp_exception(x, y):  # 除数不能为零
    try:
        result = x / y
        print(result)
    except:
        print('程序发生异常...')


exp_exception(9, 0)


"""
try...except...可以在函数体中使用
"""