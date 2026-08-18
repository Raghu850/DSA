# Can Place Flowers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in  **adjacent**  plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true`  *if*  `n`  *new flowers can be planted in the*  `flowerbed`  *without violating the no-adjacent-flowers rule and*  `false`  *otherwise*.

 

 **Example 1:** 

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

```

 **Example 2:** 

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

```

 

 **Constraints:** 

- 1 <= flowerbed.length <= 2 * 104
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 78.71%)  
**Memory:** 19.4 MB (beats 95.99%)  
**Submitted:** 2026-08-18T05:23:05.813Z  

```py
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                left=(i==0 or flowerbed[i-1]==0)
                right=(i==len(flowerbed)-1 or flowerbed[i+1]==0)
                if left and right:
                    flowerbed[i]=1
                    n-=1
            if n<=0:
                return True
        return False
```

---

[View on LeetCode](https://leetcode.com/problems/can-place-flowers/)