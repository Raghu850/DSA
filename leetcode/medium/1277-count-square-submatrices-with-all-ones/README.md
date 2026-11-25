# Count Square Submatrices with All Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a `m * n` matrix of ones and zeros, return how many  **square**  submatrices have all ones.

 

Original
Python3
 **Example 1:** 

```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

```

 **Example 2:** 

```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

```

 

 **Constraints:** 

- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 97.19%)  
**Memory:** 22.9 MB (beats 20.76%)  
**Submitted:** 2026-11-25T11:31:18.759Z  

```py
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [0] * (COLS+1)
        res = 0
        for r in range(ROWS-1, -1, -1):
            tempDP = [0] * (COLS+1)
            for c in range(COLS-1,-1,-1):
                if matrix[r][c] == 1:
                    tempDP[c] = 1 + min(dp[c], tempDP[c+1], dp[c+1])
                    res += tempDP[c]
            dp = tempDP
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)