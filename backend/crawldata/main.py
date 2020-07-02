#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import pandas as pd
import datetime

#爬取全国的空气污染数据
# execute('scrapy crawl nationalpm'.split())
#爬取世界的空气污染数据
execute('scrapy crawl worldpm'.split())
#爬取国内的水体污染数据
# execute('scrapy crawl nationalwaterpollution'.split())
#爬取国内的固体废弃物数据(输入参数 kwlist——搜索的指标关键词,year——搜索哪一年的)
# kwlist = ['垃圾','废弃物','回收','塑料','金属','纸业']
# kws = '#'.join(kwlist)
# year = str(2019)
# kws = '废弃物'
#execute(('scrapy crawl nationalsolidpollution -a kwlist='+kws+' -a year='+year).split())

