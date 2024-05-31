from sklearn.datasets import fetch_california_housing
print(fetch_california_housing())

X=pd.DataFrame(fetch_california_housing()['data'],columns=fetch_california_housing()['feature_names'])
Y=pd.DataFrame(fetch_california_housing()['target'],columns=['target'])
from sklearn.ensemble import RandomForestRegressor

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2)



model3=RandomForestRegressor(n_estimators=50)
model3.fit(x_train,y_train.values.ravel())
model3.score(x_test,y_test)
np.array(y_test[:10])
from sklearn.metrics import mean_absolute_error
model3.score(x_test,y_test)
mean_absolute_error(preds,y_test)

from sklearn.ensemble import RandomForestClassifier
np.random.seed(42)
heart=pd.read_csv('heart_disease.csv')

X=heart.drop('target',axis=1)
Y=heart['target']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

model4=RandomForestClassifier(n_estimators=185)
model4.fit(x_train,y_train)
model4.score(x_train,y_train)
model4.predict_proba(x_train)
model4.score(x_test,y_test)

from sklearn.model_selection import cross_val_score
cross_val_score(model4,X,Y,cv=5)   

from sklearn.metrics import roc_curve

y_prob=model4.predict_proba(x_test)

y_positive_prob=y_prob[:,1]

fpr,tpr,thresholds=roc_curve(y_test,y_positive_prob)
fpr
