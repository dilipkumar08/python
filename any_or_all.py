N=int(input())
l=list(map(int,input().split()))
print(all(x==abs(x) for x in l) and any(str(x)==str(x)[::-1] for x in l))
