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
**Runtime:** 7 ms (beats 48.38%)  
**Memory:** 20.4 MB (beats 70.52%)  
**Submitted:** 2026-09-06T13:30:13.202Z  

```py
from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        n_provinces = 0

        visited = [0] * n

        def bfs(start):
            q = deque()
            q.append(start)
            visited[start] = 1

            while q:
                city = q.popleft()

                # Check every possible city connected to current city
                for neighbor in range(n):

                    if isConnected[city][neighbor] == 1 and visited[neighbor] == 0:
                        visited[neighbor] = 1
                        q.append(neighbor)

        for city in range(n):

            if visited[city] == 0:
                bfs(city)
                n_provinces += 1

        return n_provinces


# Kinda wrong approach for this question
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         # isConnected is a adjacency matrix -> 
#         n_provinces = 0
#         # connected component definition: 
#         # connected component in an undirected graph is a subgraph in which we can travel to
#         # any node from any node 
#         n_rows = len(isConnected)
#         n_cols = len(isConnected[0])

#         directions = [
#             [0,1],
#             [0,-1],
#             [1,0],
#             [-1,0]
#         ]
#         # create a bfs function -> once we find a element which is not visited ,
#         # we run a bfs and find all nodes of that connected components
#         def bfs(row:int, col:int):
#             q = deque()
#             q.append((row,col))
            
#             while q:
#                 row, col = q.popleft()
#                 visited[row][col] = 1
#                 for dr,dc in directions:
#                     new_row = row + dr
#                     new_col = col + dc

#                     if new_row < n_rows and new_row > 0 and new_col < n_cols and new_col > 0 and visited[new_row][new_col] == 0 and isConnected[new_row][new_col] == 1:
#                         q.append((new_row,new_col))



#         # maintaining a 2d visited array to mark the elements which are already visited
#         visited = [[0] * n_cols for _ in range(n_rows)] 

#         # Iterated from i = 0 --> no. of rows
#         # then same for j = 0 --> no. of cols
       
#         for i in range(n_rows):
#             for j in range(n_cols):
#                 if visited[i][j] == 0:
#                     bfs(i,j)
#                     n_provinces += 1

#         return n_provinces
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-provinces/)