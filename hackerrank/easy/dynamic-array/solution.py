#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr=[]
    for x in range(n):
        arr.append([])
    last=0
    Idx=0
    ans=[]
    for r in queries:
        if r[0]==1:
            Idx=(r[1]^last)%n
            arr[Idx].append(r[2])
        elif r[0]==2:
            Idx=(r[1]^last)%n
            last=arr[Idx][r[2]%len(arr[Idx])]
            ans.append(last)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
