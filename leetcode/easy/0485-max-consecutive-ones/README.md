# Max Consecutive Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary array `nums`, return  *the maximum number of consecutive* `1` *'s in the array*.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

```

 **Example 2:** 

```
Input: nums = [1,0,1,1,0,1]
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 96.18%)  
**Memory:** 21.7 MB (beats 79.22%)  
**Submitted:** 2026-07-30T06:00:13.909Z  

```py
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        m=0
        for i in nums:
            if i:
                cnt+=1
            else:
                m=max(m,cnt)
                cnt=0
        m=max(m,cnt)
        return m

```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)