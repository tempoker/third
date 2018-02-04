from gensim import corpora,models,similarities
import jieba
from collections import defaultdict
#2017-12-10 01:28:09 过去半个月，再次复习文本相似度
doc1="D:\\Python36\\Lib\\site-packages\\data\\start_26\\博客小说\\tcby.txt"
doc2="D:\\Python36\\Lib\\site-packages\\data\\start_26\\博客小说\\ydtj.txt"
d1=open(doc1,encoding='utf-8').read()
d2=open(doc2,encoding='utf-8').read()
data1 = jieba.cut(d1)#精准分词，无叠加
data2 = jieba.cut(d2)
#“词语1 词语2 词语3.。。词语n”
data11=''
for i in data1:
     data11 += i+" "
data21=''
for i in data2:
     data21 += i+" "
documents = [data11,data21]
texts=[[word for word in document.split()]for document in documents]
frequency = defaultdict(int)#初始化一个字典
for text in texts:
     for token in text:
          frequency[token]+=1 #统计每个分词后的词汇频数
'''
texts = [[word for word in text if frequenfy[token]>3]
          for text in texts] #清洗频数低于3的词汇
'''
dictionary = corpora.Dictionary(texts)#清洗过后的数据
dictionary.save('./fenci.txt')#保存起来，以后用
#第三个文本跟前面两本的相似度
doc3="D:\\Python36\\Lib\\site-packages\\data\\start_26\\博客小说\\hdxh.txt"
d3 = open(doc3,encoding='utf-8').read()
data3=jieba.cut(d3)
data31 = ''
for i in data3:
     data31 += i+" "
new_doc = data31 #接下来变为稀疏向量
new_vec = dictionary.doc2bow(new_doc.split())
#进一步处理，得到新的语料库
corpus=[dictionary.doc2bow(text) for text in texts]#语料库
corpora.MmCorpus.serialize('./wenben2.mm',corpus)#将corpus参数保存在文本
tfidf = models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())#字典的键 关键字
index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim = index[tfidf[new_vec]]
print(sim)













