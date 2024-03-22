import pickle
a=["dilip","kumar","co","data","sc","008","ai"]

with open("pickle.txt","wb")  as file:
    pickle.dump(a,file)
with open("pickle.txt","rb") as file:
    b=pickle.load(file)
print(b)

import pickle as pk

a='jumbo circus ku vanga jolly ah poonga'
b=pk.dumps(a)
print(b)
print(pk.loads(b))

# with open("","") as file:
