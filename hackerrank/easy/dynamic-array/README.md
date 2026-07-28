# Dynamic Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

- Declare a 2-dimensional array, $arr$, with $n$ empty arrays, all zero-indexed.
- Declare an integer, $lastAnswer$, and initialize it to 0.

You need to process two types of queries:

1. Query: $1\ x\ y$
   - Compute $idx = (x \oplus lastAnswer) % n$.
   - Append the integer $y$ to $arr[idx]$.

2. Query: $2\ x\ y$
   - Compute $idx = (x \oplus lastAnswer) % n$.
   - Set $lastAnswer = arr[idx][y \% size(arr[idx])]$.
   - Store the new value of $lastAnswer$ in an answers array.

**Notes:**  
- $\oplus$ is the *bitwise XOR* operation, which corresponds to the `^` operator in most languages. Learn more about it on [Wikipedia](https://en.wikipedia.org/wiki/Exclusive_or).  
- $\%$ is the modulo operator.   
- Finally, $size(arr[idx])$ is the number of elements in $arr[idx]$.  

**Function Description**  

Complete the $dynamicArray$ function with the following parameters:  
- $int\ n$: the number of empty arrays to initialize in $arr$  
- $int\ queries[q][3]$: 2-D array of integers

**Returns**  

- $int[]$:  the results of each type 2 query in the order they are presented  

**Input Format**

The first line contains two space-separated integers, $n$, the size of $arr$ to create, and $q$, the number of queries, respectively.		
Each of the $q$ subsequent lines contains a query string, $queries[i]$.

**Constraints**

- $1 \leq  n, q \leq  10^5$
- $0 \leq x, y \leq 10^9$
- It is guaranteed that query type $2$ will never query an empty array or index.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T09:01:16.889Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/dynamic-array/problem)