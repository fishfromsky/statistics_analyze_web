#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import pandas as pd
import datetime

# # 更新代理
# from proxies import Proxies
# a = Proxies()
# a.verify_proxies()
# print (a.proxies)
# proxie = a.proxies
# with open('proxies.txt', 'w') as f:
#     for proxy in proxie:
#          f.write(proxy+'\n')

#爬取全国的空气污染数据
# execute('scrapy crawl nationalpm'.split())
#爬取世界的空气污染数据
# execute('scrapy crawl worldpm'.split())
#爬取国内的水体污染数据
# execute('scrapy crawl nationalwaterpollution'.split())
#爬取国内的固体废弃物数据(输入参数 kwlist——搜索的指标关键词,year——搜索哪一年的)
kw_list = ['垃圾', '废弃物', '回收', '塑料', '金属', '纸业']
kws = '#'.join(kw_list)
district_list = ['上海', '福建']
districts = '#'.join(district_list)
start_year = 2018
end_year = 2019
count = 100
execute(('scrapy crawl nationalsolidpollution -s CLOSESPIDER_ITEMCOUNT='+str(count)+' -a count='+str(count)+' -a kws='+kws+' -a districts='+districts+' -a start_year='+str(start_year)+' -a end_year='+str(end_year)).split())
#

