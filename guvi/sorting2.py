n=str(input())

n=".".join(n)

li=list(map(int,n.split('.')))
l=len(li)
for i in range(l):
    for j in range(l-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]


for i in range(1,l):
    if li[0]==0 and li[i]!=0:
        li[0],li[i]=li[i],li[0]
print("".join(map(str,li)))
