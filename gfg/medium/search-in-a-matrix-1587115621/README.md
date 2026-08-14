# Search in a sorted Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a strictly sorted 2D matrix **mat** [][] of size  **n x m** and a number  **x.**  Find whether the number  **x**  is present in the matrix or not.
 **Note:**  In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the  **i** th row (**i** !=0) is greater than the last element of the (**i-1**)th row.

 **Examples:** 

```
Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
Output: true
Explanation: 14 is present in the matrix, so output is true.

```

```
Input: mat[][] = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42
Output: false
Explanation: 42 is not present in the matrix.

```

```
Input: mat[][] = [[87, 96, 99], [101, 103, 111]], x = 101
Output: true
Explanation: 101 is present in the matrix.
```

**Constraints:
**1 ≤ n, m ≤ 1000
1 ≤ mat[i][j] ≤ 109
1 ≤ x ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T21:27:34.138Z  

```py
class Solution:
    def searchMatrix(self, mat, x): 
    	# code here 
    	rows = len(mat)
        cols = len(mat[0])
    
        row = 0
        col = cols - 1
    
        while row < rows and col >= 0:
            if mat[row][col] == x:
                return True
    
            elif mat[row][col] >x:
                col -= 1
    
            else:
                row += 1
    
        return False
        	

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1)