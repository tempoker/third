#-*- conding:utf-8 -*-
#2018-02-02 11:04:54

import time,random,requests
from lxml import etree
from fake_useragent import UserAgent
import urllib.request as ur
from pymongo import MongoClient
from multiprocessing.dummy import Pool as ThreadPool

client = MongoClient('localhost',27017)
db = client['test']
ip_list = db['ip_list']
ua = UserAgent()
headers = {'User-Agent':ua.random}
def get_ip(url):
     try:
          data = requests.get(url,headers=headers).text
          content = etree.HTML(data)
          ip = content.xpath('//*[@class="odd"]/td[2]/text()')
          port = content.xpath('//*[@class="odd"]/td[3]/text()')
          with open('ip_list.txt','a+') as fh:
               for i in range(len(ip)):
                    ip_port = str(ip[i])+':'+str(port[i])
                    fh.write(ip_port+'\n')
                    print('第{num}条ip记录成功'.format(num=i+1))
     except Exception as e:
          print('一不意外：{error}'.format(error=e))
def verif_ip(ip_port):
     proxy = {'http':'%s:%s' %(ip_port.split(':')[0],ip_port.split(':')[1][:-2])}
     print('正在测试的ip是:{ip}'.format(ip=proxy))
     support = ur.ProxyHandler(proxy)
     opener = ur.build_opener(support,ur.HTTPHandler)
     ur.install_opener(opener)
     test_url = 'https://www.baidu.com/'
     resp = requests.get(test_url,headers=headers)
     time.sleep(random.random()*10)
     try:
          if resp.status_code == 200:
               res = resp.text
               print('字节数为:{n}'.format(n=len(res)))
               db.ip_list.insert(proxy)
               with open('ip_userful.txt','a+') as fh:
                    fh.write(ip_port+'\n')
          else :
               print('there is some problem!')
     except Exception as e:
          print('出了问题：'+str(e))
def main():
     url_base = 'http://www.xicidaili.com/nn/{page}'
     urls = [url_base.format(page=i+1) for i in range(12)]
     pool = ThreadPool(12)
     pool.map(get_ip,urls)
     pool.close()
     pool.join()
     time.sleep(random.random()*10)
     with open ('ip_list.txt','r') as fh:
          try:
               ip_ports = fh.readlines()
               pool = ThreadPool(12)
               pool.map(verif_ip,ip_ports)
               pool.close()
               pool.join()
               #for ip_port in ip_ports:
                #    verif_ip(ip_port)
          except Exception :
               pass
if __name__ == '__main__':
     main()
                    
     
