# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.super关键字.py
# @Software: PyCharm
# @Time    : 2023/11/8 20:35


class Father:
    def play_game(self):
        print('玩游戏的方法...')


class Son(Father):
    def play_game(self):
        super().play_game()  # 可以在子类中通过super关键字调用父类的指定方法
        Father().play_game()
        print('子类中的玩游戏的方法...')


son = Son()
son.play_game()