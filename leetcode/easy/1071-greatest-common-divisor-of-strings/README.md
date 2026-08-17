# Greatest Common Divisor of Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t +... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return  *the largest string* `x` *such that* `x` *divides both* `str1` *and* `str2`.

 

 **Example 1:** 

 **Input:**  str1 = "ABCABC", str2 = "ABC"

 **Output:**  "ABC"

 **Example 2:** 

 **Input:**  str1 = "ABABAB", str2 = "ABAB"

 **Output:**  "AB"

 **Example 3:** 

 **Input:**  str1 = "LEET", str2 = "CODE"

 **Output:**  ""

 **Example 4:** 

 **Input:**  str1 = "AAAAAB", str2 = "AAA"

 **Output:**  ""​​​​​​​

 

 **Constraints:** 

- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 73.64%)  
**Submitted:** 2026-08-17T17:49:46.945Z  

```py
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            min_val = min(len1, len2)
            for i in range(min_val, 0, -1):
                if len1 % i == 0 and len2 % i == 0:
                    return i
            return 1

        return str1[:gcd(len(str1), len(str2))]
```

---

[View on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)