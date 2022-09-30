#!/usr/bin/env python
# coding: utf-8

# # Horse Survival Prediction                         

# #### @Author : Saurabh Kumar 

# In[1]:


pwd


# In[2]:


path="E:\\DataScience\\MachineLearning\\Horse Survival Prediction"


# In[3]:


import os
os.listdir(path)


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import plotly.express as px
from wordcloud import WordCloud
from scipy import signal
import scipy
#to supress warning
import warnings
warnings.filterwarnings('ignore')


#to make shell more intractive
from IPython.display import display

# setting up the chart size and background
plt.rcParams['figure.figsize'] = (16, 8)
plt.style.use('fivethirtyeight')


# In[5]:


df = pd.read_csv(path+"\\horse.csv")


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.columns


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


df.corr().style.background_gradient(cmap = 'Greys')


# In[12]:


df.describe().T.style.background_gradient(cmap = 'Greys')


# In[13]:


df.duplicated().sum()


# In[14]:


df.isnull().sum()


# In[15]:


sns.heatmap(df.isnull())


# In[16]:


#percentage of null each columns
for col in df.columns:
    print('{} :NUll %  :     {}'.format(col,df[col].isnull().sum()/df[col].count()))


# ### Remove Null values

# In[17]:


# No. of Animal Hospital Avaliable in the city from where data is taken...
df.hospital_number.nunique()


# In[18]:


#Lets drop hospital_number since it not relivant 
df.drop(['hospital_number'],axis=1,inplace=True)


# In[19]:


#center of tendency
sns.distplot(df['rectal_temp'])


# In[20]:


#Central tendency of rectal_temp
df['rectal_temp'].describe()


# In[21]:


#Since mean is Central of tendency so replace NAN with mean 
df['rectal_temp'] = df['rectal_temp'].fillna(df['rectal_temp'].mean())


# In[22]:


sns.distplot(df['pulse'])


# In[23]:


df['pulse'].describe()


# In[24]:


# Filling null values with mean of the numerical column
df['pulse'] = df['pulse'].fillna(df['pulse'].mean())
df['respiratory_rate'] = df['respiratory_rate'].fillna(df['respiratory_rate'].mean())
df['packed_cell_volume'] = df['packed_cell_volume'].fillna(df['packed_cell_volume'].mean())
df['total_protein'] = df['total_protein'].fillna(df['total_protein'].mean())


# In[25]:


#drop
df.drop(['nasogastric_tube'],axis=1,inplace=True)
df.drop(['nasogastric_reflux'],axis=1,inplace=True)
df.drop(['nasogastric_reflux_ph'],axis=1,inplace=True)
df.drop(['rectal_exam_feces'],axis=1,inplace=True)
df.drop(['abdomen'],axis=1,inplace=True)
df.drop(['abdomo_protein'],axis=1,inplace=True)
df.drop(['abdomo_appearance'],axis=1,inplace=True)


# In[26]:


df['temp_of_extremities'].value_counts()


# In[27]:


df['peripheral_pulse'].value_counts()


# In[28]:


df['mucous_membrane'].value_counts()


# In[29]:


df['capillary_refill_time'].value_counts()


# In[30]:


df['pain'].value_counts()


# In[31]:


df['peristalsis'].value_counts()


# In[32]:


df['abdominal_distention'].value_counts()


# In[33]:


#fillna 
df['temp_of_extremities'] = df['temp_of_extremities'].fillna('cold')
df['peripheral_pulse'] = df['peripheral_pulse'].fillna('increased')
df['mucous_membrane'] = df['mucous_membrane'].fillna('dark_cyanotic')
df['capillary_refill_time'] = df['capillary_refill_time'].fillna('3')
df['pain'] = df['pain'].fillna('alert')
df['peristalsis'] = df['peristalsis'].fillna('normal')
df['abdominal_distention'] = df['abdominal_distention'].fillna('severe')


# In[34]:


df.isnull().sum()


# In[35]:


## traget colums 'Outcome'
df['outcome'].value_counts()


# In[36]:


# Euthanized is also a died state 
df['outcome'].replace(to_replace='euthanized',value='died',inplace=True)


# In[37]:


#Now it correct
df['outcome'].value_counts()


