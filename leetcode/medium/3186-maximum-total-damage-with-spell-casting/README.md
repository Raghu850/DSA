# Maximum Total Damage With Spell Casting

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A magician has various spells.

You are given an array `power`, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of `power[i]`, they  **cannot**  cast any spell with a damage of `power[i] - 2`, `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.

Each spell can be cast  **only once**.

Return the  **maximum**  possible  *total damage*  that a magician can cast.

 

Original
Python3
 **Example 1:** 

 **Input:**  power = [1,1,3,4]

 **Output:**  6

 **Explanation:** 

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

 **Example 2:** 

 **Input:**  power = [7,1,6,6]

 **Output:**  13

 **Explanation:** 

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

 **Constraints:** 

- 1 <= power.length <= 105
- 1 <= power[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 305 ms (beats 99.55%)  
**Memory:** 34.3 MB (beats 99.55%)  
**Submitted:** 2026-11-10T21:39:03.276Z  

```py
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        
        # dp = [0] * (max(power)+1)
        power.sort()

        dp1, dp2, dp3 = 0, 0, 0
        prev = None
        prev_prev = None
        i = 0
        
        while i < len(power):
            p = power[i]
            curr_p = p
            while i + 1 < len(power) and power[i + 1] == p:
                curr_p += p
                i += 1

            if prev == None:
                dp1 = curr_p
            elif p - prev > 2:
                dp1, dp2, dp3 = dp1 + curr_p, dp1, dp2
            elif prev_prev and p - prev_prev > 2:
                dp1, dp2, dp3 = max(dp1, dp2+curr_p), dp1, dp2
            else:
                dp1, dp2, dp3 = max(dp1, dp3+curr_p), dp1, dp2

            prev, prev_prev = p, prev
            i += 1
        
        return max(dp1, dp2, dp3)
            


```

---

[View on LeetCode](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)