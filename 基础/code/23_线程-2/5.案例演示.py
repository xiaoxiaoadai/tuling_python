# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.案例演示.py
# @Software: PyCharm
# @Time    : 2023/11/22 21:35


import requests
import pymysql
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class BaiDu_recruit:
    lock_obj = Lock()

    def __init__(self):
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.38 Safari/537.36 '
                'JiSu/100.0.0.38',
            'Cookie':
                'BIDUPSID=79CD2B950C953D2974EBCBB2A349BDC0; PSTM=1700309560; BAIDUID=79CD2B950C953D29768F8CC83121D932:'
                'FG=1; newlogin=1; BA_HECTOR=aga52100ah81810ha4ah04261iln0h91q; H_PS_PSSID=39634_39672_39664_39695_396'
                '76_39679_39712_39745_39765_39675_39791_39704_39796; BAIDUID_BFESS=79CD2B950C953D29768F8CC83121D932:FG'
                '=1; ZFY=UCKb6gh1dvd:APcNl5hPihNzNfJwTHKlLjokVJxaF0w4:C; BDRCVFR[SeGfGLBpuj6]=mk3SLVN4HKm; BDORZ=B490B'
                '5EBF6F3CD402E515D22BCDA1598; Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1700496980; Hm_lpvt_50e85ccdd6c1'
                'e538eb1290bc92327926=1700497464; RT="z=1&dm=baidu.com&si=026d2ad1-3a33-452d-bc59-19c2259f3b46&ss=lp73'
                'zrvv&sl=5&tt=7dy&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=amb5"',
            'Referer':
                'https://talent.baidu.com/jobs/social-list?search=python'
        }
        self.sql = pymysql.connect(host='localhost', user='root', password='root', db='py_spider')
        self.sql_cursor = self.sql.cursor()

    def get_info(self, page):
        datas = {
            'recruitType': 'SOCIAL',
            'pageSize': '10',
            'keyWord': 'python',
            'curPage': page,
            'projectType': ''
        }
        response = requests.post(url=self.url, headers=self.headers, data=datas).json()
        result = response['data']['list']
        for info in result:
            info_dict = dict()
            info_dict['education'] = info['education'] if info['education'] else '空'
            info_dict['name'] = info['name'] if info['name'] else '空'
            info_dict['serviceCondition'] = info['serviceCondition'] if info['serviceCondition'] else '空'
            # print(info_dict)
            # self.save_info(info_dict)
            yield info_dict

    def creat_table(self):
        creat_table = '''
            create table if not exists BaiDu_recruit_info(
                    id int primary key auto_increment,
                    education varchar(200),
                    name varchar(100),
                    serviceCondition text
                );
        '''
        try:
            self.sql_cursor.execute(creat_table)
            print('创建表成功...')
        except Exception as e:
            print('创建表错误:', e)

    def save_info(self, info_dict):
        insert_info = '''
            insert into baidu_recruit_info(
            id, 
            education, 
            name, 
            serviceCondition) values(%s, %s, %s, %s);
        '''
        try:
            self.sql_cursor.execute(insert_info,
                                    (0, info_dict['education'], info_dict['name'], info_dict['serviceCondition']))
            self.sql.commit()
            print('数据插入成功:', info_dict['education'], info_dict['name'], info_dict['serviceCondition'])
        except Exception as e:
            print('数据插入失败:', e)
            self.sql.rollback()

    def main(self):
        self.creat_table()
        with ThreadPoolExecutor(max_workers=10) as pool:
            for page in range(1, 6):
                future = pool.submit(self.get_info, page)
            for dict_data in future.result():
                self.save_info(dict_data)
        print('任务结束...')

    def __del__(self):
        self.sql.close()
        self.sql_cursor.close()


if __name__ == '__main__':
    bd = BaiDu_recruit()
    bd.main()
