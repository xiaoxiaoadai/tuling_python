# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.python中线程对象的方法.py
# @Software: PyCharm
# @Time    : 2023/11/20 21:23


"""
start
    在创建完线程对象之后, 线程不会立即创建, 需要启动线程之后操作系统才创建一个线程对象出来
"""

# import threading
#
# t = threading.Thread(target=None)
# t.daemon = True
"""
daemon
    将子线程设置为一个守护线程
        主线程执行到最后一行代码的时候,不会等待子线程的任务完成, 立即退出程序
        子线程会随着主线程的退出而退出
"""

# t.join()
"""
join
    子线程如果设置为join的话, 则主线程会发生堵塞, 直到设置的子线程任务完成之后主线程才会解堵塞
"""

# import threading
#
#
# def work():
#     print('线程任务...')
#     name = threading.current_thread().getName()
#     print(name)
#
#
# t = threading.Thread(target=work)
# t.setName('子线程-1')
# t.start()

"""
current_thread()
    获取线程对象内部的引用信息
"""
