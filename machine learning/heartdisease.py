%matplotlib inline
import pandas as pd
import numpy as np
import sklearn
import matplotlib as plt
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
x=hd.drop('target',axis=1)
y=hd['target']
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2)
model=rfc(n_estimators=110,random_state=0)
model.fit(x_train,y_train)
prediction=model.predict(x_test)
model.score(x_train,y_train)
model.score(x_test,y_test)  
print(classification_report(y_test,prediction))
confusion_matrix(y_test,prediction)
accuracy_score(y_test,prediction)
#best estimator finder
# for i in range(10,200,10):
#      model=rfc(n_estimators=i,random_state=1)
#     model.fit(x_train,y_train)
#     print(i, model.score(x_test,y_test)*100)#110 estimator
import pickle
pickle.dump(model,open('randomforestmodel1.pkl','wb'))
load_model=pickle.load(open('randomforestmodel1.pkl','rb'))
load_model.score(x_test,y_test)
