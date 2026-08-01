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
**Runtime:** 44 ms (beats 78.53%)  
**Memory:** 36.6 MB (beats 66.24%)  
**Submitted:** 2026-08-01T08:15:14.122Z  

```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        longest=0
        cnt=0
        for i in h:
            if i-1 not in h:
                cnt=1
                while i+cnt in h:
                    cnt+=1
            longest=max(longest,cnt)
        return longest
```

---

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)