# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用多继承的方式完成手机类的编辑.py
# @Software: PyCharm
# @Time    : 2023/11/8 20:14


# 开发思维: 把项目整体以功能为单位进行拆分, 可以将这些功能封装一个类
class Camera:
    def take_photo(self):
        print('拍照...')


class PlayGame:
    def play(self):
        print('玩游戏...')


class Phone(Camera, PlayGame):
    def call(self):
        print('打电话...')


iphone = Phone()
iphone.call()
iphone.take_photo()
iphone.play()