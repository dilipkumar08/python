from collections import defaultdict
m,n=map(int,input().strip().split())
A=defaultdict(list)
B=[]
#Adding indexes to A for the given input
for i in range(1,m+1):
    temp=input()
    A[temp].append(i)
#Adding elements to B
for j in range(n):
    B.append(input())
#checking and printing the index
for k in B:
    if A[k]==[]:
        print(-1)
    else:
        print(*A[k])
