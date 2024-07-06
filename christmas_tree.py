
a=(10,3)
space=a[0]

for i in range(1,a[0],2):
  print((space-1)*' ',i*'* ')
  space-=2

for j in range(a[1]):
  print((a[0]-a[1])*' ',a[1]*'* ')
