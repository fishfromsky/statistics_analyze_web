import scrapy
from ..items import NationalPMItem
import re
import urllib
import collections
class NationalPMSpider(scrapy.Spider):
    name = 'nationalpm'
    start_urls = ['http://www.pm25.in/']
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
            'crawldata.pipelines.NationalPMPipeline': 301,
        }
    }

    def parse(self,response):
     """
            采集所有子分类的链接
            :param response:
            :return: detail response
            """
     allcitydiv = response.xpath('//div[@class="all"]')[0]
     allcityurls = allcitydiv.xpath('.//li/a/@href').extract()
     for url in allcityurls:
        url = urllib.parse.urljoin(response.url,url)
        # print("22222222222")
        yield scrapy.FormRequest(url=url, method='get', callback=self.parsedata)

    def parsedata(self, response):
        """
                    采集国内空气污染数据
                    :param response:
                    :return: item
        """
        try:
             namelist = ['city', 'check_area', 'AQI', 'air_quality', 'pollutant', 'pm2_5', 'pm10', 'co', 'no2', 'o3_1h',
                        'o3_8h', 'so2', 'update_time']
             city_name = response.xpath('//div[@class="city_name"]/h2/text()').extract()[0]
             update_time = response.xpath('//div[@class="live_data_time"]/p/text()').extract()[0]
             update_time = update_time.replace("数据更新时间：","")
             table = response.xpath('//table[@id="detail-data"]/tbody/tr')
             for tr in table:
                item = collections.OrderedDict(NationalPMItem())
                td = tr.xpath('.//td')
                item[namelist[0]] = city_name
                for i,data in enumerate(td):
                    if len(data.xpath('.//text()').extract())==0:
                        item[namelist[i+1]] = ''
                    else:
                        item[namelist[i+1]] = data.xpath('.//text()').extract()[0]
                item[namelist[-1]] = update_time
                # print(item)
                yield item
        except Exception as e:
             print(e)



