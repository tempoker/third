# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class Jianshu(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    uid = Field()
    following = Field()
    follower = Field()
    article = Field()
    character_num = Field()
    introduce = Field()
    favo = Field()
