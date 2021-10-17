import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from ..items import NationalSolidPollutionItem
import time
import math
import os
import collections
from scrapy.exceptions import CloseSpider
from urllib import parse
class NationalSolidPollutionSpider(scrapy.Spider):
	kwlist = ''
	def __init__(self, count=None, kws=None, districts=None, start_year=None, end_year=None, *args, **kwargs):
		super(NationalSolidPollutionSpider, self).__init__(*args, **kwargs)
		self.kw_list = kws.split('#')
		self.district_list = districts.split('#')
		self.maxCount = int(count)
		self.currentCount = 0
		self.start_year = start_year
		self.end_year = end_year

	name = 'nationalsolidpollution'

	# start_urls = ['http://data.cnki.net/ValueSearch/Index?datatype=year&ky=GDP']
	# cookies = 'Ecp_ClientId=4200613173102958016; ASP.NET_SessionId=vy5dpiyfhfqqzsa4rt5v4o4e; SID=009022; Hm_lvt_911066eb2f53848f7d902db7bb8ac4d7=1592040708,1592406494; Ecp_IpLoginFail=200618183.195.65.196; Hm_lpvt_911066eb2f53848f7d902db7bb8ac4d7=1592481109',
	custom_settings = {
		'DOWNLOAD_DELAY': 0,
		'COOKIES_ENABLED': True,
		'LOG_LEVEL': 'INFO',
		'RETRY_TIMES': 15,
		'DEFAULT_REQUEST_HEADERS': {
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, zh-Hant-TW; q=0.5, zh-Hant; q=0.3',
			'Cache-Control': 'no-cache',
			'Connection': 'Keep-Alive',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Referer': 'http://data.cnki.net/ValueSearch/Index?datatype=year&ky=GDP',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'X-Request-With': 'XMLHttpRequest'
		},
		'ITEM_PIPELINES': {
			'crawldata.pipelines.NationalSolidPollutionPipeline': 301,
		}
	}

	def start_requests(self):
		for i in range(len(self.kw_list)):
			url = 'http://data.cnki.net/ValueSearch/Index?datatype=year&ky=' + self.kw_list[i]
			yield scrapy.Request(url, dont_filter=True)

	def parse(self, response):
		"""
					采集国内固体废弃物数据
					:param response:
					:return:item
		"""
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--no-sandbox')
		driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=os.path.dirname(os.path.dirname(__file__)) +'/chromedriver.exe')
		driver.get(response.url)

		try:
			for i in range(len(self.district_list)):
				inputDistrict = driver.find_element_by_name("IndicateRegion")
				inputDistrict.clear()
				inputDistrict.send_keys(self.district_list[i])
				select_start = Select(driver.find_element_by_id('StartYear'))
				select_end = Select(driver.find_element_by_id('EndYear'))
				select_start.select_by_visible_text(self.start_year)
				select_end.select_by_visible_text(self.end_year)
				button = driver.find_element_by_id('AdvancedSearch')
				button.click()
				time.sleep(3)
				counts = float(driver.find_element_by_xpath('//span[@id="Count"]').text)
				pages = math.ceil(counts / 50)
				pagesize = driver.find_element_by_xpath('//ul[@id="pageSelect"]/li[3]')
				pagesize.click()
				time.sleep(3)
				namelist = ['year', 'area', 'index', 'value', 'unit', 'source']
				for id in range(pages):
					table = driver.find_elements_by_xpath('//table[@id="t1"]/tbody/tr')
					for i in range(len(table)):
						if self.currentCount < self.maxCount:
							self.currentCount += 1
							item = collections.OrderedDict(NationalSolidPollutionItem())
							td=driver.find_elements_by_xpath('//table[@id="t1"]/tbody/tr'+'['+str(i+1)+']/td')
							print(td[2].text)
							for j in range(6):
								if j == 3:
									item[namelist[j]] = float(td[j + 2].text)
								else:
									item[namelist[j]] = td[j + 2].text
							yield item
						else:
							raise CloseSpider('close it')
					nextpage = driver.find_element_by_xpath('//li[@id="NextPage"]')
					nextpage.click()
					time.sleep(2)

		except Exception as e:
			print(e)
		driver.quit()

#################################post请求#############################################
# data={
#     "ky": "GDP",
#     "length": "\n                        20\n                    ",
#     "sort": "0",
#     "start": "1",
#     "datatype": "year",
#     "searchMethod": "1",
#     "name": "垃圾",
#     "type": "0",
#     "region": "",
#     "startyear": "2019",
#     "endyear": "2019"
# }
# formdata = json.dumps(data).encode('utf-8')

# yield scrapy.Request(post_url,method='POST',body=formdata,cookies=cookies_dict,headers={
#         'Accept': '*/*',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, zh-Hant-TW; q=0.5, zh-Hant; q=0.3',
#         'Cache-Control': 'no-cache',
#         'Connection':'Keep-Alive',
#         # 'Cookie': 'Ecp_ClientId=4200613173102958016; ASP.NET_SessionId=vy5dpiyfhfqqzsa4rt5v4o4e; SID=009022; Hm_lvt_911066eb2f53848f7d902db7bb8ac4d7=1592040708,1592406494; Hm_lpvt_911066eb2f53848f7d902db7bb8ac4d7=1592469341',
#         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#         'Referer':'http://data.cnki.net/ValueSearch/Index?datatype=year&ky=GDP',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
#         'X-Request-With':'XMLHttpRequest'
#     },callback=self.parse)
