M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
c=[]
for i in a:
    if i not in b:
        c.append(i)
        
for j in b:
    if j not in a:
        c.append(j)
c.sort()
for k in c:
    print(k)  
