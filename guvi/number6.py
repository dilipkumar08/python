n=int(input())

li=list(map(int,input().split()))
rec=dict()
for i in set(li):
        rec[i]=li.count(i)

max_val=max(rec.values())

for key,value in rec.items():
    if value==max_val:
        print(key)
