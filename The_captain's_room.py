from collections import Counter
n=int(input())
A=list(map(int,input().split()))
B=Counter(A)
for item,val in B.items():
    if val==1:
        print(int(item))
