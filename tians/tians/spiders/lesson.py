# -*- coding: utf-8 -*-
import scrapy
from tians.items import TiansItem
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
class LessonSpider(RedisSpider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    redis_key = 'hellobi:start_url'
    #start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        item = TiansItem()
        item["title"]=response.xpath("//ol[@class='breadcrumb']/li[@class='active']/text()").extract_first("")
        #print(item["title"])
        item["link"]=response.xpath("//ul[@class='nav nav-tabs']/li[@class='active']/a/@href").extract_first("")
        item["stu"]=response.xpath("//span[@class='course-view']/text()").re('\d+')[0]
        yield item
        for i in range(2,245):
            url = 'https://edu.hellobi.com/course/'+str(i)
            yield Request(url,callback=self.parse)
