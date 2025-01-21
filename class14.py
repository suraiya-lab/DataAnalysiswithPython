import pandas as pd
data=pd.read_csv('social network ads.csv')
print(data)
x=data.iloc[:,1:5].values
y=data.iloc[:,-1:].values
print(x)
print(y)
from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()
x[:,0]=lb.fit_transform(x[:,0])
print(x)
lb2=LabelEncoder()
y=lb2.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.2,random_state=0)
print(x_train)
print(x_test)
from sklearn.preprocessing import MinMaxScaler
scale=MinMaxScaler()
print(MinMaxScaler)
x_train_scaled=scale.fit_transform(x_train)
print(x_train_scaled)