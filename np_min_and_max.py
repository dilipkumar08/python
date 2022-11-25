import numpy as np
N,M=map(int,input().split())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))
arr=np.array(li)
print(np.max(np.min(arr,axis=1)))
    
