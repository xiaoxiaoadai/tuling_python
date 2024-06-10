# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 16.使用同一个文件对象完成读写任务.py
# @Software: PyCharm
# @Time    : 2023/11/17 21:33


with open('测试文件.txt', 'w+') as f:
    # 在进行数据写入的时候文件指针对象会随着字符写入而发生后移
    f.write('欢迎大家来到图灵学院学习python开发...')

    # 文件指针归位
    f.seek(0)

    result = f.read()
    print(result)

