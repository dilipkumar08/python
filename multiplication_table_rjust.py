if __name__=="__main__":
    import numpy as np
    n=int(input("Enter a number: "))
    s=len(str(n))+1
    data=np.empty((n-1,n-1),dtype=int)
    data=data*0
    for i in range(1,n):
        for j in range(1,n):
            print(str((i*j)%n).rjust(s),end='')
        print("\n")
#---------------------------------------------------------------
if __name__=="__main__":
    import numpy as np
    n=int(input("Enter a number: "))
    data=np.empty((n-1,n-1),dtype=int)
    data=data*0
    for i in range(1,n):
        for j in range(1,n):
            data[i-1][j-1]=(i*j)%n
    print(data)
