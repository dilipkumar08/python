#!/bin/python3

import sys

def numsum(n,d):
    res=(n-1)//d
    return res*d*(res+1)//2
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res=0
    res+=numsum(n,3)
    res+=numsum(n,5)
    res-=numsum(n,15)
    print(res)
    
