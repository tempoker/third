import time,requests,random,re
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool as ThreadPool
from pymongo import MongoClient
ua = UserAgent()
headers = {'User-Agent':ua.random}
'''
print('现在时间是:{0}'.format(time.ctime()))
password = 'fishc'
count = 4  #2018-01-17 21:19:23
while count :
     passwd = input('请输入密码：')
     if passwd == password:
          print('密码正确，进入至尊席位')
          break
     elif "*" in passwd :
          print('密码中不能有"*"号！您还有',count,'次机会！请输入：',end = " ")
          continue
     else :
          print('密码输入不对！您还有',count-1,'次机会！请输入：',end = ' ')
          count -= 1
'''
'''
def hanoi(n,x,y,z): #n个盘子，借助y从x移动到z
     if n == 1:
          print(x,'---->',z)
     else:
          hanoi(n-1,x,z,y)
          print(x,'---->',z)
          hanoi(n-1,y,x,z)
n = int(input('请输入汉诺塔的层数：'))
hanoi(n,'X','Y','Z')
'''
'''
def fac(n):
     if n == 1:
          return 1
     else :
          return n*fac(n-1)
num = int(input('请输入一个数字：'))
result = fac(num)
print('%d的阶乘是%d' % (num,result))
'''
'''
def fab(n):
     return fab(n-1)+fab(n-2) if n>2 else 1 

num = int(input('请输入一个数：'))
res = fab(num)
if res != -1:
     print('总共有%d对兔子诞生' % res)
'''
'''
import requests,random,time,urllib.request
url = 'http://whatismyip.org/'
#ip_list = input('请开始输入：').split(sep=';')
iplist = ['110.73.1.9:8123','115.46.96.48:8123','113.64.92.22:8080']
while True:
     ip = random.choice(iplist)
     proxy = urllib.request.ProxyHandler({'http':ip})
     opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
     opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
     urllib.request.install_opener(opener)
     try:
          print('正在尝试使用%s访问' % ip)
          response = urllib.request.urlopen(url).read().decode('utf-8','ignore')
          print(len(response))
     except Exception as e:
          print('访问出错：{0}'.format(e))
     else:
          print('访问成功......')
     if input('请问是否继续?(Y/N)') == 'N':
          break
'''
'''
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
from sklearn.cluster import KMeans
fname = r'D:\Python36\Lib\site-packages\data\prac\luqu.csv'
datafm = pda.read_csv(fname)
x = datafm.iloc[:,1:4].as_matrix() #转化为矩阵
kms = KMeans(n_clusters=4)#聚成4类
y = kms.fit_predict(x)
s = npy.arange(0,len(y))
pyl.plot(s,y,'go')
pyl.show()
#pyl.subplot(3,3,5)
pyl.xlabel('num')
pyl.title('kind')
pyl.ylabel('time')
for i in range(len(y)):
     if(y[i]==0):
          pyl.plot(datafm.iloc[i:i+1,1].as_matrix(),datafm.iloc[i:i+1,0].as_matrix(),'om')
     if(y[i]==1):
          pyl.plot(datafm.iloc[i:i+1,1].as_matrix(),datafm.iloc[i:i+1,0].as_matrix(),'oy')
     if(y[i]==2):
          pyl.plot(datafm.iloc[i:i+1,1].as_matrix(),datafm.iloc[i:i+1,0].as_matrix(),'oc')
     if(y[i]==3):
          pyl.plot(datafm.iloc[i:i+1,1].as_matrix(),datafm.iloc[i:i+1,0].as_matrix(),'or')
pyl.show()
'''
'''
#使用人工神经网络实现手写体数字识别
#数据的读取与整理
#加载数据
from numpy import *
import operator
from os import listdir
import numpy as npy
import pandas as pda
import numpy
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
#建立一个函数取文件名前缀
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
#建立训练数据
def traindata():
    labels=[]
    trainfile=listdir("E:/traindata")
    num=len(trainfile)
    #长度1024（列），每一行存储一个文件
    #用一个数组存储所有训练数据，行：文件总数，列：1024
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisfname=trainfile[i]
        thislabel=seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("E:/traindata/"+thisfname)#"E:\traindata"
    return trainarr,labels
trainarr,labels=traindata()
xf=pda.DataFrame(trainarr)
yf=pda.DataFrame(labels)
tx2=xf.as_matrix().astype(int)
ty2=yf.as_matrix().astype(int)

#使用人工神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense,Activation
model=Sequential()
#输入层
model.add(Dense(10,input_dim=1024))
model.add(Activation("relu"))
#输出层
model.add(Dense(1,input_dim=1))
model.add(Activation("sigmoid"))
#模型的编译
model.compile(loss="mean_squared_error",optimizer="adam")
#训练
model.fit(tx2,ty2,nb_epoch=1,batch_size=5)
#预测分类
rst=model.predict_classes(tx2).reshape(len(tx2))
x=0
for i in range(0,len(tx2)):
    if(rst[i]!=ty2[i]):
        x+=1
print('正确率是：{0}'.format(1-x/len(tx2)))
'''
'''
import numpy as npy
x3=npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst=model.predict_classes(x3).reshape(len(tx2))
print('预测结果分别是：{0}'.format(rst))
'''
a = time.time()
client = MongoClient('localhost',27017)
db = client['test']
weather_cd_2017 = db['weather_cd_2017'] #变量名可以不同，尽量相同，等号左侧是可视化工具中表的名称
url_base = 'http://tianqi.2345.com/t/wea_history/js/20170{m}/56294_20170{n}.js'
url_second = 'http://tianqi.2345.com/t/wea_history/js/2017{m}/56294_2017{n}.js'
#url = 'http://tianqi.2345.com/t/wea_history/js/201712/56294_201712.js'
urls =[url_base.format(m=i,n=i) for i in range(1,10)]#.extend()
url2 = [url_second.format(m=i,n=i)for i in range(10,13)]
urls.extend(url2)
def get_info(url):
    try:
        data = requests.get(url,headers=headers).text 
        patime = r"ymd:'(.*?)'"
        time = re.compile(patime).findall(data)
        pabtemp = r"bWendu:'(.*?)'"
        btemp = re.compile(pabtemp).findall(data)
        paytemp = r"yWendu:'(.*?)'"
        ytemp = re.compile(paytemp).findall(data)
        pat_weather=r"tianqi:'(.*?)'"
        weather = re.compile(pat_weather).findall(data)
        pat_pollution = r"aqi:'(.*?)'"
        aqi = re.compile(pat_pollution).findall(data)
        pat_aqinfo =r"aqiInfo:'(.*?)'"
        aqinfo = re.compile(pat_aqinfo).findall(data)
        for i in range(len(time)):
            weather_info = {'time':time[i],'btemp':btemp[i],'ytemp':ytemp[i],'weather':weather[i],'aqi':aqi[i],'aqi_info':aqinfo[i],}
            #print(weather_info)
            db.weather_cd_2017.insert(weather_info)
    except Exception as e :
        print('一不意外：{info}'.format(info=e))
pool = ThreadPool(12)
pool.map(get_info,urls)
pool.close()
pool.join()
print('天气爬取程序运行了{t}s'.format(t=time.time()-a))
    
    
    
    
    
    
    

