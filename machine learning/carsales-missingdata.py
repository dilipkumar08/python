%matplotlib inline
import pandas as pd
import numpy as np
import sklearn
import matplotlib as plt
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.preprocessing import OneHotEncoder as ohe
from sklearn.compose import ColumnTransformer as ct

csem=pd.read_csv('car-sales-extended-missing-data.csv')
mcs.isna().sum()
mcs.dropna(inplace=True)
mcs['Price']=mcs['Price'].str.replace('[$,]','',regex=True).astype(float)
x,y=mcs.drop('Price',axis=1),mcs['Price']
catg=['Colour','Make','Doors']
one_hot=ohe()
transformer=ct([('one_hot',one_hot,catg)],remainder='passthrough')
cs.info
X=transformer.fit_transform(x)
x=pd.DataFrame(X)
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2)
print(x_train,x_test,y_train,y_test)
model=rfr(n_estimators=45,random_state=1)
model.fit(x_train,y_train)
predict=model    
print(model.score(x_test,y_test)*100)
