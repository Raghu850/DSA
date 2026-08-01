# Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of size `n`, return  *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
- The input is generated such that a majority element will exist in the array.

 

 **Follow-up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 22.94%)  
**Memory:** 21 MB (beats 84.71%)  
**Submitted:** 2026-08-01T05:11:37.675Z  

```py
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                cnt=1
                ele=nums[i]
            elif nums[i]==ele:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in range(len(nums)):
            if nums[i]==ele:
                cnt1+=1
        if cnt1>len(nums)//2:
            return ele
        return -1
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element/)