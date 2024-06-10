import scrapy
from scrapy import cmdline
from scrapy.http import JsonRequest


class ZhaoPinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["abc"]

    # start_urls = ["https://hr.163.com/api/hr163/position/queryPage"]

    def start_requests(self):
        api_url = 'https://hr.163.com/api/hr163/position/queryPage'
        for page in range(1, 279):
            json_data = {
                'currentPage': page,
                'pageSize': 10
            }
            yield JsonRequest(api_url, data=json_data)

    def parse(self, response, **kwargs):
        work_list = response.json()['data']['list']
        for work in work_list:
            item = dict()
            item['work_id'] = work['id']
            item['postTypeFullName'] = work['postTypeFullName']
            item['reqEducationName'] = work['reqEducationName']
            item['workPlaceNameList'] = work['workPlaceNameList'][0]
            item['requirement'] = work['requirement']

            yield item


if __name__ == '__main__':
    cmdline.execute('scrapy crawl zhaopin'.split())