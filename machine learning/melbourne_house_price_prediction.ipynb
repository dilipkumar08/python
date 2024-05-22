import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier

mel_house=pd.read_csv('D:/python/project/kaggle/dataset/melb_data.csv')

def mae_dtr(x_train,x_test,y_train,y_test,leaf_count):
    model=DecisionTreeRegressor(random_state=1,max_leaf_nodes=leaf_count)
    model.fit(x_train,y_train)
    prediction=model.predict(x_test)
    return MAE(y_test,prediction)

def mae_rfr(x_train,x_test,y_train,y_test,leaf_count):
    model=RandomForestRegressor(random_state=1,max_leaf_nodes=leaf_count)
    model.fit(x_train,y_train)
    prediction=model.predict(x_test)
    return MAE(y_test,prediction)

def mae_rfc(x_train,x_test,y_train,y_test,leaf_count):
    model=RandomForestClassifier(random_state=1,max_leaf_nodes=leaf_count)
    model.fit(x_train,y_train)
    prediction=model.predict(x_test)
    return MAE(y_test,prediction)


mel_house.dropna(axis=0,inplace=True)
mel_house.columns


y=mel_house.Price
x=mel_house[['Rooms','Bathroom','YearBuilt','Lattitude','Longtitude','Landsize','Bedroom2','Car']]

x.describe()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=1)

for i in [10,20,30,50,100,200,500,600,800,1000]:
    print(f'Decision Tree Mean Absolute Error for {i} leaf nodes is {mae_dtr(x_train,x_test,y_train,y_test,i)}')

for i in [100,200,300,400,1000,2600,2700]:
    print(f'Random Forest Mean Absolute Error for {i} leaf nodes is {mae_rfr(x_train,x_test,y_train,y_test,i)}')

for i in [100,200,300,400,1000,2600]:
    print(f'Random Forest Mean Absolute Error for {i} leaf nodes is {mae_rfc(x_train,x_test,y_train,y_test,i)}')
