# Split Array Largest Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is  **minimized**.

Return  *the minimized largest sum of the split*.

A  **subarray**  is a contiguous part of the array.

 

 **Example 1:** 

```
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

```

 **Example 2:** 

```
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

```

 

 **Constraints:** 

- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 106
- 1 <= k <= min(50, nums.length)

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 71.12%)  
**Memory:** 19.3 MB (beats 46.77%)  
**Submitted:** 2026-08-09T17:06:51.692Z  

```py
class Solution:

    def helper(self, nums:List[int], perK : int, k : int) -> bool:
        count = 1
        sum = 0
        for num in nums:
            if(sum+num>perK):
                count+=1
                sum = num
            else:
                sum += num
        
        return count <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        high = sum(nums)
        low = max(nums)
        soln = 0
        while(low<=high):
            mid = low + (high-low)//2
            if(self.helper(nums, mid, k)):
                soln = mid
                high = mid-1
            else:
                low = mid + 1
        
        return soln
```

---

[View on LeetCode](https://leetcode.com/problems/split-array-largest-sum/)