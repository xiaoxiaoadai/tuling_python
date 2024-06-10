# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 13.文件对象使用完成之后必须进行释放.py
# @Software: PyCharm
# @Time    : 2023/11/17 21:14


file_name = '测试文件.txt'

file_obj = open(file_name, 'r')
print(file_obj.read())

# 释放文件对象
file_obj.close()
