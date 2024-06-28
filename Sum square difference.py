#!/bin/python3

import sys

def your_typical_function(n):
    res1=0
    res2=0
    for i in range(1,n+1):
        res1+=i
        res2+=i*i
        
    return (res1*res1)-res2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(your_typical_function(n))
