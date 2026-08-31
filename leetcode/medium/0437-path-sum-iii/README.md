# Path Sum III

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return  *the number of paths where the sum of the values along the path equals*  `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

 **Example 1:** 

```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

```

 **Example 2:** 

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 1000].
- -109 <= Node.val <= 109
- -1000 <= targetSum <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.5 MB  
**Submitted:** 2026-08-31T13:47:06.023Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        mp = {0: 1}
        count  = 0
        def dfs(root, currSum):
            nonlocal mp
            nonlocal count
            if root is None:
                return 0
            currSum += root.val
            find = currSum - target
            if find in mp:
                count += mp[find]
            mp[currSum] = mp.get(currSum, 0)+1
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            mp[currSum] -= 1
            currSum -= root.val
        dfs(root, 0)
        return count
            
```

---

[View on LeetCode](https://leetcode.com/problems/path-sum-iii/)