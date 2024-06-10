# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.闭包使用的注意点.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:33


def send_int_data(number=0):
    def add_int_data():
        nonlocal number  # 在函数中如果需要对外层函数进行修改则需要加上nonlocal关键字, 类似于global
        number += 1
        print(number)

    return add_int_data


func_1 = send_int_data(5)
print(id(func_1))
func_1()


"""
闭包返回的内存地址可以被多个变量接收,并且多个接收的地址不同
    接收一次内部函数地址相当于重新运行了这个闭包代码
        需要在内存中重新开辟一个空间来存储第二次返回的内部函数地址
        类似于实例对象
        
        所以func_1和func_2是内存隔离的状态
"""

func_2 = send_int_data(10)
print(id(func_2))
func_2()


"""
1.在一个外层函数中定义了内层函数, 内层函数使用了外层函数的参数, 并且外层函数返回了内层函数的引用: 闭包
2.在内部函数中可以访问到外层函数的参数
"""
