#longest arithmetic progression

li=[]
n=int(input('Enter the length of the list'))
for i in range(n):
    li.append(int(input(f"Enter the {i+1} number:")))
res=[]
l=len(li)
i=0

while (i+2<l):
    
    if li[i]-li[i+1]==li[i+1]-li[i+2]:

        res.append([li[i],li[i+1],li[i+2]])
        
        i+=3
        
    else:
        
        i+=1
        
print(res)
        




    
