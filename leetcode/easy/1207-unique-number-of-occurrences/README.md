# Unique Number of Occurrences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `arr`, return `true`  *if the number of occurrences of each value in the array is  **unique**  or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

 **Example 2:** 

```
Input: arr = [1,2]
Output: false

```

 **Example 3:** 

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

```

 

 **Constraints:** 

- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 39.55%)  
**Submitted:** 2026-08-20T08:37:49.396Z  

```py
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        cnt=set()
        for i in freq.values():
            if i in cnt:
                return False
            cnt.add(i)
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)