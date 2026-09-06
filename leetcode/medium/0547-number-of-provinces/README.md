# Number of Provinces

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A  **province**  is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return  *the total number of  **provinces***.

 

 **Example 1:** 

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

```

 **Example 2:** 

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

```

 

 **Constraints:** 

- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 21.5 MB (beats 21.16%)  
**Submitted:** 2026-09-06T13:31:07.002Z  

```py
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        vis = [False] * m
        def dfs(node):
            vis[node] = True
            for j in range(m):
                if not vis[j] and isConnected[node][j] == 1 and node != j:
                    dfs(j)

        count = 0
        for i in range(m):
            if not vis[i]:
                dfs(i)
                count += 1

        return count
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-provinces/)