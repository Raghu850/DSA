# Find Kth Rotation

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an increasing sorted rotated array  **arr[]** of distinct integers. The array is right-rotated  **k**  times. Find the value of  **k**.
Let's suppose we have an array arr[] = [2, 4, 6, 9], if we rotate it by 2 times it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

 **Examples:** 

```
Input: arr[] = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is [5, 1, 2, 3, 4]. The original sorted array is [1, 2, 3, 4, 5]. We can see that the array was rotated 1 times to the right.

```

```
Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 107

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T07:48:56.699Z  

```py
class Solution:
    def findKRotation(self, arr):
        # code here
        l,h=0,len(arr)-1
        while l<h:
            mid=(l+h)//2
            if arr[mid]>arr[h]:
                l=mid+1
            else:
                h=mid
        return l
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/rotation4723/1)