import numpy as np
a=np.array(['mercury','venus','jupyter','uranus'])
print(a)
print(a.shape)
a=np.where(a=='jupyter',"saturn",a)
print(*a,sep="\n")
