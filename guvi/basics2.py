N,inp=map(int,input().split())

li=list(map(int,input().split()))
count=-1
for i in li:
    if i==inp:
        count+=1
        
print(count)
    
