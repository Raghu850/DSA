# Permutations II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a collection of numbers, `nums`, that might contain duplicates, return  *all possible unique permutations  **in any order**.* 

 

Original
Python3
 **Example 1:** 

```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

```

 **Example 2:** 

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 93.86%)  
**Submitted:** 2026-11-26T16:57:43.649Z  

```py
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def next_perm(perm: List[int]) -> List[int]:
            i = n - 2
            while i >= 0 and perm[i] >= perm[i + 1]:
                i -= 1
            if i < 0:
                return perm[::-1]
            j = i + 1
            while j + 1 < n and perm[j + 1] > perm[i]:
                j += 1
            perm[i], perm[j] = perm[j], perm[i]
            perm[i + 1:] = perm[:i:-1]
            return perm
        permutations = [nums]
        current = nums
        while True:
            current = next_perm(current.copy())
            if current == permutations[0]:
                break
            permutations.append(current)
        return permutations
```

---

[View on LeetCode](https://leetcode.com/problems/permutations-ii/)