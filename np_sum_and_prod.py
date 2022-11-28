import numpy as np
N,M=map(int,input().strip().split())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))

print(np.prod(np.sum(np.array(li),axis=0)))
