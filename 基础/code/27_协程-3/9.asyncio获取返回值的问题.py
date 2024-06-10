# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.asyncio获取返回值的问题.py
# @Software: PyCharm
# @Time    : 2023/12/1 21:30


import asyncio


async def func(x):
    print(x)
    return f'返回值: {x}'


# coro_obj = func(10)
# loop = asyncio.get_event_loop()
# task = loop.create_task(coro_obj)
#
# res = loop.run_until_complete(task)
# print()
# print('使用task对象本身获取结果:', task.result())


async def main():
    tasks = [asyncio.create_task(func(i)) for i in range(1, 11)]
    res_list = await asyncio.gather(*tasks)
    print(res_list)

asyncio.run(main())
