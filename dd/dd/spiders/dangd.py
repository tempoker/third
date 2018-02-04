# -*- coding: utf-8 -*-
import scrapy
from dd.items import DdItem
from scrapy.http import Request
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher #分发器
from scrapy import signals #信号

class DangdSpider(scrapy.Spider):
    name = 'dangd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg3-cp01.54.06.00.00.00.html']

    def __init__(self):
        self.browser = webdriver.Firefox()
        super(DangdSpider,self).__init__()
        dispatcher.connect(self.spider_closed,signals.spider_closed)
        
    def spider_closed(self,spider):
        #当爬虫退出的时候，浏览器也退出。
        print("spider:{0} closed......".format(spider.name))
        self.browser.quit()
        
    def parse(self, response):
        item = DdItem()
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comment"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        item['price']=response.xpath("//span[@class='search_now_price']/text()").extract()
        yield item
        for i in range(4,6):
            url = "http://category.dangdang.com/pg"+str(i)+"-cp01.54.06.00.00.00.html"
            yield Request(url,callback=self.parse,dont_filter=False)






