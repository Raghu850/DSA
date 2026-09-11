# Kth Largest Element in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` and an integer `k`, return  *the*  `kth`  *largest element in the array*.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

 

 **Example 1:** 

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

```

 **Example 2:** 

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

```

 

 **Constraints:** 

- 1 <= k <= nums.length <= 105
- -104 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 30 ms (beats 99.40%)  
**Memory:** 31.6 MB (beats 8.26%)  
**Submitted:** 2026-09-11T17:17:56.796Z  

```py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        # Choose a pivot element from nums
        pivot = random.choice(nums)

        left, right, equal = [], [], []
        for num in nums:
            if num > pivot:
                right.append(num)   # greater than pivot
            elif num < pivot:
                left.append(num)    # smaller than pivot
            else:
                equal.append(num)   # equal to pivot

        # Number of elements greater than pivot
        count_right = len(right)

        # If kth largest lies in right
        if k <= count_right:
            return self.findKthLargest(right, k)

        # If kth largest is in pivot group
        elif k <= count_right + len(equal):
            return pivot

        # Else, it lies in left
        else:
            # Adjust k because we skip right+equal elements
            return self.findKthLargest(left, k - count_right - len(equal))

        
```

---

[View on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)