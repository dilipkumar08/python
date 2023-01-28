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
m=list(map(int,input().split()))
inp=list(map(int,input().split()))[0:m[0]]
A=list(map(int,input().split()))[0:m[1]]
B=list(map(int,input().split()))[0:m[1]]
happiness=0
i=0
l=len(inp)
while i<l:
    if inp[i] in A:
        happiness+=1
    elif inp[i] in B:
        happiness-=1
    i+=1    
print(happiness)
#trail four which is successfull
from collections import Counter
m=list(map(int,input().split()))
inp=Counter(list(map(int,input().split()))[0:m[0]])
A=set(map(int,input().split()))
B=set(map(int,input().split()))
h=0
for i in inp:
    if i in A:
        h+=inp[i]
    elif i in B:
        h-=inp[i]  
print(h)
