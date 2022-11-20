import numpy as np
N,M=map(int,input().strip().split())
li=[]
for i in range(N):
    li.append(list(map(int,input().strip().split())))
arr=np.array(li,dtype=int)
print(np.transpose(arr))
print(arr.flatten())
