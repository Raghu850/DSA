# Union of 2 Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two  **sorted**  arrays  **a[]**  and  **b[]**, where each array may contain  **duplicate**  elements, the task is to return the elements in the  **union**  of the two arrays in  **sorted**  order.
Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

 **Examples:** 

```
Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
```

```
Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: [1, 2, 3, 4, 5]
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
```

```
Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: [1, 2]
Explanation: Distinct elements including both the arrays are: 1 2.
```

 **Constraints:** 
1  ≤  a.size(), b.size()  ≤  105
-109 ≤ a[i], b[i] ≤109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-30T04:34:12.285Z  

```py
class Solution:
    def findUnion(self, a, b):
        # code here 
        i,j=0,0
        ans=[]
        n=len(a)
        m=len(b)
        while i<n and j<m:
            if a[i]<=b[j]:
                if not ans or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
            else:
                if not ans or ans[-1]!=b[j]:
                    ans.append(b[j])
                j+=1
        while i<n:
            if ans[-1]!=a[i]:
                ans.append(a[i])
            i+=1
        while j<m:
            if ans[-1]!=b[j]:
                ans.append(b[j])
            j+=1
        return ans
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1)