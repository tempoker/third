# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request as ur

class DbSpider(scrapy.Spider):
    name = 'renren'
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    allowed_domains = ['renren.com']
    '''
    start_urls = ['http://douban.com/']
     '''
    def start_requests(self):
        return [Request("http://www.renren.com/",callback=self.parse,meta={"cookiejar":1})]
    def parse(self, response):
        captcha=response.xpath("//img[@id='verifyPic_login']/@src").extract()
        #url = "http://www.renren.com/"
        if len(captcha) > 0:
            print("OMG@#@居然有！！验证码！！")
            localpath = "D:/Python36/Lib/site-packages/data/douban/captcha.png"
            ur.urlretrieve(captcha[0],filename=localpath)
            print("请查看本地验证码！图片！并输入！")
            captcha_value = input()
            data = {
                "email": "1578852802@qq.com", 
                "password": "Yanhu20131105",
                "icode":captcha_value,
                "origURL": "http://www.renren.com/495595321/profile", #跳转页面的变量名
            }
        else:
            print("NO 没有！！验证码！！")
            data ={
                "email":"1578852802@qq.com",
                "password":"Yanhu20131105",#以下是成功登录后跳转到页面，个人中心
                "origURL":"https://www.douban.com/people/72250246/",
            }
        print("登录中......")
        return[FormRequest.from_response(response,
                                             meta={"cookiejar":response.meta["cookiejar"]},
                                             headers = self.header,
                                             formdata=data,
                                             callback=self.next,
                                             )]
    def next(self,response):
        print("此时登录成功！！爬取个人中心的数据！")
        title=response.xpath("/html/head/title/text()").extract()
        #note=response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        #print(note[0])

