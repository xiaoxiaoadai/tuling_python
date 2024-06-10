# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.并发任务.py
# @Software: PyCharm
# @Time    : 2023/11/20 20:15

import time
import threading  # 执行多线程并发程序的标准库


def work_1():
    print('任务1')
    time.sleep(2)


def work_2():
    print('任务2')
    time.sleep(2)


# 创建线程对象
t1 = threading.Thread(target=work_1)
t2 = threading.Thread(target=work_2)

# 使用线程对象调用线程启动方法
t1.start()
t2.start()


