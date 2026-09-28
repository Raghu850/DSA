# Counting Bits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `n`, return  *an array* `ans` *of length* `n + 1` *such that for each* `i` (`0 <= i <= n`) *,* `ans[i]` *is the  **number of*** `1` ***'s**  in the binary representation of *`i`.

Do not solve it with built-in functions (i.e., like `__builtin_popcount` in C++).

 

 **Example 1:** 

```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

```

 **Example 2:** 

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

```

 

 **Constraints:** 

- 0 <= n <= 105

 

 **Follow up:** 

- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 21 MB (beats 5.84%)  
**Submitted:** 2026-09-28T14:21:06.488Z  

```py
class Solution:
    ans=[0]
    for i in range(1,10**5+1):
        ans.append(ans[i>>1]+(i&1))
    def countBits(self, n: int) -> list[int]:
        return self.ans[:n+1]
```

---

[View on LeetCode](https://leetcode.com/problems/counting-bits/)