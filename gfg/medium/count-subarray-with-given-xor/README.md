# Count Subarrays with given XOR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers  **arr[]**  and a number  **k**, count the number of subarrays having  **XOR**  of their elements as  **k**.

 **Note:** It is guranteed that the total count will fit within a 32-bit integer.

**Examples: 
**

```
Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
```

```
Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
```

```
Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].
```

**Constraints:
**1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
0 ≤ k ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T05:03:05.967Z  

```py
class Solution:
    def subarrayXor(self, arr, m):
        # code here
        xr=0
        a={0:1}
        cnt=0
        for i in range(len(arr)):
            xr=xr^arr[i]
            x=xr^m
            cnt+=a.get(x,0)
            a[xr]=a.get(xr,0)+1
        return cnt
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/count-subarray-with-given-xor/1)