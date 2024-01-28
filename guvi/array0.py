n=int(input())
li=list(map(int,input().split()))
print(li.index(max(li))-li.index(min(li)))
