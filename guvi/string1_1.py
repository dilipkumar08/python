n=str(input())
l=len(n)
n=".".join(n)
n=list(n.split("."))
i=0
while i<l:
  print(i)
  if l==0:
    break
  if i>0 :
    while True:

      if (i-1)<=0 or i>=l or l==0 or n[i]!=n[i-1]: 
        break
      else: 
        n.pop(i)
        n.pop(i-1)
        l-=2
        i-=2
  i+=1
                
print("".join(n))
