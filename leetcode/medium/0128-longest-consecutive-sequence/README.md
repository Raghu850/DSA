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
**Runtime:** 50 ms (beats 61.80%)  
**Memory:** 36.5 MB (beats 62.67%)  
**Submitted:** 2026-11-09T15:36:11.176Z  

```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       h=set(nums)
       m=0
       for i in h:
        if (i-1) not in h:
            count=1
            while i+count in h:
                count+=1
            m=max(m,count)
       return m
```

---

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)