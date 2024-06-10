# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.使用拆包的方式完成函数地址互换.py
# @Software: PyCharm
# @Time    : 2023/11/1 22:16


def test_1():
    print(1)


def test_2():
    print(2)


test_1, test_2 = test_2, test_1

test_1()
test_2()

"""
函数调用: 通过小括号的方式让python解释器找到在内存中的函数代码并运行
函数引用: 通过函数名称本身获取函数地址, 这个不是运行代码
"""

# test_1  # 引用
# test_2()  # 调用
