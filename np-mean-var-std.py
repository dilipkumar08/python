import numpy
N,M=map(int,input().split())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))
arr1=numpy.array(li)
print(numpy.mean(arr1,axis=1))
print(numpy.var(arr1,axis=0))
print(round(numpy.std(arr1,axis=None),11))
