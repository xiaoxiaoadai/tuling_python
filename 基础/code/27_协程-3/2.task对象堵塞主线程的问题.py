# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.task对象堵塞主线程的问题.py
# @Software: PyCharm
# @Time    : 2023/12/1 20:17


import asyncio


async def main():
    # 获取一个正在运行的事件循环对象, 如果不存在则抛出异常
    loop = asyncio.get_running_loop()

    # 创建一个future对象
    fut_1 = loop.create_future()

    # 创建一个task对象
    # task_2 = loop.create_task()
    # task_2.set_result()

    # 在获取返回值之前设置一个返回值
    fut_1.set_result(123)

    result = await fut_1
    print(result)


asyncio.run(main())
