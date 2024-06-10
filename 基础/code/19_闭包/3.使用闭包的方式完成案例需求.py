# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用闭包的方式完成案例需求.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:10


def person(user_name):
    def say(content):
        print(f'{user_name}: {content}')
    return say


p1 = person('安娜')
p2 = person('双双')

p1("今天吃了么？")
p2("吃了~")
p1("吃了啥？")
p2("半只牛~")
p1("为啥不给我吃？")
p2("我一个人刚刚好~~")
p1("友谊的小船说翻就翻！")
p2("我会游泳~~~")