# Floor in a Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array  **arr[]** and an integer  **x**, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the  **floor**  of x. If such an element does not exist, return -1.

 **Note:**  In case of multiple occurrences of floor of x, return the index of the last occurrence.

 **Examples** 

```
Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1.
```

```
Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 11
Output: 4
Explanation: Largest Number less than or equal to 11 is 10, whose indices are 3 and 4. The index of last occurrence is 4.

```

```
Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 0
Output: -1
Explanation: No element less than or equal to 0 is found. So, output is -1.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ x ≤ arr[n-1]

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T20:56:54.726Z  

```py
class Solution:
    def findFloor(self, arr, x):
        # code here
        l,h=0,len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]<=x:
                l=mid+1
            else:
                h=mid-1
        return h
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1)