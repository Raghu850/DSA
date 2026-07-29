# Quick Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort() so that the array becomes sorted in ascending order.

 **Examples:** 

```
Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: After sorting, all elements are arranged in ascending order.
```

```
Input: arr[] = [2, 1, 6, 10, 4, 1, 3, 9, 7]
Output: [1, 1, 2, 3, 4, 6, 7, 9, 10]
Explanation: Duplicate elements (1) are retained in sorted order.
```

```
Input: arr[] = [5, 5, 5, 5]
Output: [5, 5, 5, 5]
Explanation: All elements are identical, so the array remains unchanged.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T06:09:27.258Z  

```py
class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low<high:
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
            

    def partition(self, arr, low, high):
        # code here
        pivot=arr[low]
        i=low
        j=high
        while i<j:
            while i<=high and arr[i]<=pivot:
                i+=1
            while j>low and arr[j]>=pivot:
                j-=1
            if i<j:arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/quick-sort/1)