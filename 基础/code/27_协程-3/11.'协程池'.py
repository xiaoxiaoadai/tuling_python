# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.'协程池'.py
# @Software: PyCharm
# @Time    : 2023/12/1 22:02


import random
import asyncio
from asyncio import as_completed


async def my_task(name):
    print(f'Task {name} 启动...')
    await asyncio.sleep(random.randint(1, 3))
    print(f'Task {name} 结束...')
    return f'任务: {name}'


async def main():
    # 创建一个协程池: [信号量]
    sem = asyncio.Semaphore(3)

    tasks = list()
    for i in range(1, 6):
        # 使用协程池控制任务数量
        async with sem:
            tasks.append(asyncio.create_task(my_task(i)))


asyncio.run(main())
