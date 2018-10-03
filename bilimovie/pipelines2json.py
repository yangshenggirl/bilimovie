# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
import time

class BilimoviePipeline(object):

    def __init__(self):
        self.sourceFolder = "output"

        #如果不存在
        if not os.path.exists(self.sourceFolder):
            os.mkdir(self.sourceFolder)

        pass 

    def process_item(self, item, spider):
        
        now = time.strftime("%Y%m%d",time.localtime())
        jsonFileName = "movie_" + now +".json"

        #os.sep:获取到系统的分隔符
        with open(self.sourceFolder + os.sep + jsonFileName,"a") as jsonfile:
            data = json.dumps(dict(item),ensure_ascii = False) + "\n"
            jsonfile.write(data)
            
        return item
