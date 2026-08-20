# Determine if Two Strings Are Close

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Two strings are considered  **close**  if you can attain one from the other using the following operations:

- Operation 1: Swap any two existing characters. For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character. For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` *if* `word1` *and* `word2` *are  **close**, and* `false` *otherwise.* 

 

 **Example 1:** 

```
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

```

 **Example 2:** 

```
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

```

 **Example 3:** 

```
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

```

 

 **Constraints:** 

- 1 <= word1.length, word2.length <= 105
- word1 and word2 contain only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-08-20T09:00:43.600Z  

```py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        v1 = c1.values()
        v2 = c2.values()
        k1 = c1.keys()
        k2 = c2.keys()
        if sorted(k1) != sorted(k2):
            return False
        for val1, val2 in zip(sorted(v1), sorted(v2)):
            if val1 != val2:
                return False
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/)