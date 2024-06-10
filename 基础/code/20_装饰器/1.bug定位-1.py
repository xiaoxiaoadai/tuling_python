# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.bug定位-1.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:46


def say_hello():
    print('[DEBUG]: say_hello')
    print("hello!")


def say_goodbye():
    print('[DEBUG]: say_goodbye')
    print("hello!")  # 此处应打印goodbye


if __name__ == '__main__':
    say_hello()
    say_goodbye()