# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.复习-协程并发.py
# @Software: PyCharm
# @Time    : 2023/12/1 20:00


# 任务1对一个全局变量进行循环 + 1
# 任务2对一个全局变量进行循环 - 1
# 启动函数打印最终的结果
import asyncio


num = 0


async def add():
    global num
    for _ in range(100000):
        num += 1


async def sub():
    global num
    for _ in range(100000):
        num -= 1


async def main():
    # await add()
    # await sub()

    # futures = [asyncio.ensure_future(add()), asyncio.ensure_future(sub())]

    # tasks = [asyncio.create_task(add()), asyncio.create_task(sub())]

    loop = asyncio.get_running_loop()
    tasks = [loop.create_task(add()), loop.create_task(sub())]  # 不建议大家使用
    await asyncio.wait(tasks)
    print(num)

asyncio.run(main())




