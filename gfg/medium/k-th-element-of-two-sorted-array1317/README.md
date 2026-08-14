# K-th element of two  Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two sorted arrays  **a[]** and  **b[]**  and an element  **k**, the task is to find the element that would be at the  **kth**  position of the combined sorted array.

 **Examples :** 

```
Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

```

```
Input: a[] = [1, 4, 8, 10, 12], b[] = [5, 7, 11, 15, 17], k = 6
Output: 10
Explanation: Combined sorted array is [1, 4, 5, 7, 8, 10, 11, 12, 15, 17]. The 6th element of this array is 10.
```

**Constraints:
**1 ≤ a.size(), b.size() ≤ 106
1 ≤ k ≤ a.size() + b.size()
0 ≤ a[i], b[i] ≤ 108

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T21:09:06.358Z  

```py
class Solution:
    def kthElement(self, a, b, k):
        # code here
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        m = len(b)

        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            leftA = float('-inf') if cut1 == 0 else a[cut1 - 1]
            leftB = float('-inf') if cut2 == 0 else b[cut2 - 1]

            rightA = float('inf') if cut1 == n else a[cut1]
            rightB = float('inf') if cut2 == m else b[cut2]

            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)

            elif leftA > rightB:
                high = cut1 - 1

            else:
                low = cut1 + 1

        return -1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1)