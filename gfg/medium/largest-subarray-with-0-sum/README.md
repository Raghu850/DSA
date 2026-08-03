# Largest subarray with 0 sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]** containing both positive and negative integers, the task is to find the  **length**  of the  **longest**  **subarray**  with a sum equals to  **0.** 

 **Note:** A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

 **Examples:** 

```
Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].
```

```
Input: arr[] = [2, 10, 4]
Output: 0
Explanation: There is no subarray with a sum of 0.
```

```
Input: arr[] = [1, 0, -4, 3, 1, 0]
Output: 5
Explanation: The longest subarray with sum equals to 0 is [0, -4, 3, 1, 0]
```

 **Constraints:** 
1 ≤ arr.size() ≤ 106
−103 ≤ arr[i] ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-03T19:53:20.679Z  

```py
class Solution:
    def maxLength(self, arr):
        # code here
        a={}
        maxi=0
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==0:
                maxi=i+1
            else:
                if sum in a:
                    maxi=max(maxi,i-a[sum])
                else:
                    a[sum]=i
        return maxi
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1)