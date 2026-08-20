# Longest Subarray of 1's After Deleting One Element

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary array `nums`, you should delete one element from it.

Return  *the size of the longest non-empty subarray containing only* `1` *'s in the resulting array*. Return `0` if there is no such subarray.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

```

 **Example 2:** 

```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

```

 **Example 3:** 

```
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 96.19%)  
**Memory:** 24.4 MB (beats 51.92%)  
**Submitted:** 2026-08-20T04:45:04.591Z  

```py
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        has_zero = False
        encounter_zero = False
        prev_0 = -1
        size = 0
        tr = 0
        for i, n in enumerate(nums):
            if n:
                size += 1
            else:
                encounter_zero = True
                if has_zero:
                    size = i - prev_0 - 1
                    size = size if size>0 else 0
                has_zero = True if size else False
                prev_0 = i
            if size > tr:
                tr = size
                
        if encounter_zero:
            return tr
        else:
            return max(tr-1, 0)
                
```

---

[View on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)