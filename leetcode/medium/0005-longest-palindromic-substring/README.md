# Longest Palindromic Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, return  *the longest*   *palindromic*   *substring*  in `s`.

 

 **Example 1:** 

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

```

 **Example 2:** 

```
Input: s = "cbbd"
Output: "bb"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solution

**Language:** Python  
**Runtime:** 111 ms (beats 96.72%)  
**Memory:** 19.3 MB (beats 69.01%)  
**Submitted:** 2026-08-16T16:53:46.718Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        b=0
        c=0
        l=1
        while l<=2*(n-c):
            i=0
            th=min(c,n-c-1)
            while i<th and s[c-i-1]==s[c+i+1]:
                i+=1
            if 2*i+1>l:
                b=c-i
                l=2*i+1
            i=0
            th=min(c+1,n-c-1)
            while i<th and s[c-i]==s[c+i+1]:
                i+=1
            if 2*i>l:
                b=c-i+1
                l=2*i
            c+=1    
        return s[b:b + l]
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)