n=int(input())
n=str(n)
l=len(n)
res=''

for i in range(l): 
           
    if i==0 and (i+1)!=l:
        if n[i]!=n[i+1]:
            res+=n[i]
                  
    elif i<(l-1) and i>0:
        if n[i]!=n[i+1] and n[i]!=n[i-1]:
                res+=n[i]
                  
    elif i==(l-1) and i>0:
        if n[i]!=n[i-1]:
            res+=n[i]
                    
if res=='':
    print('-1')
else:
    print(res)
                

    
