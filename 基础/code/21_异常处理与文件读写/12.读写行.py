# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 12.读写行.py
# @Software: PyCharm
# @Time    : 2023/11/17 21:11


file_name = '测试文件.txt'


data_list = ['\n你好', '\n很高兴认识你', '\n欢迎大家学习爬虫课程...']
file_obj = open(file_name, 'w')
file_obj.writelines(data_list)
