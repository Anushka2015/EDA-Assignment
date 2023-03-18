#!/usr/bin/env python
# coding: utf-8

# # EDA - Exploratory Data Analysis: Using Python Functions Phase 1
# 

# # Prediction task is to determine whether a person makes over 50K a year.

# In[74]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
# Display all the colunm of the dataframes
pd.pandas.set_option("display.max_columns",None)


# # Load the Data

# In[75]:


dfa1=pd.read_csv("adult.csv")


# # Make a copy of original data

# In[76]:


dfa1_copy=dfa1.copy()


# # characteristics of the dataset or Basic information about data (Profile of Data)

# In[77]:


dfa1_copy


# In[78]:


dfa1_copy.head()


# In[79]:


dfa1_copy.tail()


# In[80]:


dfa1_copy.sample()


# In[81]:


dfa1_copy.shape


# # 18-----# Dataset have 32560 Rows and 15 Columns

# In[82]:


dfa1_copy.info()


# # 19------# DataType of Data is int and Object(it may be categorical,text or integer variables)

# In[83]:


dfa1_copy.describe().T


# # find Duplicate values in Data

# In[84]:


dfa1_copy[dfa_copy.duplicated()]


# # Find the Null Values

# In[85]:


dfa1_copy.isnull().sum()


# In[86]:


features_with_null=[features for features in dfa1_copy.columns if dfa1_copy[features].isnull().sum()>=1]


# In[87]:


features_with_null


# # 29---------# No Any Null Values in Data

# # Unique values in the data column wise

# In[88]:


dfa1_copy.columns


# In[89]:


dfa1_copy['39'].unique()


# In[90]:


dfa1_copy[' State-gov'].unique()


# In[91]:


dfa1_copy[ '77516'].unique()


# # Check unique value in whole Dataset

# In[92]:


for col in dfa1_copy.columns:
        print(col,dfa1_copy[col].unique())


# # Cleaning of Dataset 

# # Replace unique Values

# In[93]:


dfa1_copy[' <=50K'].unique()


# In[94]:


dfa1_copy[' <=50K']=dfa1_copy[' <=50K'].replace("<=","")


# In[95]:


dfa1_copy[' <=50K']=dfa1_copy[' <=50K'].replace("K","000")


# In[96]:


dfa1_copy[' <=50K']=dfa1_copy[' <=50K'].replace(">","")


# In[97]:


dfa1_copy[' <=50K']


# In[98]:


dfa1_copy


# In[99]:


char_to_removes=[">","<="]
cols_to_clean=[' <=50K']
for item in char_to_removes:
    for col in cols_to_clean:
        dfa1_copy[col]=dfa1_copy[col].str.replace(item,"")


# In[100]:


dfa1_copy.head()


# In[101]:


char_to_removes=["K"]
cols_to_clean=[' <=50K']
for item in char_to_removes:
    for col in cols_to_clean:
        dfa1_copy [col]=dfa1_copy[col].str.replace(item,"000")


# In[102]:


dfa1_copy.head()


# In[103]:


dfa1_copy[' State-gov']=dfa1_copy[' State-gov'].str.replace(' ?',"")


# In[105]:


dfa1_copy[' Adm-clerical']=dfa1_copy[' Adm-clerical'].str.replace(' ?',"")


# In[106]:


dfa1_copy[' United-States']=dfa1_copy[' United-States'].str.replace(' ?',"")


# In[107]:


dfa1_copy.head()


# In[108]:


dfa1_copy.tail()


# # Make a file of clean dataset

# In[109]:


dfa1_copy.to_csv("data_adult_eda.csv",index=False)


# In[110]:


dfa1_clean=pd.read_csv("data_adult_eda.csv")


# In[ ]:




