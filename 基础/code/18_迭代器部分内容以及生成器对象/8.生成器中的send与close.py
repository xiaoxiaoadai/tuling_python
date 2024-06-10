# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.生成器中的send与close.py
# @Software: PyCharm
# @Time    : 2023/11/13 21:44


"""
send与close是生成器对象内置的方法
    send:用来发送信号, 根据信号控制生成器返回的值

    close:关闭生成器对象
"""


def my_range(number):
    i = 0
    while i < number:
        value = yield i
        if value == '你好':
            print('发送的值为: ', value)
        else:
            print('123')
        i += 1


my_ = my_range(3)
print(my_.send('123'))  # 不能再第一行
print(next(my_))
print(my_.send('你好'))  # 可以发送一个信号
my_.close()  # 关闭生成器对象
print(next(my_))


"""
1.send具有next取值的功能, 并且可以往生成器内部代码发送信号控制代码流程
2.send不能运行在第一行
"""


