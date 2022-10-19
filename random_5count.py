#method1
import numpy as np
def random_5count(n=None):
    if n==None:
        n=np.random.randint(low=0,high=101)
    print("n =",n,end="\n")
    arr=np.random.randint(low=0,high=6,size=(n,n),dtype=np.int64)
    print("array:\n",arr)
    print("Count of 5 in the array: ",np.count_nonzero(arr==5))
random_5count() #You can pass the n value if you want or you can just run it

#method2
import numpy as np
def random_5count(n=None):
    if n==None:
        n=np.random.randint(low=0,high=101)
    print("n =",n,end="\n")
    arr=np.random.randint(low=0,high=6,size=(n,n),dtype=np.int64)
    print("array:\n",arr)
    b=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==5:
                b+=1
    print("Count of 5 in the array: ",b)
random_5count() #You can pass the n value if you want or you can just run it
