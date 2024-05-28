csem=pd.read_csv('car-sales-extended-missing-data.csv')
csem.isna().sum()
csem.dropna(inplace=True,axis=0)
# mcs['Price']=mcs['Price'].str.replace('[$,]','',regex=True).astype(float)
x,y=csem.drop('Price',axis=1),csem['Price']
catg=['Colour','Make','Doors']
one_hot=ohe(sparse_output =False)
transformer=ct([('one_hot',one_hot,catg)],remainder='passthrough')
cs.info
X=transformer.fit_transform(x)
x=pd.DataFrame(X)
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2)
print(x)


model=rfr(n_estimators=45,random_state=1)
model.fit(x_train,y_train)
predict=model    
print(model.score(x_test,y_test)*100)
#---------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
csem_2=pd.read_csv('car-sales-extended-missing-data.csv')

X=csem_2.drop('Price',axis=1)
y=csem_2['Price']

cat_imputer=SimpleImputer(strategy='constant',fill_value='missing')
door_imputer=SimpleImputer(strategy='constant',fill_value=4)
num_imputer=SimpleImputer(strategy='mean')

cat_feature=['Make','Colour']
door_feature=['Doors']

num_feature=['Odometer (KM)']

imputer=ColumnTransformer([('cat_imputer',cat_imputer,cat_feature),('door_imputer',door_imputer,door_feature),('num_imputer',num_imputer,num_feature)],remainder='passthrough')

x=imputer.fit_transform(X)
x=pd.DataFrame(x,columns=['Make','Color','Door','Odometer (KM)'])

x.isna().sum()
x['Door']=x['Door'].astype(int)

catg=['Color','Make','Door']
one_hot=ohe(sparse_output=False)
transformer=ct([('one_hot',one_hot,catg)],remainder='passthrough')
X=transformer.fit_transform(x)
print(X)

x=pd.DataFrame(X)
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2)

model=rfr(n_estimators=45,random_state=1)
model.fit(x_train,y_train)
predict=model    
print(model.score(x_test,y_test)*100)
