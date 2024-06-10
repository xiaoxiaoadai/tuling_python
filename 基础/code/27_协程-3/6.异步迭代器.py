# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.异步迭代器.py
# @Software: PyCharm
# @Time    : 2023/12/1 21:04


import asyncio


class Reader:
    def __init__(self):
        self.count = 0

    async def read_line(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):  # 普通方法
        return self

    async def __anext__(self):  # 协程方法
        value = await self.read_line()
        if value is None:
            raise StopAsyncIteration
        return value


async def main():
    async for i in Reader():
        print(i)

asyncio.run(main())
