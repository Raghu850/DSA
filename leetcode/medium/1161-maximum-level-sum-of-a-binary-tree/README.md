# Maximum Level Sum of a Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the  **smallest**  level `x` such that the sum of all the values of nodes at level `x` is  **maximal**.

 

 **Example 1:** 

```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

```

 **Example 2:** 

```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 104].
- -105 <= Node.val <= 105

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 86.90%)  
**Memory:** 22.9 MB (beats 69.40%)  
**Submitted:** 2026-09-02T15:57:35.186Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        idx, Sum=0, -inf
        q=deque()
        q.append(root)
        level=1
        while q:
            qz=len(q)
            curSum=0
            for i in range(qz):
                Node=q.popleft()
                curSum+=Node.val
                if Node.left: q.append(Node.left)
                if Node.right: q.append(Node.right)
            if curSum>Sum:
                idx, Sum=level, curSum
            level+=1
        return idx
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)