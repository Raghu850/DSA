# Reverse Vowels of a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

 **Example 1:** 

 **Input:**  s = "IceCreAm"

 **Output:**  "AceCreIm"

 **Explanation:** 

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

 **Example 2:** 

 **Input:**  s = "leetcode"

 **Output:**  "leotcede"

 

 **Constraints:** 

- 1 <= s.length <= 3 * 105
- s consist of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 8 ms (beats 64.87%)  
**Memory:** 20.5 MB (beats 51.80%)  
**Submitted:** 2026-08-18T05:24:39.709Z  

```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        k=list(s)
        v=set('aeiouAEIOU')
        while i<=j:
            if k[i] not in v:
                i+=1
            elif k[j] not in v:
                j-=1
            else:
                k[i],k[j]=k[j],k[i]
                i+=1
                j-=1
        return ''.join(k)
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)