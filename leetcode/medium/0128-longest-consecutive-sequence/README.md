# Longest Consecutive Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an unsorted array of integers `nums`, return  *the length of the longest consecutive elements sequence.* 

You must write an algorithm that runs in `O(n)` time.

 

 **Example 1:** 

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

 **Example 2:** 

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

 **Example 3:** 

```
Input: nums = [1,0,1,2]
Output: 3

```

 

 **Constraints:** 

- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.2 MB  
**Submitted:** 2026-11-09T15:36:32.348Z  

```py
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        longest_len = 0
        start = 0
        if len(nums) < 2:
            return len(nums)
        for idx in range(1,len(nums)):
            if nums[idx] - nums[idx-1] != 1:
                longest_len = max(longest_len, idx - start)
                start = idx
        longest_len = max(longest_len, idx - start + 1)
        return longest_len
```

---

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)