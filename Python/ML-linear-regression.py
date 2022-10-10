import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from google.colab import files
uploaded=files.upload()
dataset = pd.read_csv('Salary_DataSet .csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
X
from sklearn.model_selection import train_test_split
X_train ,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
X_train.size
X_test
y_train
X_train
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)
y_prdict=reg.predict(X_test)
y_prdict=reg.predict([[6.5]])
y_prdict
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train, reg.predict(X_train),color='blue')
plt.title("Linear Regression Salary vs Experience")
plt.xlabel("Years of Employee")
plt.ylabel("Salaries of Employee")
plt.show()
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train, reg.predict(X_train),color='blue')
plt.title("Linear Regression Salary vs Experience")
plt.xlabel("Years of Employee")
plt.ylabel("Salaries of Employee")
plt.show()
