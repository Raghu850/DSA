# Minimum Operations to Reduce X to Zero

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this  **modifies**  the array for future operations.

Return  *the  **minimum number**  of operations to reduce* `x`  *to  **exactly***  `0`  *if it is possible**, otherwise, return* `-1`.

 

 **Example 1:** 

```
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

```

 **Example 2:** 

```
Input: nums = [5,6,7,8,9], x = 4
Output: -1

```

 **Example 3:** 

```
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104
- 1 <= x <= 109

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-09-23T14:59:17.451Z  

```py
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # prefixes = [0]
        # for num in nums:
        #     prefixes.append(num + prefixes[-1])
        
        # target = prefixes[-1] - x
        target = sum(nums) - x
        if target == 0:
            return n
        elif target < 0:
            return -1

        res = -1
        currsum = 0
        l = 0
        for r in range(n):
            currsum += nums[r]
            while currsum > target:
                currsum -= nums[l]
                l += 1
            
            if currsum == target:
                res = max(res, (r - l + 1))    
        return n - res if res != -1 else -1
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)