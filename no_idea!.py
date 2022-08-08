#trail1
mn=input()
inp=list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
h=0
for i in inp:
    if i in A:
        h+=1
    elif i in B:
        h-=1
print(h)
#passed test case 0, 1, 2, 3, 7 (code works but need to reduce time complexity)

#trail2
from collections import Counter
mn=input()
inp=Counter(list(map(int,input().split())))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
h=0
for i in inp:
    if i in A:
        h+=inp[i]
    elif i in B:
        h-=inp[i]  
print(h)
#passed test case 0, 1, 2, 7 (code works but not better than the previous one need to reduce time complexity)
