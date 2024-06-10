# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.使用生成器完成爬虫任务.py
# @Software: PyCharm
# @Time    : 2023/11/13 22:03

import os
import requests  # 可以发送get请求并获取网站数据

url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page={}&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=jk&qv_id=CbsgU0To8B6747KNQb7gLskYSojZBRgo&source_tag=3&gaia_vtoken=&dynamic_offset=216&web_location=1430654&w_rid=fd9b61016c2ced0a937a7bb257d61bb9&wts=1699884353'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Referer': 'https://search.bilibili.com/all?',
    'Cookie': "buvid3=7DB15F34-87B2-5C2F-19F8-5A15E3BFC1C124392infoc; b_nut=1699601024; CURRENT_FNVAL=4048; _uuid=3B3C6EAF-C8AA-BC14-9E68-A98115D1EEBB25136infoc; buvid4=11FE7AD8-FB34-3A72-5353-333D5CD254AF25838-023111015-AiqhsCVq4si1d4bxIAtx4w%3D%3D; rpdid=|(umuum)~|Yl0J'uYmmY|u|kY; enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1920-853; fingerprint=1b5ef5973c9a31cfe10a3f8de0ee9b12; buvid_fp_plain=undefined; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTk5NTc4MjQsImlhdCI6MTY5OTY5ODU2NCwicGx0IjotMX0.uzovQF-Dk8UNtaWowC7mDn4LgrZdFEK75o5opK3VER8; bili_ticket_expires=1699957764; SESSDATA=d12d3b58%2C1715250625%2C54b51%2Ab1CjBhZs7pP1C-f3YnF-sR84UypbjN68LBVoZlqlHelKbihgG04JnDv6o6grk_xlhUsLISVk1MR0x2M1dleno3YzlWX3NhUTJ0REpiSnR6c1dDV0w1TFE5ZE9yNkFycFRiX3hPNzF3bkZhaHRXRXFiYTA5Vms4MHNDX1ZMdlRrQ3VvQmp1X2RQajFRIIEC; bili_jct=8e56b093ed306f64a87f5aa3b289befd; DedeUserID=508205460; DedeUserID__ckMd5=73fc57c2f075cc42; sid=799nas2r; buvid_fp=1b5ef5973c9a31cfe10a3f8de0ee9b12; CURRENT_QUALITY=116; innersign=0; b_lsid=410A6BD5B_18BC8FF23A8; bsource=search_google; PVID=1"
}


# 生成器函数
def get_image(page):
    response = requests.get(url.format(page), headers=headers).json()
    for item in response['data']['result']:
        yield item['upic']


index = 1

if not os.path.exists('./images'):
    os.mkdir('./images')

for item in get_image(1):
    with open('./images/' + str(index) + '.jpg', 'wb') as f:
        response = requests.get(item, headers=headers).content
        f.write(response)
        index += 1
