# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.使用协程的方式调度requests同步爬虫库.py
# @Software: PyCharm
# @Time    : 2023/12/1 20:48


import asyncio
import requests


async def get_image(img_url):
    print('任务启动, 抓取的图片地址为:', img_url)
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, requests.get, img_url)
    response = await future

    file_name = img_url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)
        print('下载完成...')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

# python3.6一下语法
# loop = asyncio.get_event_loop()
# tasks = [loop.create_task(get_image(loop, url)) for url in url_list]
# loop.run_until_complete(asyncio.wait(tasks))


# python3.7以上语法
async def main(list_obj):
    tasks = [asyncio.create_task(get_image(url)) for url in list_obj]
    await asyncio.wait(tasks)

asyncio.run(main(url_list))



