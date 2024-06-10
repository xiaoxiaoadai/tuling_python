# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.进程中的队列.py
# @Software: PyCharm
# @Time    : 2023/11/24 21:56


from multiprocessing import Process, Queue  # 当前的Queue对象不支持task_done


def insert_queue(queue):
    for num in [1, 2, 3, 4]:
        queue.put(num)


def get_queue(queue):
    while True:
        if not queue.empty():
            num = queue.get()
            print('从队列中获取到的值为:', num)
        else:
            break


if __name__ == '__main__':
    queue = Queue()
    q_insert = Process(target=insert_queue, args=(queue,))
    q_get = Process(target=get_queue, args=(queue,))

    q_insert.start()
    q_insert.join()

    q_get.start()
    q_get.join()

    print('主进程任务完成...')


"""
1.队列对象必须要在主进程中创建
2.子进程可以访问同一个队列对象
3.队列对象的操作是原子性的: 线程安全
"""