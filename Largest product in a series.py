#!/bin/python3

import sys
def factorial(n):
    n=int(n)
    res=1
    while n:
        res*=n%10
        n=n//10
    return res
    

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    res=0
    num=str(num)
    i=0
    while i<(len(num)-k+1):
        temp=factorial(num[i:i+k])
        if res<temp:
            res=temp
        i+=1
    print(res)
        
        
        
    
