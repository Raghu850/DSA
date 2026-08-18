# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 49.23%)  
**Memory:** 20.6 MB (beats 24.66%)  
**Submitted:** 2026-08-18T06:56:06.220Z  

```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=-1
        for j in range(len(nums)):
            if nums[j]==0:
                i=j
                break
        if i==-1: return
        for j in range(i+1,len(nums)):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
        
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)