def sort(arr: list,y):
  return sorted(arr*y)

n=int(input())
a=list(map(int,input().strip().split()))
count={}

for i in a:
  count[i]=count.get(i,0)+1


res=[]
for j in set(count.values()):
  temp=[]

  for x,y in count.items():
    if y==j:
      temp.append(x)
    
  res=res+sort(temp,j)
print(*res)
