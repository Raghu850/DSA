# Edit Distance

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings `word1` and `word2`, return  *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

 

 **Example 1:** 

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

```

 **Example 2:** 

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

```

 

 **Constraints:** 

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 29 ms (beats 91.36%)  
**Memory:** 25.8 MB (beats 10.94%)  
**Submitted:** 2026-09-28T15:10:52.845Z  

```py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i==0: return j
            if j==0: return i
            if word1[i-1]==word2[j-1]:
                return dp(i-1, j-1)
            return min(dp(i-1,j), dp(i, j-1), dp(i-1,j-1)) + 1

        return dp(len(word1), len(word2))
```

---

[View on LeetCode](https://leetcode.com/problems/edit-distance/)