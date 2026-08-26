# Maximum Depth of Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, return  *its maximum depth*.

A binary tree's  **maximum depth**  is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

 **Example 1:** 

```
Input: root = [3,9,20,null,null,15,7]
Output: 3

```

 **Example 2:** 

```
Input: root = [1,null,2]
Output: 2

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 46.63%)  
**Memory:** 22.8 MB (beats 10.33%)  
**Submitted:** 2026-08-26T12:41:40.923Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        def chk(a):
            if(a.left == None and a.right == None):
                return 1
            elif(a.left == None and a.right != None):
                mx = chk(a.right) + 1
                return mx
            elif(a.left != None and a.right == None):
                mx = chk(a.left) + 1
                return mx
            else:
                mx = max(chk(a.left), chk(a.right))
                mx += 1
                return mx
        return chk(root)
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)