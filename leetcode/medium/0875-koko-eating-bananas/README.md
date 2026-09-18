# Koko Eating Bananas

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return  *the minimum integer*  `k`  *such that she can eat all the bananas within*  `h`  *hours*.

 

 **Example 1:** 

```
Input: piles = [3,6,7,11], h = 8
Output: 4

```

 **Example 2:** 

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30

```

 **Example 3:** 

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23

```

 

 **Constraints:** 

- 1 <= piles.length <= 104
- piles.length <= h <= 109
- 1 <= piles[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 150 ms (beats 96.18%)  
**Memory:** 20.7 MB (beats 13.16%)  
**Submitted:** 2026-09-18T09:20:56.847Z  

```py
class Solution:
    def timeTaken(self, piles: List[int], speed: int) -> int:
        totalTime = 0
        for n in piles:
            totalTime += ceil(n/speed)
        
        return totalTime

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The range shuld be between min(piles) and max(piles)
        low = 1
        high = max(piles)
        ans = 1e9

        while(low <= high):
            mid = low + (high-low)//2

            # If within limits look for a lower number
            if self.timeTaken(piles, mid) <= h:
                ans = mid
                high = mid - 1
            
            # Look for a higher number
            else:
                low = mid + 1
        
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)