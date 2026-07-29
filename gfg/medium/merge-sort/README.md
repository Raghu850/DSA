# Merge Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

 **Examples:** 

```
Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: We get the sorted array after using merge sort

```

```
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: We get the sorted array after using merge sort 
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T05:10:44.945Z  

```py
class Solution:
    def mergeSort(self, arr, l, r):
        # code here
        def merge(arr,l,mid,r):
            temp=[]
            left=l
            right=mid+1
            while left<=mid and right<=r:
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1
            while left<=mid:
                temp.append(arr[left])
                left+=1
            while right<=r:
                temp.append(arr[right])
                right+=1
            for i in range(l,r+1):
                arr[i]=temp[i-l]
        if l>=r: return
        mid=(l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/merge-sort/1)