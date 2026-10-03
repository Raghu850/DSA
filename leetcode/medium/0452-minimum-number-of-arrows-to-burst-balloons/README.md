# Minimum Number of Arrows to Burst Balloons

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose  **horizontal diameter**  stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up  **directly vertically**  (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is  **burst**  by an arrow shot at `x` if `xstart <= x <= xend`. There is  **no limit**  to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return  *the  **minimum**  number of arrows that must be shot to burst all balloons*.

 

 **Example 1:** 

```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

```

 **Example 2:** 

```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

```

 **Example 3:** 

```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

```

 

 **Constraints:** 

- 1 <= points.length <= 105
- points[i].length == 2
- -231 <= xstart < xend <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 69 ms (beats 71.63%)  
**Memory:** 53.4 MB (beats 66.41%)  
**Submitted:** 2026-10-03T17:27:05.317Z  

```py
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
            
        
        points.sort(key=lambda x: x[1])
        
        arrows = 0
        arrow_position = None
        
        for start, end in points:
           
            if arrow_position is None or start > arrow_position:
                arrows += 1
                arrow_position = end
                
        return arrows
        
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)