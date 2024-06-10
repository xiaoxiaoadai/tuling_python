# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.异步IO程序.py
# @Software: PyCharm
# @Time    : 2023/11/27 21:22


"""
异步与同步的区别:
    同步:一个线程只能执行一个任务
    异步: 同一个线程对象可以切换多个任务[当前执行的任务没有完成也可以切换]
"""

import time
import asyncio  # 标准库

"""
同步程序
"""
# def func():
#     time.sleep(1)
#     print('我是同步任务...')
#
#
# time_ = lambda: time.time()
#
# now_time = time_()
# for i in range(5):
#     func()
#
# stop_time = time_()
# print('同步程序耗时为:', stop_time - now_time)


"""
异步程序
    在函数的前面使用async关键字装饰, 则当前这个函数会被包装为协程函数
"""


async def func():
    asyncio.sleep(1)
    print('我是异步任务...')


# 协程函数不能直接启动
# 如果在调用协程函数时是不能直接运行的, 会给你返回一个协程对象
# a = func()
# print(a)

time_ = lambda: time.time()

# 创建事件循环对象去调度协程对象任务: 类似于next()方法运行生成器对象
loop = asyncio.get_event_loop()
tasks = [loop.create_task(func()) for _ in range(5)]  # task对象
start = time_()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'异步花费的时间为:', time_() - start)


"""
1. 协程函数需要使用async关键字装饰
2. 协程函数不能直接执行, 调用协程函数时会返回协程对象
3. 执行协程对象需要事件循环对象, 当前不需要知道事件循环对象的作用
4. 调度协程任务需要使用asyncio中的run_until_complete方法进行任务调度执行
"""


