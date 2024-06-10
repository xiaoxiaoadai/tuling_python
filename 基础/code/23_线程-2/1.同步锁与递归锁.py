# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.同步锁与递归锁.py
# @Software: PyCharm
# @Time    : 2023/11/22 20:01


import threading
from threading import Lock
from threading import RLock

"""
同步锁：Lock
    一个锁对象在使用过程中只能上锁和解锁一次
    
递归锁：
    一个锁对象在使用过程中可以上锁和解锁多次
    
对于锁对象都支持上下文管理协议
"""

num = 0
lock_obj_1 = Lock()  # 同步锁
lock_obj_2 = RLock()  # 递归锁  效率低

# 资源共享
def _add():
    global num
    for _ in range(1000000):
        with lock_obj_2:
            num += 1


def _sub():
    global num
    for _ in range(1000000):
        with lock_obj_2:
            num -= 1


t1 = threading.Thread(target=_add)
t2 = threading.Thread(target=_sub)

t1.start()
t2.start()

t1.join()
t2.join()

print('主线程打印信息:', num)
