#method-1
import numpy as np
def checkerboard(n):
    l=[]
    li=[]
    one=1
    temp=0
    two=2
    for i in range(n*n):
        l.append(one)
        temp=one
        one=two
        two=temp
        if len(l)==n:
            li.append(l)
            l=[]    
    arr=np.array(li,dtype=int)
    print(arr)
    
if __name__=="__main__":
    n=int(input("Enter an integer: "))
    checkerboard(n)
#-----------------------------------------------------------------------
#method-2
import numpy as np 
def checkerboard(n): 
    arr = np.ones((n, n), dtype = int) 
    arr[1::2, ::2] = 2
    arr[::2, 1::2] = 2
    print(arr)
if "__main__"==__name__:
    n=int(input("Enter an integer: "))
    checkerboard(n)
