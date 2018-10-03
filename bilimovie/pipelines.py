# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BilimoviePipeline(object):
    def process_item(self, item, spider):
        print("番剧排名：{0}".format(item["num"][0]))
        print("番剧名称：{0}".format(item["name"][0]))
        print("番剧被喜爱数：{0}".format(item["love"][0]))
        print("番剧评论数：{0}".format(item["comment"][0]))
        print("番剧评分：{0}".format(item["score"][0]))
        return item
