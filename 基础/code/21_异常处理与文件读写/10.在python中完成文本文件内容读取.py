# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.在python中完成文本文件内容读取.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:44


# 1. 定义当前存在的文件名称(需要后缀名)
file_name = '测试文件.txt'

# 2. 创建文件对象
file_obj = open(file_name, encoding='utf-8')  # 在windows系统中, 使用记事本创建的文本文件可能是GBK编码集
print(file_obj.readlines())


"""
文件对象中的读取方法:
    read(): 从文件开头读取到文件结尾
    readline(): 读取当前文件的第一行数据
    readlines(): 读取文件所有内容, 返回值是一个列表, 列表中的单个元素是文本中的一行
"""
