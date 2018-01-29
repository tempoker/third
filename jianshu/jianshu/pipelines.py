# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings
from .items import Jianshu
class JianshuPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        doc = settings['MONGODB_DOCNAME']
        client = MongoClient(host,port)
        db = client[db_name]
        self.post = db[doc]
    def process_item(self, item, spider):
        if isinstance(item,Jianshu):
            try:
                user_info = dict(item)
                if user_info:
                    self.post.insert(user_info)
            except Exception :
                pass
        return item
