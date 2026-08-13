# Find a Peak Element II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A  **peak**  element in a 2D grid is an element that is  **strictly greater**  than all of its  **adjacent** neighbors to the left, right, top, and bottom.

Given a  **0-indexed**  `m x n` matrix `mat` where  **no two adjacent cells are equal**, find  **any**  peak element `mat[i][j]` and return  *the length 2 array* `[i,j]`.

You may assume that the entire matrix is surrounded by an  **outer perimeter**  with the value `-1` in each cell.

You must write an algorithm that runs in `O(m log(n))` or `O(n log(m))` time.

 

 **Example 1:** 

```
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

```

 **Example 2:** 

```
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

```

 

 **Constraints:** 

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 500
- 1 <= mat[i][j] <= 105
- No two adjacent cells are equal.

## Solution

**Language:** Python  
**Runtime:** 18 ms (beats 11.33%)  
**Memory:** 46.3 MB (beats 15.36%)  
**Submitted:** 2026-08-13T16:07:36.333Z  

```py
class Solution:
    def findPeakGrid(self, mat):
        ans = [0, 0]
        max_val = float('-inf')

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > max_val:
                    max_val = mat[i][j]
                    ans = [i, j]

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/find-a-peak-element-ii/)