n=int(input())
li=list(map(int,input().split()))
s=sum(li)

if s%5==0 and s%2==0 and s%3==0:
    print(1)
else:
    print(0);
