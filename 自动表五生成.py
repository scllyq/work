#!/usr/bin/env python
# coding: utf-8

# In[8]:


# -*- coding: utf-8 -*-
# coding: utf-8
import pandas as pd
import jieba
import os
import synonyms
import numpy as np


# In[9]:


def clearSen(comment):
    comment = comment.strip()
    comment = comment.replace('、', '')
    comment = comment.replace('，', '。')
    comment = comment.replace('《', '。')
    comment = comment.replace('》', '。')
    comment = comment.replace('～', '')
    comment = comment.replace('…', '')
    comment = comment.replace('\r', '')
    comment = comment.replace('\t', ' ')
    comment = comment.replace('\f', ' ')
    comment = comment.replace('/', '')
    comment = comment.replace('、', ' ')
    comment = comment.replace('/', '')
    comment = comment.replace('。', '')
    comment = comment.replace('（', '')
    comment = comment.replace('）', '')
    comment = comment.replace('_', '')
    comment = comment.replace('?', ' ')
    comment = comment.replace('？', ' ')
    comment = comment.replace('!', '')
    comment = comment.replace('➕', '')
    comment = comment.replace('：', '')
    return comment


# In[ ]:





# In[10]:


def stripword(seg):
   stop = open(r"C:\Users\galaxyeye\Desktop\chinsesstoptxt.txt","r",encoding="utf-8")
   stopwords = stop.read().split("\t")
   wordlist=[]
   wordlist2=[]
   seg_list = jieba.cut(seg, cut_all=False)
   for key in seg_list:
        key = clearSen(key)
        wordlist2=str("|".join(wordlist))
        if not(key.strip() in stopwords) and (len(key.strip()) > 1) :
            zidian=synonyms.nearby(key)
           
            wordlist=list(zidian[0])
            m = len (wordlist)
            for i in  range(0,m):
                if len(wordlist[i])==0 :
                 wordlist[i]=key
       


   stop.close()
   end=str("".join(wordlist2))
   return end


# In[11]:


def creat():
    data = pd.read_excel(r"C:\Users\galaxyeye\Desktop\jieba分词测试.xlsx",encoding="utf-8")
    hangshu=len(data)
    counter=0
    while counter < hangshu:
      text = data.语义.iloc[counter]        # 读取counter行，评论列单元格内容
      data.分词1.iloc[counter]= stripword(text)     # 对读取的text评论分词
      counter=counter+1   
    data.to_excel(r"C:\Users\galaxyeye\Desktop\jieba分词测试result.xlsx") 
    
    


# In[12]:


dataz = creat()


# In[ ]:





# In[364]:





# In[238]:





# In[239]:





# In[ ]:





# In[ ]:




