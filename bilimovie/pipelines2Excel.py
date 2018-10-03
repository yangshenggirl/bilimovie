# -*- coding:gbk -*-
import os
import json
import time
import codecs
import csv
from scrapy.exporters import CsvItemExporter

class EnrolldataPipeline(object):

    def open_spider(self, spider):
        self.file = open("E:\\enrolldata.csv", "wb")
        self.file.write(codecs.BOM_UTF8)
        self.exporter = CsvItemExporter(self.file,       
        fields_to_export=["num", "name","love","comment","score"])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
