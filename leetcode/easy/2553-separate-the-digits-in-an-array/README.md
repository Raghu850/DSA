# Separate the Digits in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of positive integers `nums`, return  *an array* `answer` *that consists of the digits of each integer in* `nums` *after separating them in  **the same order**  they appear in* `nums`.

To separate the digits of an integer is to get all the digits it has in the same order.

- For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

 

 **Example 1:** 

```
Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.

```

 **Example 2:** 

```
Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].

```

 

 **Constraints:** 

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 82.32%)  
**Memory:** 19.4 MB (beats 79.60%)  
**Submitted:** 2026-11-06T10:26:51.579Z  

```py
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num > 9:
                for d in str(num):
                    res.append(int(d))
            else:
                res.append(num)
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/separate-the-digits-in-an-array/)