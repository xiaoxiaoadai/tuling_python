# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.await关键字.py
# @Software: PyCharm
# @Time    : 2023/11/29 20:36


import asyncio


async def others():
    print('开始任务...')
    await asyncio.sleep(10)
    print('任务结束...')
    return 123


async def main():
    print('正在运行main函数中的内部代码...')
    result = await others()  # 如果当前任务中有耗时任务会堵塞主线程
    # print(result)

# python3.7语法
# asyncio.run(main())

# python3.6语法
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

"""
1.await可以进行任务调度运行
2.await可以获取对应任务的返回值
3.await等待任务的返回值, 如果当前任务没有返回值则会造成线程堵塞
"""
