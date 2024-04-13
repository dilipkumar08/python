n=int(input())

temp=list(map(str,input().split()))
l=len(temp);
di={}
for i in range(1,l,2):
    di[int(temp[i])]=temp[i-1]
    
for i in list(sorted(di.keys())):
    print(di[i])
    
