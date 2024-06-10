# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.finally在异常语句中的使用.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:25


try:
    # print(9 / 0)
    print('代码测试')
# Exception: 是所有错误类的基类
except Exception as e:
    print('代码异常:', e)
else:
    print('如果代码没有发生异常的情况下则当前语句被执行...')
finally:
    print('无论当前程序是否发生异常当前语句一定会执行...')

