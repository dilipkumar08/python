import pickle
a=["dilip","kumar","co","data","sc","008","ai"]

with open("pickle.txt","wb")  as file:
    pickle.dump(a,file)
with open("pickle.txt","rb") as file:
    b=pickle.load(file)
print(b)
