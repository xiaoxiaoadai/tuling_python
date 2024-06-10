# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.事件循环调度任务的不同方式.py
# @Software: PyCharm
# @Time    : 2023/11/29 20:02


import asyncio


async def func():
    print(1)
    await asyncio.sleep(1)
    print(2)
    return '123'


# 方式一: 手动创建事件循环对象调度任务
# loop = asyncio.get_event_loop()
# coro_list = [func() for _ in range(3)]
# loop.run_until_complete(asyncio.wait(coro_list))


# 方式二: 使用run方法自动创建事件循环对象并调度任务
# coro_list = [func() for _ in range(3)]
# asyncio.run(asyncio.wait(coro_list))


# 方式三: 将多个协程对象手动打包成task/future对象并调度运行  3.11 - 3.12版本中使用
async def main():
    tasks = [asyncio.create_task(func()) for _ in range(3)]
    await asyncio.wait(tasks)

asyncio.run(main())