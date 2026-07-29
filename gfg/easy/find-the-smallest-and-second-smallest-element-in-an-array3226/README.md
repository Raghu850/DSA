# First and Second Smallests

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array,  **arr[]**  of integers, your task is to return the  **smallest**  and  **second smallest**  element in the array. If the smallest and second smallest do not exist, return  **-1.** 

 **Examples:** 

```
Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3] 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
```

```
Input: arr[] = [1, 1, 1]
Output: [-1]
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
```

 **Constraints:** 
1 ≤ arr.size ≤105
1 ≤ arr[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T08:12:22.497Z  

```py
class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        f=float('inf')
        s=float('inf')
        for i in arr:
            if i<f:
                s=f
                f=i
            elif f<i<s:
                s=i
        return [f,s] if s!=float('inf') else [-1]
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-the-smallest-and-second-smallest-element-in-an-array3226/1)