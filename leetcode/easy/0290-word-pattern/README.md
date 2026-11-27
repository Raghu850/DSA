# Word Pattern

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here  **follow**  means a full match, such that there is a bijection between a letter in `pattern` and a  **non-empty**  word in `s`. Specifically:

- Each letter in pattern maps to exactly one unique word in s.
- Each unique word in s maps to exactly one letter in pattern.
- No two letters map to the same word, and no two words map to the same letter.

 

Original
Python3
 **Example 1:** 

 **Input:**  pattern = "abba", s = "dog cat cat dog"

 **Output:**  true

 **Explanation:** 

The bijection can be established as:

- 'a' maps to "dog".
- 'b' maps to "cat".

 **Example 2:** 

 **Input:**  pattern = "abba", s = "dog cat cat fish"

 **Output:**  false

 **Example 3:** 

 **Input:**  pattern = "aaaa", s = "dog cat cat dog"

 **Output:**  false

 

 **Constraints:** 

- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 43.15%)  
**Submitted:** 2026-11-27T04:29:33.526Z  

```py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h={}
        a=list(map(str,s.split()))
        n=len(pattern)
        if n!=len(a):
            return False
        
        for i in range(n):
            if pattern[i] in h:
                if h[pattern[i]] != a[i]:
                    return False
            else:
                if a[i] in h.values():
                    return False
                h[pattern[i]]=a[i]
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/word-pattern/)