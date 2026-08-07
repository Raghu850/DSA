# Square Root

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer  **n,**  find the **square root** of n. If  **n**  is not a perfect square, then return the  **floor value**.

 **Floor value** of any number is the greatest Integer which is less than or equal to that number.

 **Examples:** 

```
Input: n = 4
Output: 2
Explanation: Since, 4 is a perfect square, so its square root is 2.

```

```
Input: n = 11
Output: 3
Explanation: Since, 11 is not a perfect square, floor of square root of 11 is 3.
```

```
Input: n = 1
Output: 1
Explanation: 1 is a perfect sqaure, so its square root is 1.
```

 **Constraints:** 
1 ≤ n ≤ 3*104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T20:02:14.150Z  

```py
class Solution:
    def floorSqrt(self, n): 
        # code here
        l,h=1,n
        ans=1
        while l<=h:
            mid=(l+h)//2
            cur=mid*mid
            if cur<=n:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/square-root/1)