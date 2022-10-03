#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")
df=pd.read_csv("C:\\Users\\ankit\\Documents\\Project Files\\laptop price data.csv")
df["Manufacturer"]=df["Manufacturer"].replace(to_replace={"HP":0,"Lenovo":1,"ASUS":2,"Dell":3})
X=df[["Manufacturer","IntelCore","Ram","HDD","SSD"]]
y=df["Price"]
X=X.astype("int")
y=y.astype("int")
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=40)
regre=LinearRegression()
regre.fit(X_train,y_train)

pickle_out= open("model.pkl", "wb")
pickle.dump(regre,pickle_out )
pickle_out.close()

