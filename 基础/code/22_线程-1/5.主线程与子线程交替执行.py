# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.主线程与子线程交替执行.py
# @Software: PyCharm
# @Time    : 2023/11/20 21:01


import time
import threading


def work():
    time.sleep(10)
    print('这是一个子线程任务...')


t = threading.Thread(target=work)

t.daemon = True  # 当前子线程是一个守护线程

t.start()

print('主线程被执行, 并且主线程即将退出...')


"""
在默认情况下, 主线程和子线程启动之后各自运行本身绑定的任务
    主线程在运行到最后一行代码的时候会等待子线程任务完成
        主线程在默认情况下要等待子线程任务全部完成之后才会退出程序
        
        
守护线程的主要功能:
    因为在默认情况下主线程要等待所有子线程任务完毕之后才能退出程序, 所以如果有一个子线程因为代码逻辑问题陷入了死循环
        主程序是无法退出的
    
    可以让子线程变成一个守护线程, 主线程执行到最后一行代码时发现子线程任务还没有完成, 如果是守护线程的情况下
        则主线程立即退出, 主程序退出之后, 子线程无论任务是否完成也会被强制退出
"""

