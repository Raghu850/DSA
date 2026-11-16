# Number of Zero-Filled Subarrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return  *the number of  **subarrays**  filled with* `0`.

A  **subarray**  is a contiguous non-empty sequence of elements within an array.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

 **Example 2:** 

```
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

```

 **Example 3:** 

```
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 99.50%)  
**Memory:** 30.6 MB (beats 9.93%)  
**Submitted:** 2026-11-16T18:04:02.143Z  

```py
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        length_of_zero = 0
        total = 0

        for num in nums:

            if(num == 0):
                length_of_zero += 1
            else:
                if(length_of_zero != 0):
                    total += (length_of_zero * (length_of_zero + 1)) // 2
                    length_of_zero = 0
        
        if(length_of_zero != 0):
            total += (length_of_zero * (length_of_zero + 1)) // 2
        
        return total
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-zero-filled-subarrays/)