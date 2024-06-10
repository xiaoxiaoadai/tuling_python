# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.获取进程的pid.py
# @Software: PyCharm
# @Time    : 2023/11/24 20:28


"""
进程被操作系统启动之后, 会随机分配一个进程编号
"""

import os
import multiprocessing


def get_pid():
    print(f'子进程pid编号为: {os.getpid()}, 当前父进程pid编号为: {os.getppid()}')


if __name__ == '__main__':
    p = multiprocessing.Process(target=get_pid)
    p.start()
    print('当前程序的父进程为:', os.getppid())


"""
获取当前进程本身编号: os.getpid()
获取当前进程的父进程编号: os.getppid()
"""
