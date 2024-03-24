#next smallest of all num in the array

n=int(input())
data=list(map(int,input().split()))
l=len(data)
temp=0
for i in range(l):
    temp+=1
    temp1=data[i]
    #print("temp1:",temp1,"temp",temp)
    for j in range(temp,l):
        if j<l:
            if data[i]>data[j]:
                data[i]=data[j]
                break
    #print(data[i],temp1," -1")    
    if data[i]==temp1:
        data[i]=-1
    
                
        
print(*data)
                
