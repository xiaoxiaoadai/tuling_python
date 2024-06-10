# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.在异常中使用else.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:22


try:
    print(9 / 0)
except:
    print('代码异常')
else:
    print('如果程序没有出现任何异常的情况下, 则执行当前语句...')