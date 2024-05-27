#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#

def minTime(files, numCores, limit):
    files.sort(reverse=True)
    total=0
    parallellimit=0
    print(numCores,limit,files)
    for i in files:
    
        if i%numCores==0 and parallellimit<limit:
            total+=i//numCores
            parallellimit+=1
        else:
            total+=i
    return total
    # print(numCores,limit,files)
    # files.sort(reverse=True)
    # if numCores==1:
    #     return sum(files)
    # elif numCores>1 and limit>1:
    #     if len(files)<=limit:
    #         l=len(files)
    #     else:
    #         l=limit
    #     for i in range(l):
    #         print(files[i])
    #         if files[i]%numCores==0:
    #             files[i]=files[i]//numCores
    # return sum(files)
        
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)

    fptr.write(str(result) + '\n')

    fptr.close()
