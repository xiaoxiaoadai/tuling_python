# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.文件写入.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:57


"""
文件读写模式:
    r
    w
    a
"""


file_name = './测试文件.txt'  # 其实是一个路径: 相对路径

# 覆盖写
# file_obj = open(file_name, mode='w')
# file_obj.write('下午一起去爬山...')

# 追加写
file_obj = open(file_name, 'a')
file_obj.write('晚上一起去游泳...')


