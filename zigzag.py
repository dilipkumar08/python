#ZIGZAG
import time,sys
i=0
cd=True
c=int(input())
while c!=0:
    print(" "*i,end="")
    print("*****")
    time.sleep(0.1)
    if cd==True:
        i+=1
        if i==5:
            c-=0.5
            cd=False
    else:
        i-=1
        if i==0:
            c-=0.5
            cd=True
        
            
