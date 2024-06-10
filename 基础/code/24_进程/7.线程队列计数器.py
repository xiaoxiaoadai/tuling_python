# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.线程队列计数器.py
# @Software: PyCharm
# @Time    : 2023/11/24 21:45


# 队列计数器
"""
1. 请求网站并获取网站页面源代码
	队列中
	200万个url
	死循环

2.获取页面源代码并进行页面分析
	死循环
	从队列中获取源代码
	得到的结果上传到一个新的队列中


3.拿到分许后的数据进行数据入库
	死循环
	从新队列中获取到分析后的数据并进行数据库入库


线程为例：普通线程  守护线程
	主线程执行到代码最后一行直接退出

设置一个条件: 如果三个队列中的值全部取完之后没有值了则解主线程
堵塞

队列中提供了一个方法 堵塞主线程的方法：join
	判断的是三个队列中默认的计数器的值为0
	把队列中的值单纯取完是不会接堵塞的
		get不会让计数器减1
		使用task_done的方式让计数器减1
"""
import threading
from queue import Queue

q_1 = Queue()
q_2 = Queue()

q_1.put(1)
q_1.put(2)
q_1.put(3)

q_2.put(1)
q_2.put(2)
q_2.put(3)


def get_value_1(queue):
    while True:
        print(queue.get())
        queue.task_done()


def get_value_2(queue):
    while True:
        print(queue.get())
        queue.task_done()


t1 = threading.Thread(target=get_value_1, args=(q_1,))
t2 = threading.Thread(target=get_value_2, args=(q_2,))

for thread_obj in [t1, t2]:
    thread_obj.daemon = True
    thread_obj.start()

# 堵塞主线程
for q in [q_1, q_2]:
    q.join()

print('主线程代码...')