# In[38]:


#--
df.head(10)


# ## EDA ~Plots

# In[39]:


plt.figure(figsize = (12,6))
sns.catplot(x='surgery',data=df,hue='outcome',col='age',kind='count')
plt.show()


# In[41]:


sns.catplot(x='mucous_membrane',data=df,hue='outcome',kind='count',col='surgery')
plt.xticks(rotation=90)
plt.show()


# In[42]:


sns.catplot(x='pain',data=df,hue='outcome',kind='count',col='surgery')
plt.xticks(rotation=90)
plt.show()


# In[43]:


sns.catplot(x='temp_of_extremities',data=df,hue='outcome',kind='count',col='age')


# In[44]:


sns.catplot(x='peripheral_pulse',data=df,hue='outcome',kind='count',col='age')
plt.show()


# In[45]:


sns.catplot(x='peripheral_pulse',data=df,hue='outcome',kind='count',col='surgery')
plt.show()


# In[46]:


sns.catplot(x='abdominal_distention',data=df,hue='age',col='outcome',kind='count')


# In[47]:


plt.figure(figsize=(20,16))
sns.catplot(x="pulse", y="age",hue="outcome", row="pain",data=df,
                orient="h", height=4, aspect=4, palette="Set3",
                kind="violin", dodge=True, cut=0, bw=.2)


# In[48]:


def mix_plot_cat(x,y):
    # 1st plot
    fig, axes = plt.subplots(3, 2, figsize=(25, 20))
    sns.set_style("darkgrid");
    sns.violinplot(ax=axes[0, 0],data=df, x=x, y=y, hue="outcome")
    # 2nd plot
    sns.barplot(ax=axes[0, 1],data=df, x=x, y=y, hue="outcome") 
    # 3rd plot
    sns.boxenplot(ax=axes[1, 0],data=df, x=x, y=y, hue="outcome") 
    # 4th plot
    sns.stripplot(ax=axes[1, 1],data=df, x=x, y=y, hue="outcome") 
    # 5th
    sns.pointplot(ax=axes[2, 0],data=df, x=x, y=y, hue="outcome")  
    # 6th
    sns.boxplot(ax=axes[2, 1],data=df, x=x, y=y, hue="outcome") 


# #### Pulse Vs Age

# In[49]:


mix_plot_cat('pulse','age')


# #### Respiratory_rate Vs Age

# In[50]:


mix_plot_cat('respiratory_rate','age')


# #### Total_protein VS Age

# In[51]:


mix_plot_cat('total_protein','age')


# #### Pluse vs Pain

# In[52]:


mix_plot_cat('pulse','pain')


# In[53]:


plt.figure(figsize=(20,16))
sns.catplot(x="respiratory_rate", y="surgery",hue="outcome", row="age",data=df,
                orient="h", height=4, aspect=4, palette="Set3",
                kind="violin", dodge=True, cut=0, bw=.2)


# In[54]:


#Pair plot
sns.pairplot(df,hue='outcome')


# ## Numerical Columns

# In[55]:


num_lst=[]
for col in df.columns:
    if df[col].dtypes != 'object':
        num_lst.append(col)


# In[56]:


num_lst


# In[57]:


df_num = df[['rectal_temp','pulse','respiratory_rate',
             'packed_cell_volume','total_protein','lesion_1','lesion_2','lesion_3']]


# In[58]:


df_num.head()


# In[59]:


def mix_plot(feature):
    plt.figure(figsize=(16, 6))
    plt.subplot(1, 3, 1)
    feature.plot(kind = 'hist')
    plt.title(f'{feature.name} histogram plot')
    #mean = feature.describe().mean()
    plt.subplot(1, 3, 2)
    mu, sigma = scipy.stats.norm.fit(feature)
    sns.distplot(feature) 
    #plt.legend({'--': mu, 'sigma': sigma})
    plt.axvline(mu, linestyle = '--', color = 'green', )
    plt.axvline(sigma, linestyle = '--', color = 'red')
    plt.title(f'{feature.name} distribution plot')
    plt.subplot(1, 3, 3)
    sns.boxplot(feature)
    plt.title(f'{feature.name} box plot')
    plt.show()


