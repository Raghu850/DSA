# Rotate String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `goal`, return `true`  *if and only if*  `s`  *can become*  `goal`  *after some number of  **shifts**  on*  `s`.

A  **shift**  on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

 

 **Example 1:** 

```
Input: s = "abcde", goal = "cdeab"
Output: true

```

 **Example 2:** 

```
Input: s = "abcde", goal = "abced"
Output: false

```

 

 **Constraints:** 

- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 15.88%)  
**Submitted:** 2026-08-14T15:45:53.243Z  

```py
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)
```

---

[View on LeetCode](https://leetcode.com/problems/rotate-string/)