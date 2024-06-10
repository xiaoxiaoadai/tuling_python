# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.自定义异常类.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:30


class PassWordError(Exception):  # 自定义异常类一定要继承Exception
    def __str__(self):  # __str__方法作用与print方法
        return '用户名或密码错误...'

    def __repr__(self):  # __repr__作用与python交互环境: ipython\python
        return '用户名或密码错误...'


name = input('请输入用户名:')
password = input('请输入密码:')


local_name = '安娜'
local_password = 'admin'


try:
    if name != local_name or password != local_password:
        raise PassWordError
except PassWordError as e:
    print(e)


