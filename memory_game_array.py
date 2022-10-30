
def memorygame(n=-1):   
    import random
    from random import shuffle
    import numpy as np
    database=[1,2,3,4,5,6,7,8,9,0,'!','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '~', '?', '>', '<', '//', '|','\\','{','}','[',']']
    len(database)
    while True:
        if -1<n<14:
            break
        else:
            print("\nAs there is only limited amount of characters in the database\nThe maximum size of the array can only be 13x13 for now.")
            n=int(input("\nPlease Enter a integer less than 14 and greater than -1: "))
    if n%2==0:
        n1=(n*n)//2
        n2=(n*n)-1
        mg=list(random.sample(database,n1))
        mg+=mg
        shuffle(mg)
        arr=np.empty(shape=(n,n),dtype=str)
        for i in range(n):
            for j in range(n):
                arr[i][j]=mg[n2]
                n2-=1
        print("\n",arr)
    else:
        n1=((n*n)//2)+1
        n2=(n*n)-1
        mg=list(random.sample(database,n1))
        mg+=mg[:n1-1]
        shuffle(mg)
        arr=np.empty(shape=(n,n),dtype=str)
        for i in range(n):
            for j in range(n):
                arr[i][j]=mg[n2]
                n2-=1
        print("\n",arr)
 
