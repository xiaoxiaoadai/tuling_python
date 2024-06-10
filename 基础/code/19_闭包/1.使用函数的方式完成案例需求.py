# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.使用函数的方式完成案例需求.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:01


"""
一个用户发送一条信息
    标记这个信息是谁发送的
"""


def message(user_name, content):
    print(f'{user_name}: {content}')


user_name_1 = '安娜'
user_name_2 = '双双'

message(user_name_1, "今天吃了么？")
message(user_name_2, "吃了~")

message(user_name_1, "吃了啥？")
message(user_name_2, "半只牛~")

message(user_name_1, "为啥不给我吃？")
message(user_name_2, "我一个人刚刚好~~")

message(user_name_1, "友谊的小船说翻就翻！")
message(user_name_2, "我会游泳~~~")
