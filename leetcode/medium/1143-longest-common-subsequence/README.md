# Longest Common Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings `text1` and `text2`, return  *the length of their longest  **common subsequence**.* If there is no  **common subsequence**, return `0`.

A  **subsequence**  of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, "ace" is a subsequence of "abcde".

A  **common subsequence**  of two strings is a subsequence that is common to both strings.

 

 **Example 1:** 

```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

```

 **Example 2:** 

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

```

 **Example 3:** 

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

```

 

 **Constraints:** 

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

## Solution

**Language:** Python  
**Runtime:** 133 ms (beats 98.38%)  
**Memory:** 19.3 MB (beats 97.83%)  
**Submitted:** 2026-09-26T05:58:00.833Z  

```py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest = 0

        for c in text2:
            cur_length = 0
            for i, val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)
        
        return longest
```

---

[View on LeetCode](https://leetcode.com/problems/longest-common-subsequence/)