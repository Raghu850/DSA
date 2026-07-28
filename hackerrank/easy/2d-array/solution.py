#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    n = len(arr)
    m = len(arr[0])
    ans = float('-inf')
    dir = [[-1,-1], [-1,0], [-1,1], [0, 0], [1, -1], [1,0], [1, 1]]
    for i in range(1, n-1):
        for j in range(1, m-1):
            sm = 0
            for k in dir:
                sm += arr[i + k[0]][j+k[1]]
            ans = max(ans, sm)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
