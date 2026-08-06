# Ceil in a Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array  **arr[]** and an integer  **x**, find the index (0-based) of the smallest element in arr[] that is greater than or equal to x. This element is called the  **ceil**  of x. If such an element does not exist, return -1.

 **Note:**  In case of multiple occurrences of ceil of x, return the index of the first occurrence.

 **Examples** 

```
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.
```

```
Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.
```

```
Input: arr[] = [1, 1, 2, 8, 10, 11, 12, 19], x = 0
Output: 0
Explanation: Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ x ≤ arr[n-1]

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T21:04:22.920Z  

```py
class Solution:
    def findCeil(self, arr, x):
        # code here
        if x>arr[-1]:
            return -1
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>=x:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1)