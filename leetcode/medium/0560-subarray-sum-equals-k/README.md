# Subarray Sum Equals K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums` and an integer `k`, return  *the total number of subarrays whose sum equals to*  `k`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,1,1], k = 2
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,2,3], k = 3
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 47.92%)  
**Memory:** 21.9 MB (beats 56.68%)  
**Submitted:** 2026-08-01T10:20:18.728Z  

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h={0:1}
        s=0
        res=0
        for i in nums:
            s+=i
            res+=h.get(s-k,0)
            h[s]=1+h.get(s,0)
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)