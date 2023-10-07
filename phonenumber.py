#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPhoneNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getPhoneNumber(s):
    di={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    li=list(s.split(' '))
    a=''
    for i in range(len(li)):

        if li[i].lower()=='double':
            i=i+1
            a=a+di[li[i].lower()
        elif li[i].lower()=='triple':
            i=i+1
            a=a+di[li[i].lower()]+di[li[i].lower()]
        else:
            a=a+di[li[i].lower()]
    return(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getPhoneNumber(s)

    fptr.write(result + '\n')

    fptr.close()
