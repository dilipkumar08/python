import math

m,n=map(int,input().split())

prod=m*n

if prod==(int(math.sqrt(prod))*int(math.sqrt(prod))):
    print('yes')
else:
    print('no')  
