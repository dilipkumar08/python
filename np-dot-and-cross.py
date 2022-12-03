import numpy
N=int(input())
A,B=[],[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
arr1=numpy.array(A)
arr2=numpy.array(B)
print(numpy.dot(arr1,arr2))
