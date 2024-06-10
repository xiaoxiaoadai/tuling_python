# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 下午9:24
# @Author  : 顾安
# @File    : 1.案例演示.py
# @Software: PyCharm


have_friend = False

# if默认判断的条件是成立的
# if have_friend条件为True 则不需要写: if have_friend == True
"""
== 对两个或多个变量进行比较
"""

if have_friend:
    # 当前条件如果不成立则不运行if判断语句下面的print代码
    print('你有朋友...')


"""
作用域:
    如果代码结尾是冒号则代表开启作用域
    
1.在if判断语句中如果开启了作用域则冒号后面的代码需要换行
2.换行的代码需要缩进: 当前代码需要留出4个空格, pycharm会自动处理
    如果大家使用的是其他编辑器可能需要自己手写4个空格, 键盘中的tab键默认是四个空格
    
作用域的功能是: 作用域内部的代码受到上一行代码的控制
"""



