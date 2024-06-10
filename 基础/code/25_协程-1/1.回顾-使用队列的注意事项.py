# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.回顾-使用队列的注意事项.py
# @Software: PyCharm
# @Time    : 2023/11/27 20:01


import time
from queue import Queue
from threading import Thread, RLock


lock = RLock()
nums = [1, 2, 3, 4]


def put_work(q):
    with lock:
        for i in nums:
            q.put(i)
            time.sleep(1)


def get_work(q):
    with lock:
        while True:
            if not q.empty():
                value = q.get()
                print(value)
                q.task_done()
            else:
                print('队列为空...')


if __name__ == '__main__':
    queue = Queue()
    thread_list = list()
    put_work(queue)
    thread_list.append(Thread(target=get_work, args=(queue,)))

    for t in thread_list:
        t.daemon = True
        t.start()

    queue.join()
    print('主线程结束...')


"""
1.第一个任务如果是在队列中上传数据最好让主线程执行第一个任务, 确保任务全部上传到队列
2.在上传代码处加锁, 一处加锁, 处处加锁
"""
