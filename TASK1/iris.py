#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing all the require libraries needed for the project

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


data = pd.read_csv("iris.csv") # importing and running data set


# In[5]:


data.shape # helps you to know the dimentions of the data set ,from here we start DATA INSPECTION


# In[6]:


data.info # helps to know about the info present in data set


# In[7]:


data.describe() # describes the mean and other values in data set


# In[8]:


data.nunique() # used to find usinque values in data set


# In[9]:


data['Species'].value_counts() # counts for many types of species are there in IRIS flower


# In[18]:


data.columns # used  to know the names of all columns in data set, FROM HERE WE START ANALYSING THE DATASET


# In[22]:


for i in data.columns:
    plt.scatter(data[str(i)], data['SepalLengthCm'])
    plt.xlabel(i)
    plt.ylabel("Sepal Length Cm")
    plt.show()


# In[23]:


sns.pairplot(data,hue = 'Species')


# In[24]:


data.corr() # now checking CORRELATION BETWEEN VARIBLES(NUMERIC)


# In[28]:


plt.figure(figsize =(10,10))
sns.heatmap(data.corr(),cmap ='Purples',annot = True) #PLOTTING CORRRELATION USING HEATMAP


# In[29]:


data.columns # OBSERVING THE DISTRIBUTION NATURE OF 4 COLUMES


# In[31]:


col = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
plt.figure(figsize=(35,5))
i=1
for e in col:
    plt.subplot(1,10,i)
    sns.distplot(data[e])
    i= i+1

plt.show()


# In[32]:


data.describe() # OBSERVING DISTURBUTION OF DATA ACROSS THE VARIOUS COLUMNS USIG HISTOGRAM

