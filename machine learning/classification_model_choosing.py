import pandas as pd
heartdisease=pd.read_csv('heart_disease.csv')
heartdisease.size
X=heartdisease.drop('target',axis=1)
Y=heartdisease['target']
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import numpy as np
np.random.seed(42)

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

model1=LinearSVC()
model1.fit(x_train,y_train)  
model1.score(x_test,y_test)

from sklearn.ensemble import RandomForestClassifier

model2=RandomForestClassifier()

model2.fit(x_train,y_train)
model2.score(x_test,y_test)

