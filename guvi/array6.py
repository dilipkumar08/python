n=int(input())
a=0
li=list(map(int,input().split()))
for i in li:
    if li.count(i)==2:
        a=i
        break
    
print(a)
