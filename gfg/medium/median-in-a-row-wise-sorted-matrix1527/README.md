# Median in a Row-Wise Sorted Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a row-wise sorted matrix  **mat[][]**  of size  **n x m**, where the number of rows and columns is always  **odd**. Return the  **median**  of the matrix.

 **Examples:** 

```
Input: mat[][] = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.

```

```
Input: mat[][] = [[2, 4, 9], [3, 6, 7], [4, 7, 10]]
Output: 6
Explanation: Sorting matrix elements gives us [2, 3, 4, 4, 6, 7, 7, 9, 10]. Hence, 6 is median.
```

```
Input: mat = [[3], [4], [8]]
Output: 4
Explanation: Sorting matrix elements gives us [3, 4, 8]. Hence, 4 is median.

```

 **Constraints:** 
1 ≤ n, m ≤ 400
1 ≤ mat[i][j] ≤ 2000

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T20:22:25.378Z  

```py
class Solution:
    def median(self, mat):
    	# code here 
     rows = len(mat)
     cols = len(mat[0])

     low = min(row[0] for row in mat)
     high = max(row[-1] for row in mat)

     required = (rows * cols + 1) // 2

     while low <= high:
         mid = (low + high) // 2

         count = 0

         # Count elements <= mid
         for row in mat:
             l = 0
             r = cols

             while l < r:
                 m = (l + r) // 2

                 if row[m] <= mid:
                     l = m + 1
                 else:
                     r = m

             count += l

         if count < required:
             low = mid + 1
         else:
             high = mid - 1

     return low
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1)