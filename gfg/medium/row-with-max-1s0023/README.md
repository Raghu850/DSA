# Row with Max 1s in Rowwise Sorted

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a 2D binary array `arr[][]` consisting of only `1`s and `0`s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of `1`s. If no such row exists, return `-1`.

 **Note:** 

- The array follows 0-based indexing.
- The number of rows and columns in the array are denoted by n.

 **Examples:** 

```
Input: arr[][] = [[0,1,1,1],
               [0,0,1,1],
               [1,1,1,1],
               [0,0,0,0]]
Output: 2
Explanation: Row 2 contains the most number of 1s (4 1s). Hence, the output is 2.
```

```
Input: arr[][] = [[0,0],
               [1,1]]
Output: 1
Explanation: Row 1 contains the most number of 1s (2 1s). Hence, the output is 1.
```

```
Input: arr[][] = [[0,0], 
               [0,0]]
Output: -1
Explanation: No row contains any 1s, so the output is -1.
```

 **Constraints:** 
1 ≤ arr.size(), arr[i].size() ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T21:20:57.874Z  

```py
class Solution:
    def rowWithMax1s(self, mat):
        # code here
        rows = len(mat)
        cols = len(mat[0])

        max_ones = 0
        answer = -1

        for i in range(rows):
            low = 0
            high = cols - 1

            # Find first 1 using binary search
            while low <= high:
                mid = (low + high) // 2

                if mat[i][mid] == 1:
                    high = mid - 1
                else:
                    low = mid + 1

            # low = index of first 1
            ones = cols - low

            if ones > max_ones:
                max_ones = ones
                answer = i

        return answer
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1)