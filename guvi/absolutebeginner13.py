import math
a,b,c=map(int,input().split())
x=(-b + math.sqrt((b**2) - (4*a*c))) / (2*a)
y=(-b-math.sqrt((b**2)-(4*a*c)) )/(2*a)
print("%.2f"%x)
print("%.2f"%y)
