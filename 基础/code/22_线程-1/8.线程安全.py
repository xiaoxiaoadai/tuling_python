# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.线程安全.py
# @Software: PyCharm
# @Time    : 2023/11/20 21:50


"""
多个线程存在于一个进程中, 在进程中的资源多个线程是共享的
    在一个线程执行任务的过程中如果遇到任务切换会导致其他线程损坏原有线程计算的结果
"""

import threading
from threading import Lock

num = 0
lock_obj = Lock()


# 资源共享
def _add():
    global num
    for _ in range(1000000):
        lock_obj.acquire()  # 上锁
        num += 1
        lock_obj.release()  # 解锁


def _sub():
    global num
    for _ in range(1000000):
        lock_obj.acquire()
        num -= 1
        lock_obj.release()


t1 = threading.Thread(target=_add)
t2 = threading.Thread(target=_sub)

t1.start()
t2.start()

t1.join()
t2.join()

print('主线程打印信息:', num)


"""
如何避免原子性代码被切换执行？
    使用线程中的线程锁对象
"""