import numpy as np
import math
data=np.array([5,6,12,40,234,80])
x=min(data)
print('minimum',x)
y=max(data)
print("maximum",y)
m=data.mean()
print("mean:",m)
ab=abs(m)
print('absolute Value of mean',ab)
power=pow(y,x)
print("power:",power)
sq=math.sqrt(x)
print("square root of x:",sq)
ceiling=math.ceil(m)
print("ceiling value of mean:",ceiling)
floor=math.floor(m)
print("floor value of mean:",floor)
pi=math.pi
print("pi:",pi)
print(round(pi,2))
