A=set(map(int,input().strip().split()))

for i in range(int(input())):
    B=set(map(int,input().strip().split()))
    if A.issuperset(B):
        res=True
    else:
        res=False
        break
print(res)

