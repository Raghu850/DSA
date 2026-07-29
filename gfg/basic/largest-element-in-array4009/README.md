# Largest in Array

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[].**  The task is to find the largest element and return it.

 **Examples:** 

```
Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
```

```
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
```

```
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
```

**Constraints:
**1 <= arr.size()<= 106
0 <= arr[i] <= 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T07:41:35.156Z  

```py
class Solution:
    def largest(self, arr):
        # code here
        m=arr[0]
        for i in arr:
            if i>m:
                m=i
        return m
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1)