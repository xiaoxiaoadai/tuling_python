# -*- coding: utf-8 -*-
"""
Created on 2023-12-21 20:09:25
---------
@summary:
---------
@author: poppies
"""

import time
import json
import feapder
from feapder.utils.webdriver import WebDriver


class JobInfo(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://q.yingjiesheng.com/jobs/search/Python?jobarea=220200", render=True)

    def parse(self, request, response):
        browser: WebDriver = response.browser
        time.sleep(1)  # 获取对应接口前延时一秒等待接口加载
        json_data = browser.xhr_json('open/noauth/job/search')
        for temp in json_data['resultbody']['searchData']['joblist']['items']:
            item = dict()
            item['jobname'] = temp['jobname']
            item['coname'] = temp['coname']
            item['jobarea'] = temp['jobarea']
            item['issuedate'] = temp['issuedate']
            item['jobtag'] = temp['jobtag']
            item['providesalary'] = temp['providesalary']
            print(item)


if __name__ == "__main__":
    JobInfo().start()
