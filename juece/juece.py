#决策树算法 2017-12-10 18:14:23 
import pandas as pda
import numpy as npy
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

fname = "D:\\Python36\\Lib\\site-packages\\data\\start_26\\algorithm\\lesson.csv"
datafm = pda.read_csv(fname,encoding='gbk')#中文内容用gbk编码
x = datafm.iloc[:,1:5].as_matrix()
y = datafm.iloc[:,5].as_matrix()
#x=[[int(1) if(x[i][j] in ['高','是','多']) else -1 for j in range(0,len(x[0]))  ]for i in range(0,len(x))]
for i in range(0,len(x)): #行数
     for j in range(0,len(x[i])):
          if(x[i][j] in ['高','多','是']):#取出x中第i行第j列的数据
               x[i][j]=int(1)
          else:
               x[i][j] = -1
for i in range(0,len(y)):
     if (y[i]=='高') :
          y[i] = int(1)
     else:
          y[i] = -1
#易错点：数据格式不改变直接dtc练习
#正确做法:转化为数据框，在转化为数组等指定形式
xf = pda.DataFrame(x)
yf = pda.DataFrame(y)
x2 = xf.as_matrix().astype(int)#转化为int类型的数组格式
y2 = yf.as_matrix().astype(int)
dtc = DTC(criterion='entropy') #criterion :规范  entropy：信息熵
dtc.fit(x2,y2) #接下来 数据可视化决策树
x3 = npy.array([[1,-1,-1,1],[1,-1,-1,1],[-1,-1,-1,1]])# 直接预测
rst = dtc.predict(x3)#x3的维度和x2必须一致
print(rst)
with open('./dtc2.dot','w') as fh:          #feature_names 依次表示特征的名称
     export_graphviz(dtc,feature_names=['combat','lessons','promotion','datum'],out_file=fh)
#接下来目录下生成dtc2.dot文件，用graphviz 这款软件转换格式如PNG
#首先下载安装，同时把该软件的bin目录添加到环境变量
#再用powercmd 配合Tab快捷键迅速切换到dtc2.dot所在目录
#最后 >  dot -Tpng dtc2.dot -o dtc2.png  形式为 dot -T格式 文件 -o 新文件名.格式
#-Tpng表示转换为png格式，也可以是-Tpdf dtc2.dot是待转换文件 -o表示输出 新文件名.格式
#看png格式决策树方法：往左表示负能量，往右是正能量  图中entropy表示信息增益，信息有价值程度，说明实战最有价值。    









