import numpy
N=int(input())
li=[]
for i in range(N):
    li.append(list(map(float,input().split())))
arr=numpy.array(li)
print(round(numpy.linalg.det(arr),2))
