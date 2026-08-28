# Leaf-Similar Trees

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a  **leaf value sequence**  *.* 

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered  *leaf-similar*  if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

 

 **Example 1:** 

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

```

 **Example 2:** 

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

```

 

 **Constraints:** 

- The number of nodes in each tree will be in the range [1, 200].
- Both of the given trees will have values in the range [0, 200].

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 83.37%)  
**Submitted:** 2026-08-28T16:21:43.032Z  

```py
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaf_values(root, leaf_values):
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2
```

---

[View on LeetCode](https://leetcode.com/problems/leaf-similar-trees/)