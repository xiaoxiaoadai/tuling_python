# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.函数返回值.py
# @Software: PyCharm
# @Time    : 2023/10/30 20:03


"""
在完成一个大型项目的过程中, 代码内部不一定只有一个函数
    可能一个功能需要有多个函数配合完成

第一个函数的返回值是第二个函数的参数
"""


# 返回值: return
def add_nums(a, b):
    c = a + b
    return c  # 通过return返回一个结果出去, 当前这个返回的结果可以使用一个新的变量进行接收


# 如果一个函数的内部有返回值 则可以定义一个变量来接收函数的返回值
result = add_nums(1, 2)
print(result)

# 可以使用print打印这个函数运行之后得到的返回值结果
print(add_nums(3, 4))

"""
1.return具有将一个或多个结果给调用方
2.return具有让一个函数结束的功能
"""


def test():
    print("test1")
    return 1  # 函数遇到return会自动终止
    print("test2")  # 永远不会执行到


test()


def return_test():
    return 1, 2, 3  # 打包成元组的形式将多个返回值返回


# 通过拆包的方式将元组中的元素分别赋值给a, b, c
a, b, c = return_test()
print(a, b, c)
