# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : push_start_url.py
# @Software: PyCharm
# @Time    : 2023/12/14 21:22

import json
import redis


def push_start_url_form_data(db, request_obj):
    """
    :param db:
    :param request_obj: {'url': url, 'form_data': form_data, 'meta': meta}
    :return:
    """
    db.lpush('jc:start_urls', request_obj)


if __name__ == '__main__':
    redis_client = redis.Redis()
    for page in range(1, 21):
        form_data = {
            "column": "szse_latest",
            "pageNum": str(page),
            "pageSize": "30",
            "sortName": "",
            "sortType": "",
            "clusterFlag": "true"
        }

        request_data = {
            'form_data': form_data
        }
        push_start_url_form_data(redis_client, json.dumps(request_data))
    redis_client.close()
