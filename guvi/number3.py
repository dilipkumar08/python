n=int(input())
li=list(map(int,input().split()))

min_val=li[0]
min_ind=0
max_val=li[0]
max_ind=0
for i in range(1,len(li)):
    if li[i]>max_val:
        max_val=li[i]
        max_ind=i
    if li[i]<min_val:
        min_val=li[i]
        min_ind=i
print(max_ind-min_ind)
    
