#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import jieba
df = pd.read_csv("data.csv", encoding='utf-8')
df["content"] = df["content"].astype(str)
df.head()


# In[16]:


#df.shape


# In[17]:


def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))


# In[18]:


df["content_cutted"] = df.content.apply(chinese_word_cut)
print(df.content_cutted.head()) 


# In[19]:


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
n_features = 1000
tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df = 0.5,
                                min_df = 10)


# In[20]:


tf = tf_vectorizer.fit_transform(df.content_cutted)
from sklearn.decomposition import LatentDirichletAllocation


# In[ ]:





# In[21]:


n_components = 50  # 设定主题个数
lda = LatentDirichletAllocation(n_components=n_components, max_iter=50, learning_method='online', learning_offset=50.,
                                random_state=0)
result_topic = lda.fit(tf)
print(result_topic)


# In[8]:


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()
n_top_words = 20
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)


# In[9]:


import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()
pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)


# In[24]:


n_components = 25
lda = LatentDirichletAllocation(n_components=n_components, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
lda.fit(tf)
print_top_words(lda, tf_feature_names, n_top_words)
pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)


# In[ ]:





# In[ ]:




