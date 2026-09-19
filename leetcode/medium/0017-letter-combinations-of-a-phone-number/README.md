# Letter Combinations of a Phone Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in  **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

 **Example 1:** 

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

 **Example 2:** 

```
Input: digits = "2"
Output: ["a","b","c"]

```

 

 **Constraints:** 

- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 78.89%)  
**Submitted:** 2026-09-19T08:46:35.323Z  

```py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        to_return = []
        cur = []
        mapping = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        def helper(i):
            if i >= len(digits):
                if len(cur)>0:
                    to_return.append("".join(cur))
                return
            else:
                for c in mapping[digits[i]]:
                    cur.append(c)
                    helper(i+1)
                    cur.pop()
        helper(0)
        return to_return

```

---

[View on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)