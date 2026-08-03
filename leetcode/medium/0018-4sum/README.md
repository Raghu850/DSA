# 4Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` of `n` integers, return  *an array of all the  **unique**  quadruplets*  `[nums[a], nums[b], nums[c], nums[d]]` such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

```

 **Example 2:** 

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 200
- -109 <= nums[i] <= 109
- -109 <= target <= 109

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 96.78%)  
**Memory:** 19.6 MB (beats 6.24%)  
**Submitted:** 2026-08-03T18:26:59.000Z  

```py
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        def two_sum(nums, target):
            seen = set()
            res = set()
            for num in nums:
                if target - num in seen:
                    res.add((target - num, num))
                seen.add(num)
            
            return res

        def k_sum(nums, target, k):

            res = []

            average = target // k

            if nums[0] > average or nums[-1] < average:
                return res

            if k == 2:
                return two_sum(nums, target)
            else:
                for idx in range(len(nums) - k + 1):
                    if idx > 0 and nums[idx - 1] == nums[idx]:
                        continue 
                    results = k_sum(nums[idx + 1:], target - nums[idx], k - 1)
                    for result in results:
                        result = list(result)
                        result.append(nums[idx])
                        res.append(result)
            return res

        return k_sum(nums, target, 4)
```

---

[View on LeetCode](https://leetcode.com/problems/4sum/)