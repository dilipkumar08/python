import sklearn.datasets
import pandas as pd
X=pd.DataFrame(sklearn.datasets.fetch_california_housing()['data'],columns=sklearn.datasets.fetch_california_housing()['feature_names'])

Y=pd.DataFrame(sklearn.datasets.fetch_california_housing()['target'],columns=sklearn.datasets.fetch_california_housing()['target_names'])
Y.rename(columns={'MedHouseVal':'Target'},inplace=True)
from sklearn.ensemble import RandomForestRegressor
Y
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import SGDRegressor,ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
model1=Ridge(random_state=1)
model1.fit(x_train,y_train)
model1.score(x_test,y_test)
model2=Lasso(random_state=1)
model2.fit(x_train,y_train)
model2.score(x_test,y_test)
model3=RandomForestRegressor(random_state=1)
model3.fit(x_train,y_train.values.ravel())
model3.score(x_test,y_test)
model4=SGDRegressor(random_state=1)
model4.fit(x_train,y_train.values.ravel())
model4.score(x_test,y_test.values.ravel())
model5=ElasticNet(random_state=1)
model5.fit(x_train,y_train.values.ravel())
model5.score(x_test,y_test)
from sklearn import svm
model6=svm.SVR()
model6.fit(x_train,y_train.values.ravel())
model6.score(x_test,y_test)
