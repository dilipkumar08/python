from collections import namedtuple
N=int(input())
s=0
Students=namedtuple("Students",input().split())
for i in range(N):
    stud=Students(*input().split())
    s+=int(stud.MARKS)
    
print(s/N)
  
