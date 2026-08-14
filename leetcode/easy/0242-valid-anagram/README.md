# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 6 ms (beats 93.31%)  
**Memory:** 19.5 MB (beats 30.18%)  
**Submitted:** 2026-08-14T15:46:16.610Z  

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        f=Counter(s)
        d=Counter(t)
        for i in f:
            if(f[i]!=d[i]):
                return False
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)