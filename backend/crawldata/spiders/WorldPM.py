import scrapy
from ..items import WorldPMItem
import re
import urllib
import pandas as pd
import os
import time
import collections
class WorldPMSpider(scrapy.Spider):
    name = 'worldpm'
    start_urls = ['https://aqicn.org/map/world/cn/']
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
            'crawldata.pipelines.WorldPMPipeline': 301,
        }
    }

    def parse(self,response):
     """
            采集所有国家的链接
            :param response:
            :return: detail response
            """
     countrylist = response.xpath('//span[@class="country"]')
     for country in countrylist:
         country_url = country.xpath('.//a/@href').extract()[0]
         if country_url!='http://aqicn.org/map/china/cn/':
            yield scrapy.FormRequest(url=country_url, method='get', callback=self.parsecountry)

    def parsecountry(self,response):
     """
            采集所有地区的链接
            :param response:
            :return: detail response
            """
     arealist = response.xpath('//div[@id="map-stations"]/a/@href').extract()
     for area_url in arealist:
         yield scrapy.FormRequest(url=area_url, method='get', callback=self.parsedata)

    def parsedata(self, response):
        """
                    采集各国空气污染数据
                    :param response:
                    :return: item
        """
        if response.xpath('//div[@id="citydivouter"]'):
                item = collections.OrderedDict(WorldPMItem())
                table = response.xpath('//div[@id="citydivouter"]')[0]
                update_time = ''.join(
                    response.xpath('//div[@class="aqifshare-mobile"]/center/div[2]/div/span/text()').extract())
                item['update_time'] = ''.join(
                    re.findall(r'[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日.*[0-9]{2}:[0-9]{2}', update_time))
                item['check_area'] = response.xpath('//div[@id="h1header1"]/b/text()').extract()[0]
                item['AQI'] = table.xpath('.//div[@id="aqiwgtvalue"]/text()').extract()[0]
                item['air_quality'] = ''.join(
                    response.xpath('//div[@class="aqifshare-mobile"]/center/div[2]/div/span/b/text()').extract())

                pollutant_dict = {}
                pm2_5 = table.xpath('.//td[@id="cur_pm25"]/text()').extract()
                pm10 = table.xpath('.//td[@id="cur_pm10"]/text()').extract()
                o3 = table.xpath('.//td[@id="cur_o3"]/text()').extract()
                no2 = table.xpath('.//td[@id="cur_no2"]/text()').extract()
                so2 = table.xpath('.//td[@id="cur_so2"]/text()').extract()
                co = table.xpath('.//td[@id="cur_co"]/text()').extract()
                if pm2_5 and pm2_5[0]!='-':
                    pm2_5 = int(pm2_5[0])
                    pollutant_dict['PM2.5'] = pm2_5
                else:
                    pm2_5 = '-'
                if pm10 and pm10[0]!='-':
                    pm10 = int(pm10[0])
                    pollutant_dict['PM10'] = pm10
                else:
                    pm10 = '-'
                if o3 and o3[0]!='-':
                    o3 = int(o3[0])
                    pollutant_dict['O3'] = o3
                else:
                    o3 = '-'
                if no2 and no2[0]!='-':
                    no2 = int(no2[0])
                    pollutant_dict['NO2'] = no2
                else:
                    no2 = '-'
                if so2 and so2[0]!='-':
                    so2 = int(so2[0])
                    pollutant_dict['SO2'] = so2
                else:
                    so2 = '-'
                if co and co[0]!='-':
                    co = int(co[0])
                    pollutant_dict['CO'] = co
                else:
                    co = '-'
                if pollutant_dict:
                    item['pollutant'] = max(pollutant_dict, key=lambda x: pollutant_dict[x])
                else:
                    item['pollutant'] = '-'

                temperature = table.xpath('.//td[@id="cur_t"]/text()|.//td[@id="cur_t"]/span/text()').extract()
                air_pressure = table.xpath('.//td[@id="cur_p"]/text()|.//td[@id="cur_p"]/span/text()').extract()
                humidity = table.xpath('.//td[@id="cur_h"]/text()|.//td[@id="cur_h"]/span/text()').extract()
                wind = table.xpath('.//td[@id="cur_w"]/text()|.//td[@id="cur_w"]/span/text()').extract()
                if temperature and temperature[0]!='-':
                    temperature = int(temperature[0])
                else:
                    temperature = '-'
                if air_pressure and air_pressure[0]!='-':
                    air_pressure = int(air_pressure[0])
                else:
                    air_pressure = '-'
                if humidity and humidity[0]!='-':
                    humidity = int(humidity[0])
                else:
                    humidity = '-'
                if wind and wind[0]!='-':
                    wind = int(wind[0])
                else:
                    wind = '-'

                item['pm2_5'] = pm2_5
                item['pm10'] = pm10
                item['o3'] = o3
                item['no2'] = no2
                item['so2'] = so2
                item['co'] = co
                item['temperature'] = temperature
                item['air_pressure'] = air_pressure
                item['humidity'] = humidity
                item['wind'] = wind
                yield item


