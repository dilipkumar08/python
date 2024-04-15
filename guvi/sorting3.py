m,n = map(int,input().split())
li=[]
for i in range(m):
  li=li+list((map(int,input().split())))

for i in range(m*n):
  mini=i
  for j in range(i+1,m*n):
    if li[mini]>li[j]:
      mini=j
  li[mini],li[i]=li[i],li[mini]


for i in range(m):
  print(*li[(i*n):(n*(i+1))])

