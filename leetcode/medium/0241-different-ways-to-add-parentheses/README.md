# Different Ways to Add Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `expression` of numbers and operators, return  *all possible results from computing all the different possible ways to group numbers and operators*. You may return the answer in  **any order**.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed `104`.

 

Original
Python3
 **Example 1:** 

```
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

```

 **Example 2:** 

```
Input: expression = "2 *3-4* 5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2 *(3-(4* 5))) = -34 
((2 *3)-(4* 5)) = -14 
((2 *(3-4))* 5) = -10 
(2 *((3-4)* 5)) = -10 
(((2 *3)-4)* 5) = 10

```

 

 **Constraints:** 

- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].
- The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 50.58%)  
**Submitted:** 2026-11-24T08:58:17.896Z  

```py
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        memo = {}

        
        def compute(expr):
            
            if expr in memo:
                return memo[expr]
            
           
            res = []
            
          
            for i in range(len(expr)):
                if expr[i] in '+-*':  

                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    

                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            elif expr[i] == '*':
                                res.append(l * r)
            
           
            if not res:
                res.append(int(expr))
            
            
            memo[expr] = res
            return res
        
        
        return compute(expression)
```

---

[View on LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/)