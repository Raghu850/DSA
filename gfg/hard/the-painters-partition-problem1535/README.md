# The Painter's Partition Problem-II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array  **arr[]**  where each element denotes the length of a board, and an integer  **k**  representing the number of  **painters**  available. Each painter takes  **1**  unit of time to paint  **1 unit length**  of a board.

Determine the  **minimum**  amount of time required to paint all the boards, under the constraint that each painter can paint only a  **contiguous**  sequence of boards (no skipping or splitting allowed).

 **Examples:** 

```
Input: arr[] = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The optimal allocation of boards among 3 painters is - 
Painter 1 → [5, 10] → time = 15
Painter 2 → [30] → time = 30
Painter 3 → [20, 15] → time = 35
Job will be done when all painters finish i.e. at time = max(15, 30, 35) = 35
```

```
Input: arr[] = [10, 20, 30, 40], k = 2
Output: 60
Explanation: A valid optimal partition is - 
Painter 1 → [10, 20, 30] → time = 60
Painter 2 → [40] → time = 40
Job will be complete at time = max(60, 40) = 60
```

```
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 1000
Explanation: There is only one painter, so the painter must paint all boards sequentially. The total time taken will be the sum of all board lengths, i.e., 100 + 200 + 300 + 400 = 1000.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
1 ≤ k ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-11T20:09:26.136Z  

```py
class Solution:
    def minTime(self, arr, k):
        
        low = max(arr)
        high = sum(arr)
        result = high
        
        def is_possible(max_time):
            painters = 1
            current_time = 0
            
            for time in arr:
                if current_time + time > max_time:
                    painters += 1
                    current_time = time
                    
                    if painters > k:
                        return False
                else:
                    current_time += time
            
            return True
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1)