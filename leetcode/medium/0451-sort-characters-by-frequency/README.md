# Sort Characters By Frequency

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, sort it in  **decreasing order**  based on the  **frequency**  of the characters. The  **frequency**  of a character is the number of times it appears in the string.

Return  *the sorted string*. If there are multiple answers, return  *any of them*.

 

 **Example 1:** 

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

```

 **Example 2:** 

```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

```

 **Example 3:** 

```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

```

 

 **Constraints:** 

- 1 <= s.length <= 5 * 105
- s consists of uppercase and lowercase English letters and digits.

## Solution

**Language:** Python  
**Runtime:** 39 ms (beats 5.59%)  
**Memory:** 28.2 MB (beats 12.82%)  
**Submitted:** 2026-08-15T16:49:49.124Z  

```py
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)

        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        buckets = [[] for _ in range(n + 1)]

        for char, count in freq.items():
            buckets[count].append(char)

        res = []

        for i in range(n, 0, -1):
            for char in sorted(buckets[i]):
                res.append(char * i)

        return ''.join(res)
```

---

[View on LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)