# In[60]:


for i in df_num.columns:
    mix_plot(df_num[i])


# In[61]:


sns.heatmap(df.corr(),cbar=True,square=True,fmt='.2f',annot=True,annot_kws={'size':10},cmap='Pastel2')
sns.set_style('darkgrid')


# ### Categorical Colums

# In[62]:


cat_lst=[]
for col in df.columns:
    if df[col].dtypes == 'object':
        cat_lst.append(col)
cat_lst.remove('outcome')
cat_lst


# In[63]:


#convert all categorical variables to numeric
df[cat_lst] = df[cat_lst].apply(lambda x: pd.factorize(x)[0])


# In[64]:


df['outcome'].value_counts()


# In[65]:


# target value
df['outcome'] = df['outcome'].map({'lived':0,'died':1}).astype(int)


# In[66]:


df['outcome'].value_counts()


# In[67]:


# Independent variable and dependent variable
#Independent 
X = df.loc[:, df.columns != 'outcome']
#dependent
y = df[['outcome']]


# In[68]:


#split data for training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[69]:


print("Shape X_train :",X_train.shape)
print("Shape y_train :",y_train.shape)
print("Shape X_test  :",X_test.shape)
print("Shape y_test  :",y_test.shape)


# In[70]:


from sklearn.preprocessing import StandardScaler
Scaler =StandardScaler()
X =Scaler.fit_transform(X)


# In[71]:


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
import xgboost 
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold ,StratifiedKFold
from sklearn import metrics
from sklearn.pipeline import Pipeline


# In[72]:


pipe_LR=Pipeline([('scaler1',StandardScaler()),
                 ('LR',LogisticRegression(random_state=2))])
pipe_Ada=Pipeline([('scaler2',StandardScaler()),
                    ('Ada',AdaBoostClassifier(learning_rate=0.1,random_state=2))])
pipe_DT=Pipeline([('scaler3',StandardScaler()),
                  ('DTR',DecisionTreeClassifier())])
pipe_RF=Pipeline([('scaler4',StandardScaler()),
                  ('RFR',RandomForestClassifier())])
pipe_Knn=Pipeline([('scaler5',StandardScaler()),
                   ('Knn',KNeighborsClassifier())])
pipe_Xgb =Pipeline([('scaler5',StandardScaler()),
                   ('Xgboost',XGBClassifier(learning_rate=0.1,random_state=5))])


# In[73]:


pipeline=[pipe_LR,pipe_Ada,pipe_DT,pipe_RF,pipe_Knn,pipe_Xgb]
pipe_dict ={0:'Lr',1:'Ada',2:'DT',3:'RF',4:'Knn',5:'Xgb'}


# In[74]:


pipe_dict={0:'LogisticRegression',1:'AdaBoostClassifier',2:'DecisionTreeClassifier',3:'RandomForestClassifier'
           ,4:'KNeighborsClassifier',5:'XGBClassifier'}


# In[75]:


for pipe in pipeline:
  pipe.fit(X_train,y_train)


# In[76]:


for i,models in enumerate(pipeline):
  print("{} Accuracy : {}".format(pipe_dict[i],models.score(X_test,y_test)))


# In[77]:


model_knn =KNeighborsClassifier()
model_knn.fit(X_train,y_train)
y_pred =model_knn.predict(X_test)


# In[78]:


print('Accuracy_Score :',metrics.accuracy_score(y_test,y_pred))
print('Classification_report:\n',metrics.classification_report(y_test,y_pred))
print('Confusion_mat:\n',metrics.confusion_matrix(y_test,y_pred))


# In[79]:


error_rate=[]
for i in range(1,30):
  model_knn =KNeighborsClassifier(n_neighbors=i)
  model_knn.fit(X_train,y_train)
  pred_i =model_knn.predict(X_test)
  error_rate.append(np.mean(pred_i) != np.mean(y_test))


# In[80]:


plt.figure(figsize=(10,5))
plt.plot(range(1,30),error_rate,color='blue', linestyle='dashed', marker='o',markerfacecolor='red', markersize=8)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# In[ ]:


----------------------XXXXXXXXXXXXXXXXXXXXXX-------------------


# In[ ]:




