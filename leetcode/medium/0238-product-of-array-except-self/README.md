# Product of Array Except Self

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return  *an array*  `answer`  *such that*  `answer[i]`  *is equal to the product of all the elements of*  `nums`  *except*  `nums[i]`.

The product of any prefix or suffix of `nums` is  **guaranteed**  to fit in a  **32-bit**  integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

 **Example 1:** 

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

 **Example 2:** 

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

 

 **Constraints:** 

- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

 **Follow up:**  Can you solve the problem in `O(1)` extra space complexity? (The output array  **does not**  count as extra space for space complexity analysis.)

## Solution

**Language:** Python  
**Runtime:** 12 ms (beats 96.90%)  
**Memory:** 25.4 MB (beats 69.96%)  
**Submitted:** 2026-08-18T05:30:42.022Z  

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_li = []
        for i in nums:
            prefix_li.append(prefix)
            prefix = prefix*i
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            prefix_li[i] = prefix_li[i]*suffix
            suffix = suffix*nums[i]
        return prefix_li

```

---

[View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)