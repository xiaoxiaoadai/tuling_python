# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 下午8:01
# @Author  : 顾安
# @File    : 1.print的使用.py
# @Software: PyCharm


"""
print是python这门语言提供的一个功能
    python中的一个函数

    可以使用这个函数来完成打印的功能
    print可以打印一个具体的值、变量、对象
"""

age = 18
print(age)  # print在打印变量的时候不需要加上单双引号

# 打印整型类型以及字符串类型
print(100)
print('双双真好看...')

# print也可以打印一个表达式
print(1 + 2 + 3)
print('1 + 2 + 3')  # 当前打印的是一串字符串 不是表达式

int_data_1 = 3
int_data_2 = 4
int_data_3 = 5
print(int_data_1 + int_data_2 + int_data_3)

"""
进阶用法
"""
# 如果需要输出多个值, 则在多个值中间通过逗号进行分割
print(10, 20, 30)

num_1 = 1
num_2 = 2
num_3 = 3
print(num_1, num_2, num_3)
