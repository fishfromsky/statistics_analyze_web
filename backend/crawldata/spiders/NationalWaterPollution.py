import scrapy
from ..items import NationalWaterPollutionItem
import re
import urllib
import pandas as pd
import os
import time
import collections
class NationalWaterPollutionSpider(scrapy.Spider):
    name = 'nationalwaterpollution'
    start_urls = ['http://123.127.175.45:8082/']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1000,
        'DOWNLOAD_DELAY': 0,
        'COOKIES_ENABLED': False,
        'LOG_LEVEL': 'INFO',
        'RETRY_TIMES': 15,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
        },
        'ITEM_PIPELINES': {
            'crawldata.pipelines.NationalWaterPollutionPipeline': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'crawldata.middlewares.AreaSpiderMiddleware': 543,
        },
    }

    def parse(self,response):
     """
            采集所有水体污染数据
            :param response:
            :return: item
            """
     try:

         namelist = ['name', 'check_time', 'PH', 'DO', 'AN', 'Mn', 'OC', 'sort', 'attr', 'situation']
         table = response.xpath('//li[@class="news-item"]')
         for tr in table:
             item = collections.OrderedDict(NationalWaterPollutionItem())
             td = tr.xpath('.//td')
             for i, data in enumerate(td):
                 if len(data.xpath('.//text()').extract()) == 0:
                     item[namelist[i]] = ''
                 else:
                     item[namelist[i]] = data.xpath('.//text()').extract()[0]
             yield item
     except Exception as e:
         print(e)





