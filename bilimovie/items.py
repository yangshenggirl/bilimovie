# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilimovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #番剧排名
    num = scrapy.Field()
    #番剧名称
    name = scrapy.Field() 
    #番剧被喜爱数
    love = scrapy.Field()
    #番剧评论数
    comment = scrapy.Field()
    #番剧评分
    score = scrapy.Field() 
    pass
