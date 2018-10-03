# -*- coding: utf-8 -*-
import scrapy

from bilimovie.items import BilimovieItem

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['https://www.bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking/bangumi/13/0/7']

    def parse(self, response):
        #获取当前所有番剧电影采集标签
        movie_items = response.xpath("//li[@class = 'rank-item']")
        #使用for循环遍历番剧标签
        for item in movie_items:
            #创建一个空的番剧采集对象
            movie = BilimovieItem()
            #xpath解析
            movie["num"] = item.xpath("div[@class = 'num']/text()").extract()
            movie["name"] = item.xpath("div[@class = 'content']/div[@class = 'info']/a/text()").extract()
            movie["love"] = item.xpath("div[@class = 'content']/div[@class = 'info']/div[@class = 'detail']/span[@class = 'data-box'][1]/text()").extract()
            movie["comment"] = item.xpath("div[@class = 'content']/div[@class = 'info']/div[@class = 'detail']/span[@class = 'data-box'][2]/text()").extract()
            movie["score"] = item.xpath("div[@class = 'content']/div[@class = 'info']/div[@class = 'pts']/div/text()").extract()
            yield movie
        pass
