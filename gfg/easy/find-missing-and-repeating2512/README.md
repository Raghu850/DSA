# Missing And Repeating

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an unsorted array  **arr[]** of size  **n**, containing elements from the range  **1** to **n**, it is known that one number in this range is  **missing**, and another number  **occurs twice**  in the array, find both the  **duplicate** number and the  **missing** number.

**Examples:
**

```
Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and the missing number is 1.
```

```
Input: arr[] = [1, 3, 3] 
Output: [3, 2]
Explanation: Repeating number is 3 and the missing number is 2.
```

```
Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5.
```

 **Constraints:** 
2 ≤ n ≤ 106
1 ≤ arr[i] ≤ n

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T10:23:09.678Z  

```py
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        xr = 0

        # XOR array elements and numbers 1 to n
        for i in range(n):
            xr = xr ^ arr[i]
            xr = xr ^ (i + 1)

        # Find rightmost set bit
        bitNo = 0
        while True:
            if xr & (1 << bitNo):
                break
            bitNo += 1

        zero = 0
        one = 0

        # Divide both array elements and 1..n into two groups
        for i in range(n):
            if arr[i] & (1 << bitNo):
                one = one ^ arr[i]
            else:
                zero = zero ^ arr[i]

            if (i + 1) & (1 << bitNo):
                one = one ^ (i + 1)
            else:
                zero = zero ^ (i + 1)

        # Check which one is repeating
        cnt = 0
        for x in arr:
            if x == zero:
                cnt += 1

        if cnt == 2:
            return [zero, one]

        return [one, zero]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1)