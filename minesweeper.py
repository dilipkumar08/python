def Minesweeper(n=0,m=0):    
    import numpy as np
    import random
    arr=np.empty((n,m),dtype=str)
    li=[]
    mn=m*n
    M=(mn)//4
    for i in range(M):
        li.append("M")
    for j in range((mn)-M):
        li.append("0")
    random.shuffle(li)
    for i in range(n):
        for j in range(m):
            mn-=1
            arr[i][j]=li[mn]
    print("Before:\n",arr,"\n")
    for i in range(n):
        for j in range(m):
            if arr[i][j]!="M":
                temp=0
                if i+1<n:
                    if arr[i+1][j]=='M':
                        temp+=1
                if j+1<m:
                    if arr[i][j+1]=="M":
                        temp+=1
                if (i-1)>-1:
                    if arr[i-1][j]=='M':
                        temp+=1
                if (j-1)>-1:
                    if arr[i][j-1]=='M':
                        temp+=1
                if i+1<n and j+1<m:
                    if arr[i+1][j+1]=='M':
                        temp+=1
                if (i-1)>-1 and (j-1)>-1:
                    if arr[i-1][j-1]=='M':
                        temp+=1
                if i+1<n and (j-1)>-1:
                    if arr[i+1][j-1]=='M':
                        temp+=1
                if (i-1)>-1 and j+1<m:
                    if arr[i-1][j+1]=='M':
                        temp+=1
                arr[i][j]=str(temp)
    print("After:\n",arr)
