# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.缺省参数的使用场景.py
# @Software: PyCharm
# @Time    : 2023/11/1 20:48


"""
如果一个功能中的参数可以被确定, 则可以使用缺省参数
    当然, 如果这个值需要被修改, 也可以完成修改操作
"""

def print_stu_info(name, age, gender, school_name='图灵学院'):
    print(f'姓名: {name}, 年龄: {age}, 性别: {gender}, 学校: {school_name}')


print_stu_info('安娜', 18, '女')


"""
使用缺省参数的注意事项
    缺省参数的位置必须要在形式参数的后面
"""

# 错误声明
# def print_stu_info(school_name='图灵学院', name, age, gender):
#     print(f'姓名: {name}, 年龄: {age}, 性别: {gender}, 学校: {school_name}')
#
#
# print_stu_info('安娜', 18, '女')
