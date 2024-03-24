#Remove duplicates 
n=int(input())
data=list(map(str,input().split()))
l=len(data)
k=0
for i in data:
    k+=1
    j=k
    while j<l:
        if data[j]==i:
            data.pop(j)
            l-=1
        else:
            j+=1

print(*data)
