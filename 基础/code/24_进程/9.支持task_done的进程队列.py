# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.支持task_done的进程队列.py
# @Software: PyCharm
# @Time    : 2023/11/24 22:09


from multiprocessing import Process, JoinableQueue as Queue  # 支持task_done操作

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


if __name__ == '__main__':
    p1 = Process(target=get_value_1, args=(q_1,))
    p2 = Process(target=get_value_2, args=(q_2,))

    for process_obj in [p1, p2]:
        process_obj.daemon = True
        process_obj.start()

    # 堵塞主进程
    for q in [q_1, q_2]:
        q.join()

    print('主进程代码...')
