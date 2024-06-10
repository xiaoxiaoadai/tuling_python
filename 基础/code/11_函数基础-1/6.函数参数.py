# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.函数参数.py
# @Software: PyCharm
# @Time    : 2023/10/27 21:48


"""
在函数内部执行的代码中可能存在变量, 这个变量是使用者传递过来的数据
    这些数据需要通过函数参数的方式进行数据接收
"""

# 登录功能
local_name = 'admin'
local_password = '123456'


# 当前函数中定义的两个形参是需要在调用函数的时候将具体的值传递给对应的形参
def login(username, password):
    # 将用户传递的数据与本地数据进行校验
    if username == local_name and password == local_password:
        print('登录成功')
    else:
        print('登录失败')


login('安娜', '123456')
