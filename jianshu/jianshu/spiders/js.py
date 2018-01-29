# -*- coding: utf-8 -*-  思路：通过一个人id，找出他所有关注对象的信息，再取其中每位用户id，分别查询信息。亮点去重：dont_filter=False
#因为不能直接获取next_url链接，所以只能查处page_max，再从第2页开始往后查询，所以写了第二个next函数，不能回调 
import scrapy
from scrapy.http import Request
from jianshu.items import Jianshu
from math import ceil
class JsSpider(scrapy.Spider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    #start_urls = ['http://jianshu.com/']
    start_user_id = '1562c7f16a04'
    user_url = 'https://www.jianshu.com/u/{user_id}'
    following_url = 'https://www.jianshu.com/users/{uid}/following?page={num}'
    def start_requests(self):                                                   #写下初始Request 一方面为了检测爬虫能否正常运行
        yield Request(self.user_url.format(user_id=self.start_user_id),callback=self.parse_user) #初始查看开始id账户的基本情况
        yield Request(self.following_url.format(uid=self.start_user_id,num=1),callback=self.parse_follow) #从他开始分析关注对象

    def parse_user(self, response):
        item = Jianshu()
        item['name'] = response.xpath('//a[@class="name"]/text()').extract()[0] #等价于.extract_first()
        item['uid'] = response.xpath('//a[@class="name"]/@href').extract()[0][3:]
        item['following'] = response.xpath('//div[@class="meta-block"]/a/p/text()').extract()[0]
        item['follower'] = response.xpath('//div[@class="meta-block"]/a/p/text()').extract()[1]
        item['article'] = response.xpath('//div[@class="meta-block"]/a/p/text()').extract()[2]
        item['character_num'] = response.xpath('//div[@class="meta-block"]/p/text()').extract()[0]
        item['favo'] = response.xpath('//div[@class="meta-block"]/p/text()').extract()[1]
        item['introduce'] = response.xpath('//div[@class="js-intro"]').xpath('string(.)').extract()[0]
        yield item
        #print(item) #在这里取得每位用户的详情，取出item['uid']，作为下次爬取的uid,如此往复下去
        yield Request(self.following_url.format(uid=item['uid'],num=1),callback=self.parse_follow,dont_filter=False)
    def parse_follow(self, response):
        #print(response.text)
        uid = response.xpath('//a[@class="name"]/@href').extract()
        for u_id in uid[1:] : #第一个是作者，重复，跳过
            yield Request(self.user_url.format(user_id=u_id[3:]),callback=self.parse_user)
        following_num = response.xpath('//div[@class="meta-block"]/a/p/text()').extract()[0]
        page = ceil(float(following_num)/9) #不足一页的数据也在一页内
        #print('@'*24) 测试代码
        for i in range(2,page+1): #第一页已经爬过，故跳过从第二页开始
            yield Request(self.following_url.format(uid=self.start_user_id,num=i),callback=self.next)
        
    def next(self, response):
        uid = response.xpath('//a[@class="name"]/@href').extract()
        for u_id in uid[1:] : #第一个是作者，重复 
            #print("="*26) 测试这段代码运行情况
            yield Request(self.user_url.format(user_id=u_id[3:]),callback=self.parse_user)
   
        
        
        
            
