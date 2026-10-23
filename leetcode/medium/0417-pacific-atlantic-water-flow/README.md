# Pacific Atlantic Water Flow

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is an `m x n` rectangular island that borders both the  **Pacific Ocean**  and  **Atlantic Ocean**. The  **Pacific Ocean**  touches the island's left and top edges, and the  **Atlantic Ocean**  touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the  **height above sea level**  of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is  **less than or equal to**  the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return  *a  **2D list**  of grid coordinates* `result` *where* `result[i] = [ri, ci]` *denotes that rain water can flow from cell* `(ri, ci)` *to  **both**  the Pacific and Atlantic oceans*.

 

 **Example 1:** 

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

```

 **Example 2:** 

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

```

 

 **Constraints:** 

- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 105

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 99.31%)  
**Memory:** 20.5 MB (beats 95.00%)  
**Submitted:** 2026-10-23T15:57:44.344Z  

```py
List = list

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def reachable(starts):
            seen = [[False] * n for _ in range(m)]
            stack = []

            for r, c in starts:
                if not seen[r][c]:
                    seen[r][c] = True
                    stack.append((r, c))

            while stack:
                r, c = stack.pop()

                if r > 0 and not seen[r - 1][c] and heights[r - 1][c] >= heights[r][c]:
                    seen[r - 1][c] = True
                    stack.append((r - 1, c))
                if r + 1 < m and not seen[r + 1][c] and heights[r + 1][c] >= heights[r][c]:
                    seen[r + 1][c] = True
                    stack.append((r + 1, c))
                if c > 0 and not seen[r][c - 1] and heights[r][c - 1] >= heights[r][c]:
                    seen[r][c - 1] = True
                    stack.append((r, c - 1))
                if c + 1 < n and not seen[r][c + 1] and heights[r][c + 1] >= heights[r][c]:
                    seen[r][c + 1] = True
                    stack.append((r, c + 1))

            return seen

        pacific_starts = []
        atlantic_starts = []

        for c in range(n):
            pacific_starts.append((0, c))
            atlantic_starts.append((m - 1, c))

        for r in range(m):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, n - 1))

        pacific = reachable(pacific_starts)
        atlantic = reachable(atlantic_starts)

        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result
```

---

[View on LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)