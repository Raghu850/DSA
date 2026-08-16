# Sum of Beauty of All Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The  **beauty**  of a string is the difference in frequencies between the most frequent and least frequent characters.

- For example, the beauty of "abaacc" is 3 - 1 = 2.

Given a string `s`, return  *the sum of  **beauty**  of all of its substrings.* 

 

 **Example 1:** 

```
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
```

 **Example 2:** 

```
Input: s = "aabcbaa"
Output: 17

```

 

 **Constraints:** 

- 1 <= s.length <= 500
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 1180 ms (beats 88.87%)  
**Memory:** 19.2 MB (beats 62.23%)  
**Submitted:** 2026-08-16T16:54:58.466Z  

```py
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0
        for i in range(n):
            freq = {}
            for j in range(i,n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                maxf = max(freq.values())
                minf = min(freq.values())
                total_beauty += maxf - minf
        return total_beauty
```

---

[View on LeetCode](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/)