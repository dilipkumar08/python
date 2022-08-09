from collections import deque
n=int(input())
d=deque()
for i in range(n):
    c=list(map(str,input().split()))
    if c[0]=="append":
        d.append(int(c[1]))
    elif c[0]=="pop":
        d.pop()
    elif c[0]=="popleft":
        d.popleft()
    elif c[0]=="appendleft":
        d.appendleft(int(c[1]))
print(*d,sep=" ")
