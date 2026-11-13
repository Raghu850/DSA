# To Lower Case

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, return  *the string after replacing every uppercase letter with the same lowercase letter*.

 

Original
Python3
 **Example 1:** 

```
Input:s = "Hello"Output: "hello"

```

 **Example 2:** 

```
Input:s = "here"Output: "here"

```

 **Example 3:** 

```
Input:s = "LOVELY"Output: "lovely"

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 39.58%)  
**Submitted:** 2026-11-13T16:45:12.252Z  

```py
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
```

---

[View on LeetCode](https://leetcode.com/problems/to-lower-case/)