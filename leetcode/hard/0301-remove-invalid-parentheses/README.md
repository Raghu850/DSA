# Remove Invalid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return  *a list of  **unique strings**  that are valid with the minimum number of removals*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "()())()"
Output: ["(())()","()()()"]

```

 **Example 2:** 

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

```

 **Example 3:** 

```
Input: s = ")("
Output: [""]

```

 

 **Constraints:** 

- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 98.80%)  
**Memory:** 19.3 MB (beats 94.37%)  
**Submitted:** 2026-10-07T09:22:06.693Z  

```py
class Solution:  # Iterative
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        stack = [(s, 0, 0, ("(", ")"))]

        while stack:
            cur, li, lj, par = stack.pop()
            n = len(cur)
            bal = 0
            match = False

            for i in range(li, n):
                bal += (cur[i] == par[0]) - (cur[i] == par[1])
                if bal >= 0:
                    continue

                for j in range(lj, i + 1):
                    if cur[j] == par[1] and (j == lj or cur[j - 1] != par[1]):
                        nxt = cur[:j] + cur[j + 1 :]
                        stack.append((nxt, i, j, par))

                match = True
                break

            if not match:
                rev = cur[::-1]

                if par[0] == "(":
                    stack.append((rev, 0, 0, (")", "(")))
                else:
                    res.append(rev)

        return res
```

---

[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)