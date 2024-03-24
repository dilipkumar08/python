n=int(input())
data=list(map(int,input().split()))

temp=data[0]
for i in data[1:]:
    if i<temp:
        temp=i
print(temp)
