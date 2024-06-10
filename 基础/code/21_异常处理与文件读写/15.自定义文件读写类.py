# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 15.自定义文件读写类.py
# @Software: PyCharm
# @Time    : 2023/11/17 21:28


class MyOpenFile:
    def __init__(self, file_name):
        self.file_obj = None
        self.file_name = file_name

    def __enter__(self):
        print(1)
        self.file_obj = open(self.file_name, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(2)
        self.file_obj.close()

    def my_read(self):
        print(self.file_obj.read())


with MyOpenFile('测试文件.txt') as my_file:
    my_file.my_read()
