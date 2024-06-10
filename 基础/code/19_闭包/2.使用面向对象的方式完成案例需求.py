# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.使用面向对象的方式完成案例需求.py
# @Software: PyCharm
# @Time    : 2023/11/15 20:05


class SendMessage(object):
    def __init__(self, user_name):
        self.user_name = user_name

    def say(self, content):
        print(f'{self.user_name}: {content}')


p1 = SendMessage('安娜')
p2 = SendMessage('双双')

p1.say("今天吃了么？")
p2.say("吃了~")
p1.say("吃了啥？")
p2.say("半只牛~")
p1.say("为啥不给我吃？")
p2.say("我一个人刚刚好~~")
p1.say("友谊的小船说翻就翻！")
p2.say("我会游泳~~~")
