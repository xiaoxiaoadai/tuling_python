# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.将协程函数封装为一个异步生成器.py
# @Software: PyCharm
# @Time    : 2023/12/1 21:12


import asyncio


# 当前的写成函数是一个异步生成器对象
async def func():
    for i in range(100):
        yield i


async def main():
    # 异步生成器对象必须使用异步for循环执行
    async for i in func():
        print(i)


asyncio.run(main())


