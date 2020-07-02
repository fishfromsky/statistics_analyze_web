# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    # pass
class NationalPMItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    check_area = scrapy.Field()
    AQI = scrapy.Field()
    air_quality = scrapy.Field()
    pollutant = scrapy.Field()
    pm2_5 = scrapy.Field()
    pm10 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o3_1h = scrapy.Field()
    o3_8h = scrapy.Field()
    so2 = scrapy.Field()
    update_time = scrapy.Field()

class WorldPMItem(scrapy.Item):
    # define the fields for your item here like:
    update_time = scrapy.Field()
    check_area = scrapy.Field()
    AQI = scrapy.Field()
    air_quality = scrapy.Field()
    pollutant = scrapy.Field()
    pm2_5 = scrapy.Field()
    pm10 = scrapy.Field()
    o3 = scrapy.Field()
    no2 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    temperature = scrapy.Field()
    air_pressure = scrapy.Field()
    humidity = scrapy.Field()
    wind = scrapy.Field()

class NationalWaterPollutionItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    check_time = scrapy.Field()
    PH = scrapy.Field()
    DO = scrapy.Field()
    AN = scrapy.Field()
    Mn = scrapy.Field()
    OC = scrapy.Field()
    sort = scrapy.Field()
    attr = scrapy.Field()
    situation = scrapy.Field()

class NationalSolidPollutionItem(scrapy.Item):
    # define the fields for your item here like:
    year = scrapy.Field()
    area = scrapy.Field()
    index = scrapy.Field()
    value = scrapy.Field()
    unit = scrapy.Field()
    source = scrapy.Field()
