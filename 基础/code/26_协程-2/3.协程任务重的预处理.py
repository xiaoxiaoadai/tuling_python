# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.协程任务重的预处理.py
# @Software: PyCharm
# @Time    : 2023/11/29 20:27


import asyncio


async def work():
    print(1)
    await asyncio.sleep(1)
    print(2)


async def main():
    # 在当前函数的内部将以上的写成任务手动打包成一个task对象
    """
    当一个协程对象被手动打包成一个task任务时, python解释器会先运行当前被打包的这个任务的内部代码
        一旦运行到IO耗时操作的代码的时, 停止运行。
    :return:
    """
    task = asyncio.create_task(work())  # 当前代码只是对上面的任务进行了打包并没有使用await调度任务


asyncio.run(main())
