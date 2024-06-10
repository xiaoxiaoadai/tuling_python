# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.协程嵌套.py
# @Software: PyCharm
# @Time    : 2023/11/29 20:47


import asyncio


async def others():
    print('开始任务...')
    await asyncio.sleep(10)
    print('任务结束...')
    return 123


async def main():
    print('正在执行main函数中的内部代码...')

    res_1 = await others()  # 当前await会等待调度任务的结束并获取返回值, 如果任务没有完成则造成线程堵塞

    print(res_1)
    res_2 = await others()
    print(res_2)


asyncio.run(main())


"""
多个协程对象使用await调度是一种同步程序
    await会等待调度任务的结束并获取返回值, 如果任务没有完成则造成线程堵塞
"""