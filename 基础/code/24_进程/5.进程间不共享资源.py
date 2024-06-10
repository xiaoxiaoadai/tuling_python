# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.进程间不共享资源.py
# @Software: PyCharm
# @Time    : 2023/11/24 20:46


import multiprocessing

nums = [1, 2, 3]


def work_1():
    for i in range(4, 7):
        nums.append(i)
    print('子进程一任务完成后列表中的元素为:', nums)


def work_2():
    print('子进程二任务完成后列表中的元素为:', nums)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work_1)
    p2 = multiprocessing.Process(target=work_2)

    p1.start()
    p1.join()

    p2.start()

