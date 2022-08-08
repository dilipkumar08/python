from collections import Counter
n=int(input())
size=list(map(int,input().split()))
c=int(input())
size_count=Counter(size)
amount=0
for i in range(c):
    sp=list(map(int,input().split()))
    if size_count[sp[0]]!=0:
        amount+=sp[1]
        size_count[sp[0]]=size_count[sp[0]]-1
    sp.clear()
print(amount)
