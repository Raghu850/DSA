# Aggressive Cows

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]**, which denotes the positions of stalls. All the positions are distinct. There are **k**  aggressive cows.

Assign the cows to the stalls such that the **minimum**  distance between any two cows is  **maximized.** 

 **Examples:** 

```
Input: arr[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. The minimum distance between any two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements.
```

```
Input: arr[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at arr[0], the second at arr[1], and the third at arr[4]. In this arrangement, the minimum distance between any two cows is 4 (between arr[1] and arr[4]), which is the maximum possible among all valid arrangements.
```

 **Constraints:** 
2 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 108
2 ≤ k ≤ arr.size()

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T22:22:03.850Z  

```py
class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()
        low =1
        high=stalls[-1]-stalls[0]
        def canPlace(stalls,k,mid):
            count=1
            last=stalls[0]
            for i in range(len(stalls)):
                if stalls[i]-last>=mid:
                    count+=1
                    last=stalls[i]
                    if count==k:
                        return True
            return False
        while low<high:
            mid=(low+high+1)//2
            if canPlace(stalls,k,mid):
                low=mid
            else:
                high=mid-1
        return low
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/aggressive-cows/1)