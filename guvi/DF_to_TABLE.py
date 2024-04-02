import numpy as np
import pandas as pd
import pymysql as sql
import seaborn as sb

connection=sql.connect(host='127.0.0.1',user='root',password='mysql')
db1=connection.cursor()
tp=sb.load_dataset("tips")
colmn=[i.replace( "-","_").replace(" ","_")for i in tp.columns]
columns=",".join(f"{i} {j}" for i,j in zip(colmn,tp.dtypes))
table_name='tips'
tc=f"create table {table_name}  ({columns});"

tc=tc.replace("float64","float").replace("category","text").replace("int64","int").replace("object","text")
print(tc)

db1.execute("use guvi")
db1.execute(tc)

insert=f"insert into {table_name} values"
for i in range(0,len(tp)):
    db1.execute(insert+str(tuple(tp.iloc[i])))
    connection.commit()
