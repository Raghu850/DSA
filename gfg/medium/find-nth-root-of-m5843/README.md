# Find nth root of m

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given 2 numbers  **n and m,**  the task is to find  **n√m**  (nth root of m). If the root is not integer then return  **-1**.

 **Examples :** 

```
Input: n = 3, m = 8
Output: 2
Explanation: 23 = 8

```

```
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.
```

```
Input: n = 4, m = 16
Output: 2
Explanation: 24 = 16
```

 **Constraints:** 
1 ≤ n ≤ 9
0 ≤ m ≤ 20

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T20:13:03.668Z  

```py
class Solution:
    def nthRoot(self, n, m):
       # code here
       l,h=0,m
       while l<=h:
           mid=(l+h)//2
           cur=mid**n
           if cur==m:
               return mid
           elif cur<m:
               l=mid+1
           else:
               h=mid-1
       return -1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1)