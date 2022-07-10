import pandas as pd
data=pd.read_csv("C:/Users/dilip/OneDrive/Documents/sample datasets/Test-Set.csv")
data.head()
#
data.set_index('ProductID',drop=True,inplace=True)
data.head()
#
data.loc['FDW58']
data.reset_index(inplace=True)
#
data.loc[2:8]
data.iloc[2:5]
#
data[data.FatContent=="Regular"]
data.loc[(data.OutletSize=='Small') & (data.ProductType=='Dairy')]
#
data[data.FatContent.isin(['Low Fat','Regular'])]
#
column=['ProductID','Weight']
data[data.ProductType=='Dairy'][column]
#
data.loc[data.ProductType=='Dairy',column]
#
data.dtypes
data.select_dtypes('object')
#
data.isna().sum()
data.Weight=data.Weight.fillna(data.Weight.mean())
#
data.Weight.isna().sum() #data.loc[(data.weight.isna()==True),'Weight']= data.Weight.mean()
data.loc[data.OutletSize.isna()==True]
#
data.OutletSize.mode()
#
data.OutletSize.value_counts()
#
data.loc[(data.OutletSize.isna()==True),'OutletSize']='Medium'
data.OutletSize.isna().sum()
#
data.FatContent.value_counts()
#
mapping={'Low Fat':'Low Fat','LF':'Low Fat','low fat':'Low Fat','Regular':'Regular','reg':'Regular'}
data.FatConte nt=data.FatContent.map(mapping)
data.FatContent.value_counts()
#
#converting to dollars
data.MRP.apply(lambda x:x/74)
data['MRP USD']=data.MRP.apply(lambda x:x/74)
