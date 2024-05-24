import pandas as pd
data=pd.read_csv('D:/python/project/kaggle/dataset/melb_data.csv')
price_mean=data.Price.mean()
def remean_price(row):

    row.Price=row.Price-price_mean
    return row
data.apply(remean_price,axis='columns')
