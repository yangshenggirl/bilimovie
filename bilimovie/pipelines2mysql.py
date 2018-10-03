# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BilimoviePipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect("localhost","root","123456","testa")
        
        cursor = db.cursor()
        sql = "INSERT INTO bilimovie(bnum,bname,blove,bcomment,bscore) VALUES({0},'{1}','{2}','{3}',{4})"\
        .format(int(item['num'][0]),item['name'][0],item['love'][0],item['comment'][0],int(item['score'][0]))
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()

        return item
