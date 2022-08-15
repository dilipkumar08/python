from itertools import combinations
res=[]
s,n=input().split()
for i in range(int(n)):
    com=list(combinations(s,i+1))
    if i>0:
        for j in com:
            res.append(sorted(j))
    else:
        res=com
    for z in sorted(res):
        print("".join(z))
    res.clear()
     
       
