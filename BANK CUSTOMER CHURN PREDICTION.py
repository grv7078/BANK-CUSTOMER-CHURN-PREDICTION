#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('Churn_Modelling.csv')


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.shape


# In[6]:


print('Number of Rows:', data.shape[0])
print('Number of Columns:', data.shape[1])


# In[7]:


data.info()


# In[8]:


data.isnull().sum() #check null valves


# In[9]:


data.describe() # get overall statistics about the dataset


# In[10]:


data.columns # dropping irrelevent features


# In[11]:


data=data.drop(['RowNumber','CustomerId','Surname'],axis=1)
data


# In[12]:


data['Geography'].unique() #encoding categorical data


# In[13]:


dta=pd.get_dummies(data,drop_first=True)


# In[14]:


data.head()


# In[15]:


data['Exited'].value_counts()


# In[16]:


import seaborn as sns


# In[17]:


sns.countplot(x='Exited',data=data)


# In[18]:


x=data.drop('Exited',axis=1)
y=data['Exited']


# In[19]:


y


# In[28]:


x_train


# In[29]:


y_train


# In[34]:


x_test


# In[ ]:




