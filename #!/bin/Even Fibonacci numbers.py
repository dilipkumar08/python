#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=0
    b=1
    res=0
    
    while b<n:
        if b%2==0:
            res+=b
        a,b=b,a+b
    print(res)
