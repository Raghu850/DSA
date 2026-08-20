# Equal Row and Column Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a  **0-indexed**  `n x n` integer matrix `grid`,  *return the number of pairs* `(ri, cj)` *such that row* `ri` *and column* `cj` *are equal*.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

 **Example 1:** 

```
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

```

 **Example 2:** 

```
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

```

 

 **Constraints:** 

- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 105

## Solution

**Language:** Python  
**Runtime:** 25 ms (beats 51.23%)  
**Memory:** 24.6 MB (beats 55.98%)  
**Submitted:** 2026-08-20T09:18:28.862Z  

```py
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq={}
        for row in grid:
            r=tuple(row)
            freq[r]=freq.get(r,0)+1
        ans=0
        n=len(grid)
        for j in range(n):
            col=[]
            for i in range(n):
                col.append(grid[i][j])
            c=tuple(col)
            if c in freq:
                ans+=freq[c]
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/)