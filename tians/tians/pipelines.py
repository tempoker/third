# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings
from .items import TiansItem

class TiansPipeline(object):
    def __init__(self):
        #self.fh=open("D:/Python36/Lib/site-packages/data/tians/tians.txt",'a')
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        doc = settings['MONGODB_DOCNAME']
        client = MongoClient(host=host,port=port)
        db = client[db_name] #库名
        self.post = db[doc] #表名
    def process_item(self, item, spider):
        '''先判断item类型，再存入相应数据库'''
        if isinstance(item,TiansItem):
            try:
                book_info = dict(item)
                if book_info:
                    self.post.insert(book_info)
            except Exception :
                pass
            #self.fh.write(str(item["title"][i])+"\n"+str(item["link"][i])+"\n"+str(item["stu"][i])+"\n--------\n")
        return item
    def close_spider(self):
        pass
        #self.fh.close()
'''
   for i in range(len(item['stu'])):
            print(item["title"][i])
            print(item["link"][i])
            print(item["stu"][i])
            print("---------------")
'''
