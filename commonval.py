ar1=[10,2,3,8,11,9,16,0,4]
ar2=[11,2,3,7,9,10,4,10,0]
ar1=list(set(ar1))
ar2=list(set(ar2))
print(ar1)
print(ar2)
for i in ar1:
    if i in ar2[:]:
        print(i)
