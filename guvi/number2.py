n=int(input())

ticket=list(map(int,input().split()))

date=int(input())
res=[]
for i in ticket:
    if i%date==0:
        res.append(1)
    else:
        res.append(0)
        
print(*res)
