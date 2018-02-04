# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DdPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1",user='root',password='131105',
                               db='pic',port=3306,use_unicode=True,charset="utf8")
        cursor = conn.cursor()
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i][:-3]
            price = item["price"][i][1:]
            sql = "insert into ddang values(null,'"+str(title)+"','"+str(link)+"',\
                    '"+comment+"','"+price+"')"
            cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return item
