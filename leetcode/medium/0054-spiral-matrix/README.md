# Spiral Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an `m x n` `matrix`, return  *all elements of the*  `matrix`  *in spiral order*.

 

 **Example 1:** 

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

```

 **Example 2:** 

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```

 

 **Constraints:** 

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 33.82%)  
**Submitted:** 2026-08-01T10:06:23.354Z  

```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m=len(matrix),len(matrix[0])
        l,r=0,m-1
        top,bottom=0,n-1
        ans=[]
        while top<=bottom and l<=r:
            for i in range(l,r+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][r])
            r-=1
            if top<=bottom:
                for i in range(r,l-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if l<=r:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][l])
                l+=1
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/spiral-matrix/)