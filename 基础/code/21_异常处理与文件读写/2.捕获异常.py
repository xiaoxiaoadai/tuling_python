# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.捕获异常.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:04



try:
    print(a)
except:
    print('程序有错误...')

"""
在python中有一种特殊的语法可以防止程序因为报错而导致崩溃
    try:
        要执行的代码...
    except:
        如果发生异常则执行什么代码...
        
        
    if:
        pass
    else:
        pass
"""
