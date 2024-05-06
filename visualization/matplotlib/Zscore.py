import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

data=list(map(float,input().split()))
sd=np.std(data)
mn=np.mean(data)
z_score=[abs(i-mn)/sd for i in data]
plt.grid()
plt.plot(z_score,linestyle='--')
sd_list=[abs(j-sd) for j in data]
plt.plot(data)
plt.show()
