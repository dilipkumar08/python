import numpy as np
N,M,P=map(int,input().strip().split())
arr1=np.array(list(input().split() for i in range(N)),dtype=int)
arr2=np.array(list(input().split() for i in range(M)),dtype=int)
print(np.concatenate((arr1,arr2),axis=0))
