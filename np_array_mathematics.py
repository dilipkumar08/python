import numpy as np
N,M=map(int,input().split())
A=[]
B=[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
A=np.array(A)
B=np.array(B)
print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(A//B)
print(np.mod(A,B))
print(np.power(A,B))
